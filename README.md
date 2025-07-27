# 🤖 ChatFusion

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Gradio](https://img.shields.io/badge/Gradio-4.7+-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

*An intelligent, multilingual chatbot with speech recognition, translation, and text-to-speech capabilities*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API Reference](#-api-reference)

</div>

---

## 🌟 Overview

The **Advanced Multi-Faceted Chatbot** is a comprehensive language processing application that combines multiple AI-powered features into a single, user-friendly interface. Built with Python and Gradio, this chatbot can understand speech, translate between languages, process natural language, and convert text back to speech.

### 🎯 Key Capabilities

- **🗣️ Speech Recognition**: Convert audio input to text using Google's speech recognition
- **🌍 Multi-language Translation**: Translate text between 100+ languages using Google Translate
- **🎤 Voice Command Processing**: Execute simple voice commands and queries
- **📝 Natural Language Processing**: Clean and process text using advanced NLP techniques
- **🔊 Text-to-Speech**: Convert processed text back to natural-sounding audio
- **🖥️ Web Interface**: Beautiful, responsive Gradio-based UI

---

## ✨ Features

### Core Functionality

| Feature | Description | Status |
|---------|-------------|--------|
| **Speech-to-Text** | Convert audio files or microphone input to text | ✅ Active |
| **Translation** | Translate between 100+ languages | ✅ Active |
| **Voice Commands** | Process basic voice commands (time, date, greetings) | ✅ Active |
| **Text Processing** | NLP preprocessing with tokenization and lemmatization | ✅ Active |
| **Text-to-Speech** | Convert text to natural audio | ✅ Active |
| **Multi-format Input** | Support for text, audio files, and microphone input | ✅ Active |

### Advanced Features

- **Real-time Processing**: Instant feedback and processing
- **Language Detection**: Automatically detect input language
- **Audio Format Support**: WAV, MP3, FLAC, and more
- **Responsive Design**: Works on desktop and mobile devices
- **Error Handling**: Comprehensive error management and user feedback
- **Temporary File Management**: Automatic cleanup of generated files

---

## 🚀 Installation

### Prerequisites

- **Python 3.8+** (recommended: Python 3.9 or 3.10)
- **Internet Connection** (required for translation and TTS services)
- **Microphone** (optional, for voice input)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/P-Soma-Sekhar-Pandu-Ranga-raju/ChatFusion
   cd advanced-chatbot
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   # Using venv
   python -m venv chatbot_env
   
   # Activate virtual environment
   # On Windows:
   chatbot_env\Scripts\activate
   # On macOS/Linux:
   source chatbot_env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK Data** (Automatic on first run)
   ```python
   # This happens automatically when you run the app
   # But you can also run manually:
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
   ```
---

## 📖 Usage

### Starting the Application

```bash
python app.py
```

The application will start and be available at: `http://localhost:7860`

### Using the Interface

#### 1. **Input Methods**
- **Text Input**: Type directly in the text box
- **Audio Upload**: Upload audio files (WAV, MP3, FLAC)
- **microphone**: Record directly in the browser

#### 2. **Feature Selection**
- **Translation**: Translate text between languages
- **Voice Command**: Process voice commands
- **Transcription**: Clean and process text using NLP

#### 3. **Language Codes**
Use these codes for translation:

| Language | Code | Language | Code | Language | Code |
|----------|------|----------|------|----------|------|
| English | `en` | Spanish | `es` | French | `fr` |
| German | `de` | Hindi | `hi` | Chinese | `zh` |
| Japanese | `ja` | Portuguese | `pt` | Russian | `ru` |
| Arabic | `ar` | Italian | `it` | Korean | `ko` |

### Example Usage Scenarios

#### Scenario 1: Translation
```
Input: "Hello, how are you today?"
Feature: Translation
Target Language: es
Output: "Hola, ¿cómo estás hoy?"
```

#### Scenario 2: Voice Command
```
Audio Input: "What time is it?"
Feature: Voice Command
Output: "Current time is 14:30:25"
```

#### Scenario 3: Text Processing
```
Input: "The quick brown fox jumps over the lazy dog"
Feature: Transcription
Output: "Original: The quick brown fox jumps over the lazy dog
         Processed: quick brown fox jump lazy dog"
```

---

## 🔧 API Reference

### Core Functions

#### `natural_language_understanding(text)`
Processes text using NLP techniques.

**Parameters:**
- `text` (str): Input text to process

**Returns:**
- `str`: Processed text with stopwords removed and words lemmatized

#### `translate_text(text, target_language)`
Translates text to target language.

**Parameters:**
- `text` (str): Text to translate
- `target_language` (str): Target language code

**Returns:**
- `str`: Translated text

#### `text_to_speech(text, language='en')`
Converts text to speech audio file.

**Parameters:**
- `text` (str): Text to convert
- `language` (str): Language code for TTS

**Returns:**
- `str`: Path to temporary audio file

<div align="center">


</div>
