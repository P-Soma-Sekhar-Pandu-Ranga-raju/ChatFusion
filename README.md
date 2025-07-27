# 🤖 Advanced Multi-Faceted Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Gradio](https://img.shields.io/badge/Gradio-4.7+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

*An intelligent, multilingual chatbot with speech recognition, translation, and text-to-speech capabilities*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API Reference](#-api-reference) • [Contributing](#-contributing)

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
   git clone https://github.com/yourusername/advanced-chatbot.git
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

### 🐳 Docker Installation (Optional)

```dockerfile
# Dockerfile included in project
docker build -t advanced-chatbot .
docker run -p 7860:7860 advanced-chatbot
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

### Configuration Options

#### Launch Parameters
```python
iface.launch(
    server_name="0.0.0.0",  # Server host
    server_port=7860,       # Server port
    share=False,            # Create public link
    debug=True              # Enable debug mode
)
```

---

## 📁 Project Structure

```
advanced-chatbot/
├── 📄 app.py                 # Main application file
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # Project documentation
├── 📄 .gitignore            # Git ignore rules
├── 📁 temp/                 # Temporary files (auto-created)
├── 📁 audio_outputs/        # Generated audio files
└── 📁 __pycache__/          # Python cache files
```

---

## 🛠️ Development

### Setting Up Development Environment

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/advanced-chatbot.git
   ```
3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make changes and test**
5. **Submit a pull request**

### Adding New Features

#### Adding a New Voice Command
```python
def process_voice_command(text):
    text_lower = text.lower()
    
    # Add your new command here
    if 'your_command' in text_lower:
        return "Your response here"
    
    # ... existing commands
```

#### Adding New Languages
```python
# Language codes are handled automatically by Google Translate
# Just use the appropriate language code in the interface
```

### Testing

```bash
# Run basic tests
python -m pytest tests/

# Test specific components
python -c "from app import natural_language_understanding; print(natural_language_understanding('test text'))"
```

---

## 🔍 Troubleshooting

### Common Issues

#### 1. **Audio Input Not Working**
- **Solution**: Check microphone permissions in browser
- **Alternative**: Use audio file upload instead

#### 2. **Translation Errors**
- **Problem**: "Translation error" message
- **Solution**: Check internet connection and language codes

#### 3. **Speech Recognition Fails**
- **Problem**: "Could not understand audio"
- **Solutions**:
  - Ensure clear audio quality
  - Check audio file format (WAV, MP3, FLAC supported)
  - Reduce background noise

#### 4. **Module Import Errors**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Or install individually
pip install gradio speech_recognition googletrans==4.0.0rc1
```

#### 5. **Port Already in Use**
```bash
# Change port in app.py
iface.launch(server_port=7861)  # Use different port
```

### Debug Mode

Enable debug mode for detailed error messages:
```python
iface.launch(debug=True)
```

---

## 📊 Performance Notes

### System Requirements
- **RAM**: Minimum 2GB, Recommended 4GB+
- **CPU**: Any modern processor (2+ cores recommended)
- **Storage**: 500MB for dependencies + temporary files
- **Network**: Stable internet connection for translation/TTS

### Optimization Tips
- Use virtual environments to avoid conflicts
- Clear temporary files periodically
- Close unused browser tabs when running
- Consider using Docker for consistent performance

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Types of Contributions
- 🐛 **Bug Reports**: Report issues with detailed descriptions
- 💡 **Feature Requests**: Suggest new functionality
- 📖 **Documentation**: Improve README or add tutorials
- 🔧 **Code**: Submit bug fixes or new features
- 🌍 **Translations**: Help translate the interface

### Contribution Guidelines

1. **Code Style**: Follow PEP 8 guidelines
2. **Documentation**: Update README for new features
3. **Testing**: Test your changes thoroughly
4. **Commit Messages**: Use clear, descriptive commits

### Development Workflow
```bash
# 1. Fork and clone
git clone your-fork-url

# 2. Create feature branch
git checkout -b feature/amazing-feature

# 3. Make changes
# ... code changes ...

# 4. Test changes
python app.py

# 5. Commit and push
git commit -m "Add amazing feature"
git push origin feature/amazing-feature

# 6. Create Pull Request
```

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Advanced Chatbot Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- **[Gradio](https://gradio.app/)** - For the amazing web interface framework
- **[Google Speech Recognition](https://cloud.google.com/speech-to-text)** - For speech recognition services
- **[Google Translate](https://translate.google.com/)** - For translation services
- **[Google Text-to-Speech](https://cloud.google.com/text-to-speech)** - For TTS capabilities
- **[NLTK](https://www.nltk.org/)** - For natural language processing tools
- **Open Source Community** - For continuous inspiration and support

---

## 📞 Support

### Getting Help
- **📖 Documentation**: Check this README first
- **🐛 Issues**: [Create an issue](https://github.com/yourusername/advanced-chatbot/issues)
- **💬 Discussions**: [Join discussions](https://github.com/yourusername/advanced-chatbot/discussions)
- **📧 Contact**: your-email@example.com

### FAQ

**Q: Can I use this without internet?**
A: Speech recognition and translation require internet. Only text processing works offline.

**Q: What audio formats are supported?**
A: WAV, MP3, FLAC, and most common audio formats are supported.

**Q: Can I add my own voice commands?**
A: Yes! Edit the `process_voice_command()` function in `app.py`.

**Q: Is this free to use?**
A: Yes, completely free and open source under MIT license.

---

## 🎯 Roadmap

### Upcoming Features
- [ ] **Offline Mode**: Local speech recognition and translation
- [ ] **Custom Voice Commands**: User-defined command system
- [ ] **Multiple Language Detection**: Automatic language detection
- [ ] **Chat History**: Save and manage conversation history
- [ ] **API Endpoints**: RESTful API for integration
- [ ] **Mobile App**: Native mobile applications
- [ ] **Plugin System**: Extensible plugin architecture

### Version History
- **v1.0.0** - Initial release with core features
- **v1.1.0** - Enhanced UI and error handling (planned)
- **v1.2.0** - Offline capabilities (planned)
- **v2.0.0** - Major feature additions (planned)

---

<div align="center">

**⭐ If you found this project helpful, please give it a star! ⭐**

**Made with ❤️ by the Advanced Chatbot Team**

[🏠 Home](https://github.com/yourusername/advanced-chatbot) • [📚 Docs](https://github.com/yourusername/advanced-chatbot/wiki) • [🐛 Issues](https://github.com/yourusername/advanced-chatbot/issues) • [💬 Discussions](https://github.com/yourusername/advanced-chatbot/discussions)

</div>
