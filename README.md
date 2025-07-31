# 🎙️ Flash Voice Clone App

This is a minimal web application that lets users upload:
- A reference audio sample (WAV format)
- A custom text input

It then uses **TTS (Text-to-Speech)** with voice cloning to generate new speech audio in the style of the reference voice — all running locally on CPU (Intel Mac supported).

---

## 🚀 Features

- 🔉 Voice cloning using reference audio
- 📝 Custom text-to-speech generation
- 🖥️ Runs entirely on CPU (no GPU needed)
- 🧼 Lightweight HTML frontend (Flash-style minimal UI)
- 🌐 Built with FastAPI + Coqui TTS

---

## 🛠️ Tech Stack

- Python 3.8+
- FastAPI (backend)
- Coqui TTS (voice cloning)
- HTML + JS (minimal frontend)

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/flash-voice-app.git
cd flash-voice-app
