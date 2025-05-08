#!/usr/bin/env python3
"""
Manual dubbing module
--------------------
Takes a video file and an SRT file with speaker tags,
and creates a dubbed version using voice cloning.
"""
import os
import argparse
import torch
from collections import defaultdict
from TTS.api import TTS
from pydub import AudioSegment
import soundfile as sf
import deepl
from utils import (extract_audio_from_video, remove_silence, overlay_audio_on_video,
                  cleanup_files, get_device, srt_time_to_ms, load_srt_file, ensure_dir)

class ManualDubber:
    def __init__(self, device=None, temp_dir="temp", target_language="en"):
        """Initialize the manual dubber."""
        # Setup environment
        self.device = device if device is not None else get_device()
        self.temp_dir = ensure_dir(temp_dir)
        self.target_language = target_language
        
        # Initialize TTS
        os.environ["COQUI_TOS_AGREED"] = "1"  # Accept terms of service for TTS
        self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(self.device)
        
        # Initialize translator
        try:
            self.translator = deepl.Translator("da952e5e-99f3-49be-b09f-a4c897d561b7:fx")
        except Exception as e:
            print(f"Warning: Could not initialize DeepL translator: {e}")
            self.translator = None
    
    def translate_text(self, text, source_lang=None, target_lang=None):
        """Translate text to target language."""
        if not self.translator:
            print(f"Warning: No translator available. Returning original text.")
            return text
            
        target_lang = target_lang or self.target_language
        
        try:
            return str(self.translator.translate_text(
                text, 
                source_lang=source_lang, 
                target_lang=target_lang
            ))
        except Exception as e:
            print(f"Warning: Translation failed: {e}")
            return text
    
    def extract_speaker_audio(self, video_audio, segments_by_speaker, speaker):
        """Extract and combine all audio segments for a specific speaker."""
        combined_audio = AudioSegment.silent(duration=0)
        
        for segment in segments_by_speaker[speaker]:
            start_ms = srt_time_to_ms(segment['start_time'])
            end_ms = srt_time_to_ms(segment['end_time'])
            combined_audio += video_audio[start_ms:end_ms]
        
        return combined_audio
    
    def synthesize_speech(self, text, speaker_audio_path):
        """Synthesize speech using TTS with voice cloning."""
        temp_tts_path = os.path.join(self.temp_dir, "temp_tts_output.wav")
        
        # Generate speech using voice cloning
        wav = self.tts.tts(
            text=text,
            speaker_wav=speaker_audio_path,
            language=self.target_language
        )
        
        # Save and process the synthesized speech
        sf.write(temp_tts_path, wav, samplerate=22050)
        remove_silence(temp_tts_path)
        
        return temp_tts_path
    
    def process_video(self, video_path, srt_path, output_path=None, translate=True):
        """Process a video with an SRT file for manual dubbing."""
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        
        if not output_path:
            output_path = f"{base_name}_dubbed.mp4"
        
        # Extract audio from video
        print(f"Extracting audio from {video_path}...")
        audio_path = extract_audio_from_video(video_path, 
                                           os.path.join(self.temp_dir, f"{base_name}_audio.wav"))
        
        # Load original audio
        original_audio = AudioSegment.from_wav(audio_path)
        
        # Load and parse SRT file
        print(f"Loading SRT file: {srt_path}")
        segments = load_srt_file(srt_path)
        
        # Group segments by speaker
        segments_by_speaker = defaultdict(list)
        for segment in segments:
            speaker = segment.get('speaker', 'unknown')
            segments_by_speaker[speaker].append(segment)
        
        # Create a new audio segment for the dubbed audio
        dubbed_audio = AudioSegment.silent(duration=len(original_audio))
        
        # Process each speaker
        speaker_samples = {}
        for speaker in segments_by_speaker:
            print(f"Processing speaker: {speaker}")
            
            # Extract and save combined audio for the speaker
            speaker_audio = self.extract_speaker_audio(original_audio, segments_by_speaker, speaker)
            speaker_audio_path = os.path.join(self.temp_dir, f"{speaker}_audio.wav")
            speaker_audio.export(speaker_audio_path, format="wav")
            speaker_samples[speaker] = speaker_audio_path
        
        # Process each segment
        for segment in segments:
            speaker = segment.get('speaker', 'unknown')
            start_ms = srt_time_to_ms(segment['start_time'])
            end_ms = srt_time_to_ms(segment['end_time'])
            available_duration = end_ms - start_ms
            
            # Translate the text if requested
            text = segment['text']
            if translate:
                text = self.translate_text(text)
            
            # Synthesize speech
            speaker_sample = speaker_samples.get(speaker, audio_path)
            tts_path = self.synthesize_speech(text, speaker_sample)
            
            # Adjust timing
            tts_audio = AudioSegment.from_wav(tts_path)
            tts_duration = len(tts_audio)
            
            if tts_duration > available_duration:
                # Simple approach: truncate if too long
                tts_audio = tts_audio[:available_duration]
            elif tts_duration < available_duration:
                # Add silence if too short
                tts_audio += AudioSegment.silent(duration=available_duration - tts_duration)
            
            # Overlay at the correct position
            dubbed_audio = dubbed_audio.overlay(tts_audio, position=start_ms)
        
        # Export the final dubbed audio
        dubbed_audio_path = os.path.join(self.temp_dir, "dubbed_audio.wav")
        dubbed_audio.export(dubbed_audio_path, format="wav")
        
        # Combine video with dubbed audio
        print(f"Creating final dubbed video: {output_path}")
        overlay_audio_on_video(video_path, dubbed_audio_path, output_path)
        
        # Clean up temporary files
        if os.path.exists(output_path):
            print(f"Dubbing complete! Output saved to: {output_path}")
            self.cleanup_temp_files()
        else:
            print("Error: Failed to create output video.")
        
        return output_path
    
    def cleanup_temp_files(self):
        """Clean up temporary files."""
        print("Cleaning up temporary files...")
        for file in os.listdir(self.temp_dir):
            file_path = os.path.join(self.temp_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)


def main():
    parser = argparse.ArgumentParser(description="Manual video dubbing with SRT file")
    parser.add_argument("video_path", help="Path to the video file")
    parser.add_argument("srt_path", help="Path to the SRT file with speaker tags")
    parser.add_argument("-o", "--output", help="Output path for dubbed video")
    parser.add_argument("-t", "--target-language", default="en", 
                      help="Target language for dubbing (default: en)")
    parser.add_argument("--no-translate", action="store_true", 
                      help="Skip translation and use original text")
    parser.add_argument("--temp-dir", default="temp", 
                      help="Temporary directory for processing files")
    
    args = parser.parse_args()
    
    # Create manual dubber and process video
    dubber = ManualDubber(
        temp_dir=args.temp_dir,
        target_language=args.target_language
    )
    
    output_path = args.output or f"{os.path.splitext(args.video_path)[0]}_dubbed.mp4"
    dubber.process_video(
        args.video_path, 
        args.srt_path, 
        output_path,
        translate=not args.no_translate
    )


if __name__ == "__main__":
    main()
