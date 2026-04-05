# 🎬 Auto Generate Video AI

> 🚀 Automatically generate short videos from ideas using AI.

---

## 📌 Overview

**Auto Generate Video AI** is a Python-based application that transforms simple ideas into ready-to-use videos.

This project focuses on automating the content creation process by combining:

- Script generation
- Text-to-speech conversion
- Stock video retrieval
- Video rendering

---

## ⚡ Features

- 🎯 Input idea → auto generate script
- 🔊 Convert text to voice (gTTS)
- 🎥 Download stock video (Pexels API)
- ✂️ Combine video and audio (MoviePy)
- 📱 Output vertical video (9:16 format)

---

## 🗂️ Project Structure

```
AUTO_GENERATE_VIDEO/
│
├── assets/              # Generated files (video, audio)
│   ├── video.mp4
│   ├── voice.mp3
│   └── final.mp4
│
├── generator.py         # Script generator
├── video.py             # Video processing
├── main.py              # Main entry point
├── config.py            # Configuration (API keys, settings)
├── requirements.txt     # Dependencies
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/auto-video.git
cd auto-video
```

---

### 2. Create virtual environment (recommended)

```
python -m venv .venv
```

Activate it:

**Windows (PowerShell):**

```
.venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Configuration

This project uses a configuration file for API keys and settings.

### 1. Copy example config

```bash
cp config.example.py config.py
```

**Windows (PowerShell):**

```bash
copy config.example.py config.py
```

---

### 2. Edit `config.py`

```python
PEXELS_API_KEY = "YOUR_API_KEY"
OUTPUT_VIDEO = "assets/final.mp4"
VIDEO_DURATION = 30
```

Get your API key from:
https://www.pexels.com/api/

---

## ▶️ Usage

Run the application:

```
python main.py
```

Example input:

```
Input idea: space facts
```

---

## 🎬 Output

Generated files:

- 📹 `assets/final.mp4` → final video
- 🔊 `assets/voice.mp3` → generated audio
- 🎥 `assets/video.mp4` → downloaded stock video

---

## 📱 Video Format

The output video is optimized for vertical viewing:

- Resolution: **1080 x 1920**
- Aspect Ratio: **9:16**
- Format: **MP4**

---

## 🧠 Example Ideas

- "Top 5 Space Facts"
- "Interesting Facts About AI"
- "Daily Motivation"
- "Did You Know?"

---

## 🚧 Future Improvements

- Subtitles generator
- Background music integration
- More advanced AI voice
- Multiple video generation
- UI / Web dashboard

---

## ⚠️ Limitations

- Pexels API has request limits (free tier)
- gTTS requires internet connection
- Video results depend on search keywords

---

## 🔐 Security Notes

Do NOT upload the following files to GitHub:

- `config.py` (contains API keys)
- `assets/` folder

Use `.gitignore` to protect sensitive data.

---

## 📜 License

MIT License — free to use and modify.

---

## 💡 Author Notes

This project is built for:

- Learning AI automation
- Experimenting with content generation
- Building scalable video tools

---

## ⭐ Support

If you find this project useful:

- ⭐ Star this repository
- 🍴 Fork and improve it
- 🚀 Share with others

---

🔥 _Turn ideas into videos automatically._
