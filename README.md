# Video Dubbing & Subtitle Project / Video Dublaj ve Altyazı Projesi

## English

A comprehensive toolkit for automatic and manual video dubbing, along with subtitle generation. This tool allows you to create SRT subtitle files in any language for your videos and use these SRT files to make automatic dubbing.

### Features

#### 1. Manual Dubbing (`manual_dubbing.py`)

- Uses a provided SRT file with speaker tags
- Extracts voice characteristics for each speaker
- Translates subtitles to target language
- Synthesizes speech while maintaining speaker identity
- Creates a dubbed video

#### 2. Subtitle Generation (`subtitle_generator.py`)

- Transcribes speech in videos
- Creates SRT subtitle files
- Optionally translates subtitles to target language

### Requirements

- Python 3.11
- FFmpeg
- Torch 2.5.1

### Installation

#### Option 1: Local Installation

1. Clone the repository:

```bash
git clone https://github.com/koesan/Auto_Dubbing_And_Subtitle.git
cd Auto_Dubbing_And_Subtitle
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure FFmpeg is installed on your system.

### Usage

#### Manual Dubbing

This module takes a video file and an SRT file with speaker tags to create a dubbed version.

```bash
python manual_dubbing.py path/to/video.mp4 path/to/subtitles.srt --output output.mp4 --target-language tr
```

Parameters:

- `video_path`: Path to input video
- `srt_path`: Path to SRT file with speaker tags
- `-o, --output`: Output path for dubbed video (optional)
- `-t, --target-language`: Target language code (default: en)
- `--no-translate`: Skip translation and use original text
- `--temp-dir`: Temporary directory for processing files (default: temp)

SRT file format with speaker tags:

```
1
[speaker1]
00:00:01,000 --> 00:00:05,000
Hello, how are you?

2
[speaker2]
00:00:06,000 --> 00:00:10,000
I'm doing well, thank you!
```

#### Subtitle Generation

This module takes a video file and generates an SRT subtitle file.

```bash
python subtitle_generator.py path/to/video.mp4 --output subtitles.srt --translate --target-language tr --source-language en
```

Parameters:

- `video_path`: Path to input video
- `-o, --output`: Output path for SRT file (optional)
- `-t, --translate`: Translate subtitles to target language
- `--target-language`: Target language code (default: en)
- `--source-language`: Source language code (optional, auto-detected if not specified)
- `--model-size`: Whisper model size (tiny, base, small, medium, large) (default: small)
- `--temp-dir`: Temporary directory for processing files (default: temp)

### Supported Languages

The project supports the following languages for both speech recognition and translation through Whisper and DeepL integrations:

- English (en)
- Turkish (tr)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Portuguese (pt)

---

## Türkçe

Video dublajı ile altyazı oluşturma için kapsamlı bir araç seti. Bu araç ile videolarınıza istediğiniz dilde srt alt yazı dosaysı oluştrua bilirsiniz ve bu srt alt yazı dosyalarını kullanarak otomatik dublaj yapa bilirsiniz.

### Özellikler

#### 1. Manuel Dublaj (`manual_dubbing.py`)

- Konuşmacı etiketleri içeren bir SRT dosyası kullanır
- Her konuşmacı için ses özelliklerini çıkarır
- Altyazıları hedef dile çevirir
- Konuşmacı kimliğini koruyarak konuşma sentezler
- Dublajlı bir video oluşturur

#### 2. Altyazı Oluşturma (`subtitle_generator.py`)

- Videolardaki konuşmaları yazıya döker
- SRT altyazı dosyaları oluşturur
- İsteğe bağlı olarak altyazıları hedef dile çevirir

### Gereksinimler

- Python 3.11
- FFmpeg
- Torch 2.5.1

### Kurulum

#### Seçenek 1: Yerel Kurulum

1. Depoyu klonlayın:

```bash
git clone https://github.com/koesan/Auto_Dubbing_And_Subtitle.git
cd Auto_Dubbing_And_Subtitle
```

2. Bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

3. FFmpeg'in sisteminizde kurulu olduğundan emin olun.

### Kullanım

#### Manuel Dublaj

Bu modül, konuşmacı etiketleri içeren bir video dosyası ve bir SRT dosyası alarak dublajlı bir versiyon oluşturur.

```bash
python manual_dubbing.py video/yolu.mp4 altyazılar/yolu.srt --output çıktı.mp4 --target-language tr
```

Parametreler:

- `video_path`: Giriş videosu yolu
- `srt_path`: Konuşmacı etiketleri içeren SRT dosyasının yolu
- `-o, --output`: Dublajlı video için çıktı yolu (isteğe bağlı)
- `-t, --target-language`: Hedef dil kodu (varsayılan: en)
- `--no-translate`: Çeviriyi atla ve orijinal metni kullan
- `--temp-dir`: Dosyaları işlemek için geçici dizin (varsayılan: temp)

Konuşmacı etiketli SRT dosya formatı:

```
1
[speaker1]
00:00:01,000 --> 00:00:05,000
Merhaba, nasılsın?

2
[speaker2]
00:00:06,000 --> 00:00:10,000
İyiyim, teşekkür ederim!
```

#### Altyazı Oluşturma

Bu modül bir video dosyası alır ve bir SRT altyazı dosyası oluşturur.

```bash
python subtitle_generator.py video/yolu.mp4 --output altyazılar.srt --translate --target-language tr --source-language en
```

Parametreler:

- `video_path`: Giriş videosu yolu
- `-o, --output`: SRT dosyası için çıktı yolu (isteğe bağlı)
- `-t, --translate`: Altyazıları hedef dile çevir
- `--target-language`: Hedef dil kodu (varsayılan: en)
- `--source-language`: Kaynak dil kodu (isteğe bağlı, belirtilmezse otomatik algılanır)
- `--model-size`: Whisper model boyutu (tiny, base, small, medium, large) (varsayılan: small)
- `--temp-dir`: Dosyaları işlemek için geçici dizin (varsayılan: temp)

### Desteklenen Diller

Proje, Whisper ve DeepL entegrasyonları aracılığıyla hem konuşma tanıma hem de çeviri için aşağıdaki dilleri destekler:

- İngilizce (en)
- Türkçe (tr)
- İspanyolca (es)
- Fransızca (fr)
- Almanca (de)
- İtalyanca (it)
- Portekizce (pt)

---

file:///home/koesan/%C4%B0ndirilenler/Madara_dubbed_subl.mp4
-24:-82:64:64
