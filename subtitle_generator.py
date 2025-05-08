import os
import argparse
import whisper
import deepl
from moviepy.editor import VideoFileClip
from utils import (extract_audio_from_video, format_time_to_srt, get_device, ensure_dir)

class SubtitleGenerator:
    def __init__(self, device=None, temp_dir="temp", model_size="small"):
        """Initialize the subtitle generator."""
        # Setup environment
        self.device = device if device is not None else get_device()
        self.temp_dir = ensure_dir(temp_dir)
        self.model_size = model_size
        self.model = None
        
        # Initialize translator
        try:
            self.translator = deepl.Translator("da952e5e-99f3-49be-b09f-a4c897d561b7:fx")
        except Exception as e:
            print(f"Warning: Could not initialize DeepL translator: {e}")
            self.translator = None
    
    def load_model(self):
        """Load the Whisper model."""
        if not self.model:
            print(f"Loading Whisper {self.model_size} model...")
            self.model = whisper.load_model(self.model_size, device=self.device)
        return self.model
    
    def transcribe_audio(self, audio_path, source_lang=None):
        """Transcribe audio using Whisper."""
        model = self.load_model()
        print("Transcribing audio...")
        
        # Use provided source language if specified
        if source_lang:
            print(f"Using source language: {source_lang}")
            result = model.transcribe(audio_path, verbose=True, language=source_lang)
        else:
            print("Language will be auto-detected by Whisper")
            result = model.transcribe(audio_path, verbose=True)
            
        return result
    
    def translate_text(self, text, source_lang=None, target_lang="en"):
        """Translate text to target language."""
        if not self.translator:
            print(f"Warning: No translator available. Returning original text.")
            return text
            
        try:
            return str(self.translator.translate_text(
                text, 
                source_lang=source_lang, 
                target_lang=target_lang
            ))
        except Exception as e:
            print(f"Warning: Translation failed: {e}")
            return text
    
    def create_srt_file(self, segments, output_path, translate=False, target_lang="en"):
        """Create SRT file from transcript segments."""
        print(f"Creating SRT file: {output_path}")
        with open(output_path, 'w', encoding='utf-8') as f:
            for idx, segment in enumerate(segments):
                start_time = format_time_to_srt(segment['start'])
                end_time = format_time_to_srt(segment['end'])
                
                # Translate the text if requested
                text = segment['text']
                if translate:
                    text = self.translate_text(text, target_lang=target_lang)
                
                f.write(f"{idx + 1}\n")
                f.write(f"{start_time} --> {end_time}\n")
                f.write(f"{text}\n\n")
    
    def process_video(self, video_path, output_path=None, translate=False, source_lang=None, target_lang="en"):
        """Process a video file to generate subtitles."""
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        
        if not output_path:
            suffix = f"_{target_lang}" if translate else ""
            output_path = f"{base_name}{suffix}.srt"
        
        # Extract audio from video
        print(f"Extracting audio from {video_path}...")
        audio_path = extract_audio_from_video(video_path, 
                                           os.path.join(self.temp_dir, f"{base_name}_audio.wav"))
        
        # Transcribe audio with source language
        result = self.transcribe_audio(audio_path, source_lang=source_lang)
        
        # Create SRT file
        self.create_srt_file(
            result['segments'], 
            output_path, 
            translate=translate, 
            target_lang=target_lang
        )
        
        # Clean up temporary files
        if os.path.exists(output_path):
            print(f"Subtitle generation complete! Output saved to: {output_path}")
            self.cleanup_temp_files()
        else:
            print("Error: Failed to create subtitle file.")
        
        return output_path
    
    def cleanup_temp_files(self):
        """Clean up temporary files."""
        print("Cleaning up temporary files...")
        for file in os.listdir(self.temp_dir):
            file_path = os.path.join(self.temp_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)


def main():
    parser = argparse.ArgumentParser(description="Generate subtitle files from videos")
    parser.add_argument("video_path", help="Path to the video file")
    parser.add_argument("-o", "--output", help="Output path for SRT file")
    parser.add_argument("-t", "--translate", action="store_true", 
                      help="Translate subtitles to target language")
    parser.add_argument("--source-language", 
                      help="Source language of the video (if not specified, will be auto-detected)")
    parser.add_argument("--target-language", default="en", 
                      help="Target language for translation (default: en)")
    parser.add_argument("--model-size", default="small", 
                      choices=["tiny", "base", "small", "medium", "large"],
                      help="Whisper model size (default: small)")
    parser.add_argument("--temp-dir", default="temp", 
                      help="Temporary directory for processing files")
    
    args = parser.parse_args()
    
    # Create subtitle generator and process video
    generator = SubtitleGenerator(
        temp_dir=args.temp_dir,
        model_size=args.model_size
    )
    
    output_path = args.output
    generator.process_video(
        args.video_path, 
        output_path, 
        translate=args.translate,
        source_lang=args.source_language,
        target_lang=args.target_language
    )


if __name__ == "__main__":
    main()