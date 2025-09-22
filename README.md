<div align="center">

# Video Dubbing & Subtitle Generator

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.5.1-red.svg)](https://pytorch.org)
[![Whisper](https://img.shields.io/badge/OpenAI-Whisper-green.svg)](https://openai.com/research/whisper)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-orange.svg)](https://ffmpeg.org)

🎬 **Professional video dubbing and subtitle generation with AI-powered voice synthesis**

****

[🇬🇧 English](#english) | [🇹🇷 Türkçe](#türkçe)

</div>

---

## English

##  🇬🇧

### About This Project

Video Dubbing & Subtitle Generator is a comprehensive AI-powered toolkit designed for professional video localization and accessibility. This advanced system combines cutting-edge speech recognition, neural machine translation, and voice synthesis technologies to create high-quality dubbed videos and accurate subtitle files in multiple languages.

The project leverages OpenAI's Whisper for state-of-the-art speech recognition, advanced text-to-speech models for natural voice synthesis, and sophisticated speaker identification to maintain voice consistency across different speakers. Whether you're localizing content for international audiences or creating accessible versions of your videos, this tool delivers professional-grade results.

### ✨ Core Features

**1. Manual Dubbing (`manual_dubbing.py`)**

- Uses a provided SRT file with speaker tags
- Extracts voice characteristics for each speaker
- Translates subtitles to target language
- Synthesizes speech while maintaining speaker identity
- Creates a dubbed video

**2. Subtitle Generation (`subtitle_generator.py`)**

- Transcribes speech in videos
- Creates SRT subtitle files
- Optionally translates subtitles to target language

### 🛠️ Installation & Setup

#### System Requirements
- **Python 3.11+** with pip package manager
- **FFmpeg** for audio/video processing
- **CUDA-capable GPU** (recommended for faster processing)
- **Sufficient RAM** (8GB+ recommended for large models)

#### Required Dependencies
```bash
pip install -r requirements.txt
```

#### FFmpeg Installation

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install ffmpeg
```

**Arch Linux:**

```bash
sudo pacman -Syu ffmpeg
```

**Fedora:**

```bash
sudo dnf install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Download from [official FFmpeg website](https://ffmpeg.org/download.html) and add to PATH.

### 🚀 Usage Guide

#### 1. Subtitle Generation

Generate accurate SRT subtitle files from video content:

```bash
python subtitle_generator.py path/to/video.mp4 \
    --output subtitles.srt \
    --translate \
    --target-language tr \
    --source-language en \
    --model-size small
```

**Parameters:**
- `video_path`: Input video file path
- `--output (-o)`: Output SRT file path (optional)
- `--translate (-t)`: Enable translation to target language
- `--target-language`: Target language code (default: en)
- `--source-language`: Source language (auto-detected if not specified)
- `--model-size`: Whisper model size (tiny/base/small/medium/large)
- `--temp-dir`: Temporary processing directory

#### 2. Manual Dubbing

Create dubbed videos using existing SRT files with speaker tags:

```bash
python manual_dubbing.py path/to/video.mp4 path/to/subtitles.srt \
    --output dubbed_video.mp4 \
    --target-language tr \
    --temp-dir temp_processing
```

**Parameters:**
- `video_path`: Input video file
- `srt_path`: SRT file with speaker tags
- `--output (-o)`: Output dubbed video path
- `--target-language (-t)`: Target language for dubbing
- `--no-translate`: Skip translation, use original text
- `--temp-dir`: Temporary processing directory

#### SRT File Format with Speaker Tags

The manual dubbing system requires SRT files with speaker identification:

```srt
1
[speaker1]
00:00:01,000 --> 00:00:05,000
Hello, welcome to our presentation today.

2
[speaker2]
00:00:06,000 --> 00:00:10,000
Thank you for having me. I'm excited to share our findings.

3
[speaker1]
00:00:11,000 --> 00:00:15,000
Let's begin with the overview of our research methodology.
```

### 🌍 Language Support

The system supports comprehensive language processing through integrated AI models:

**Supported Languages:**
- **English (en)** 
- **Turkish (tr)** 
- **Spanish (es)** 
- **French (fr)**
- **German (de)** 
- **Italian (it)** 
- **Portuguese (pt)**

### 🔧 Advanced Configuration

#### Model Selection
Choose appropriate Whisper model based on your needs:

- **tiny**: Fastest processing, basic accuracy 
- **base**: Balanced speed and accuracy 
- **small**: Good accuracy for most use cases 
- **medium**: Higher accuracy for complex audio 
- **large**: Maximum accuracy for professional use

### 🎥 Workflow Examples

#### Complete Localization Pipeline
```bash
# Step 1: Generate subtitles from original video
python subtitle_generator.py original_video.mp4 \
    --output english_subs.srt \
    --source-language en

# Step 2: Translate subtitles to target language
python subtitle_generator.py original_video.mp4 \
    --output turkish_subs.srt \
    --translate \
    --target-language tr \
    --source-language en

# Step 3: Create dubbed version
python manual_dubbing.py original_video.mp4 turkish_subs.srt \
    --output turkish_dubbed.mp4 \
    --target-language tr
```

---

## Türkçe

## 🇹🇷 

### Proje Hakkında

Video Dublaj ve Altyazı Üretici, profesyonel video yerelleştirme ve erişilebilirlik için tasarlanmış kapsamlı bir AI destekli araç setidir. Bu gelişmiş sistem, çok dilli yüksek kaliteli dublajlı videolar ve doğru altyazı dosyaları oluşturmak için son teknoloji konuşma tanıma, sinir ağı makine çevirisi ve ses sentezi teknolojilerini birleştirir.

Proje, son teknoloji konuşma tanıma için OpenAI'nın Whisper'ını, doğal ses sentezi için gelişmiş text-to-speech modellerini ve farklı konuşmacılar arasında ses tutarlılığını korumak için gelişmiş konuşmacı tanımlamayı kullanır. İçeriği uluslararası kitleler için yerelleştiriyor veya videolarınızın erişilebilir versiyonlarını oluşturuyor olun, bu araç profesyonel seviye sonuçlar sunar.

### ✨ Temel Özellikler

**1. Manuel Dublaj (`manual_dubbing.py`)**

- Konuşmacı etiketleri içeren bir SRT dosyası kullanır
- Her konuşmacı için ses özelliklerini çıkarır
- Altyazıları hedef dile çevirir
- Konuşmacı kimliğini koruyarak konuşma sentezler
- Dublajlı bir video oluşturur

**2. Altyazı Oluşturma (`subtitle_generator.py`)**

- Videolardaki konuşmaları yazıya döker
- SRT altyazı dosyaları oluşturur
- İsteğe bağlı olarak altyazıları hedef dile çevirir

### 🛠️ Kurulum ve Ayarlar

#### Sistem Gereksinimleri
- **Python 3.11+** ve pip paket yöneticisi
- **FFmpeg** ses/video işleme için
- **CUDA-capable GPU** (daha hızlı işleme için önerilen)
- **Yeterli RAM** (büyük modeller için 8GB+ önerilen)

#### Gerekli Bağımlılıklar
```bash
pip install -r requirements.txt
```

#### FFmpeg Kurulumu

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install ffmpeg
```

**Arch Linux:**

```bash
sudo pacman -Syu ffmpeg
```

**Fedora:**

```bash
sudo dnf install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
[Resmi FFmpeg web sitesinden](https://ffmpeg.org/download.html) indirin ve PATH'e ekleyin.

### 🚀 Kullanım Kılavuzu

#### 1. Altyazı Üretimi

Video içeriğinden doğru SRT altyazı dosyaları üretin:

```bash
python subtitle_generator.py video/yolu.mp4 \
    --output altyazilar.srt \
    --translate \
    --target-language tr \
    --source-language en \
    --model-size small
```

**Parametreler:**
- `video_path`: Giriş video dosyası yolu
- `--output (-o)`: Çıktı SRT dosya yolu (isteğe bağlı)
- `--translate (-t)`: Hedef dile çeviriyi etkinleştir
- `--target-language`: Hedef dil kodu (varsayılan: en)
- `--source-language`: Kaynak dil (belirtilmezse otomatik algılanır)
- `--model-size`: Whisper model boyutu (tiny/base/small/medium/large)
- `--temp-dir`: Geçici işleme dizini

#### 2. Manuel Dublaj

Konuşmacı etiketleri olan mevcut SRT dosyalarını kullanarak dublajlı videolar oluşturun:

```bash
python manual_dubbing.py video/yolu.mp4 altyazilar/yolu.srt \
    --output dublajli_video.mp4 \
    --target-language tr \
    --temp-dir temp_isleme
```

**Parametreler:**
- `video_path`: Giriş video dosyası
- `srt_path`: Konuşmacı etiketleri olan SRT dosyası
- `--output (-o)`: Çıktı dublajlı video yolu
- `--target-language (-t)`: Dublaj için hedef dil
- `--no-translate`: Çeviriyi atla, orijinal metni kullan
- `--temp-dir`: Geçici işleme dizini

#### Konuşmacı Etiketli SRT Dosya Formatı

Manuel dublaj sistemi konuşmacı tanımlaması olan SRT dosyaları gerektirir:

```srt
1
[speaker1]
00:00:01,000 --> 00:00:05,000
Merhaba, bugünkü sunumumuza hoş geldiniz.

2
[speaker2]
00:00:06,000 --> 00:00:10,000
Beni ağırladığınız için teşekkür ederim. Bulgularımızı paylaşmak için heyecanlıyım.

3
[speaker1]
00:00:11,000 --> 00:00:15,000
Araştırma metodolojimizin genel bakışı ile başlayalım.
```

### 🌍 Dil Desteği

Sistem, entegre AI modelleri aracılığıyla kapsamlı dil işlemeyi destekler:

**Desteklenen Diller:**
- **İngilizce (en)** 
- **Türkçe (tr)** 
- **İspanyolca (es)** 
- **Fransızca (fr)** 
- **Almanca (de)** 
- **İtalyanca (it)** 
- **Portekizce (pt)** 

### 🔧 Gelişmiş Yapılandırma

#### Model Seçimi
İhtiyaçlarınıza göre uygun Whisper modelini seçin:

- **tiny**: En hızlı işleme, temel doğruluk
- **base**: Dengeli hız ve doğruluk
- **small**: Çoğu kullanım için iyi doğruluk
- **medium**: Karmaşık ses için daha yüksek doğruluk 
- **large**: Profesyonel kullanım için maksimum doğruluk

### 🎥 İş Akışı Örnekleri

#### Komple Yerelleştirme Hattı
```bash
# Adım 1: Orijinal videodan altyazı üret
python subtitle_generator.py orijinal_video.mp4 \
    --output ingilizce_altyazi.srt \
    --source-language en

# Adım 2: Altyazıları hedef dile çevir
python subtitle_generator.py orijinal_video.mp4 \
    --output turkce_altyazi.srt \
    --translate \
    --target-language tr \
    --source-language en

# Adım 3: Dublajlı versiyon oluştur
python manual_dubbing.py orijinal_video.mp4 turkce_altyazi.srt \
    --output turkce_dublaj.mp4 \
    --target-language tr
```
