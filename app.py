import speech_recognition as sr
from googletrans import Translator
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gtts import gTTS
import gradio as gr
import tempfile
import os

# Download required NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

# Initialize global objects
recognizer = sr.Recognizer()
translator = Translator()

def natural_language_understanding(text):
    """
    Process text using NLP techniques: tokenization, stopword removal, and lemmatization.
    
    Args:
        text (str): Input text to process
        
    Returns:
        str: Processed text with stopwords removed and words lemmatized
    """
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    processed_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words and token.isalpha()]
    return " ".join(processed_tokens)

def translate_text(text, target_language):
    """
    Translate text to target language using Google Translate.
    
    Args:
        text (str): Text to translate
        target_language (str): Target language code (e.g., 'es', 'fr', 'de')
        
    Returns:
        str: Translated text
    """
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Translation error: {str(e)}"

def text_to_speech(text, language='en'):
    """
    Convert text to speech and save as temporary audio file.
    
    Args:
        text (str): Text to convert to speech
        language (str): Language code for TTS
        
    Returns:
        str: Path to temporary audio file
    """
    try:
        tts = gTTS(text=text, lang=language, slow=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            return fp.name
    except Exception as e:
        print(f"TTS error: {str(e)}")
        return None

def process_voice_command(text):
    """
    Process voice commands (placeholder for future implementation).
    
    Args:
        text (str): Processed voice command text
        
    Returns:
        str: Response to voice command
    """
    # Basic command processing - can be extended
    text_lower = text.lower()
    
    if 'hello' in text_lower or 'hi' in text_lower:
        return "Hello! How can I help you today?"
    elif 'time' in text_lower:
        from datetime import datetime
        return f"Current time is {datetime.now().strftime('%H:%M:%S')}"
    elif 'date' in text_lower:
        from datetime import datetime
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"
    elif 'weather' in text_lower:
        return "I don't have access to weather data yet, but you can check your local weather service."
    else:
        return f"Voice command processed: '{text}'. Advanced command processing coming soon!"

def process_input(input_text, input_audio, feature, target_language, output_language):
    """
    Main processing function that handles all input types and features.
    
    Args:
        input_text (str): Text input from user
        input_audio (str): Path to audio file
        feature (str): Selected feature ('Translation', 'Voice Command', 'Transcription')
        target_language (str): Target language for translation
        output_language (str): Output language for final result
        
    Returns:
        tuple: (result_text, audio_file_path)
    """
    # Handle audio input first
    if input_audio is not None:
        try:
            with sr.AudioFile(input_audio) as source:
                # Adjust for ambient noise
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.record(source)
            input_text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Could not understand the audio. Please try speaking more clearly.", None
        except sr.RequestError as e:
            return f"Could not request results from speech recognition service: {str(e)}", None
        except Exception as e:
            return f"An error occurred during speech recognition: {str(e)}", None
    
    # Validate input
    if not input_text or input_text.strip() == "":
        return "No input provided. Please enter text or upload an audio file.", None
    
    # Process text with NLP
    processed_text = natural_language_understanding(input_text)
    
    # Execute selected feature
    if feature == "Translation":
        if not target_language or target_language.strip() == "":
            return "Please specify a target language for translation (e.g., 'es' for Spanish, 'fr' for French).", None
        result = translate_text(input_text, target_language.strip())
    elif feature == "Voice Command":
        result = process_voice_command(processed_text)
    elif feature == "Transcription":
        result = f"Original: {input_text}\nProcessed: {processed_text}"
    else:
        result = "Please select a valid feature (Translation, Voice Command, or Transcription)."
    
    # Apply output language translation if specified
    if output_language and output_language.strip() != "" and feature != "Translation":
        result = translate_text(result, output_language.strip())
    
    return result, None

def tts_function(text, language_code="en"):
    """
    Convert result text to speech.
    
    Args:
        text (str): Text to convert to speech
        language_code (str): Language code for TTS
        
    Returns:
        str: Path to audio file or None if error
    """
    if text and text.strip():
        return text_to_speech(text, language_code)
    return None

# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft(), title="Advanced Multi-Faceted Chatbot") as iface:
    gr.Markdown("""
    # 🤖 Advanced Multi-Faceted Chatbot
    
    **Welcome to your intelligent language processing assistant!**
    
    This chatbot offers multiple features:
    - 🗣️ **Speech Recognition**: Upload audio and convert it to text
    - 🌍 **Translation**: Translate text between different languages
    - 🎤 **Voice Commands**: Process simple voice commands
    - 📝 **Transcription**: Clean and process text using NLP techniques
    - 🔊 **Text-to-Speech**: Convert results back to audio
    
    ### How to use:
    1. Enter text directly OR upload an audio file
    2. Select your desired feature
    3. For translation, specify target language codes (e.g., 'es', 'fr', 'de', 'hi', 'zh')
    4. Click "Process" to get results
    5. Use "Convert to Speech" to hear the output
    """)
    
    with gr.Row():
        with gr.Column(scale=2):
            input_text = gr.Textbox(
                label="💬 Input Text",
                placeholder="Type your message here...",
                lines=3
            )
        with gr.Column(scale=1):
            input_audio = gr.Audio(
                label="🎤 Input Audio",
                type="filepath",
                sources=["microphone", "upload"]
            )
    
    with gr.Row():
        feature = gr.Radio(
            choices=["Translation", "Voice Command", "Transcription"],
            label="🔧 Select Feature",
            value="Translation"
        )
        with gr.Column():
            target_language = gr.Textbox(
                label="🌍 Target Language Code",
                placeholder="e.g., es, fr, de, hi, zh, ja",
                info="For Translation feature only"
            )
            output_language = gr.Textbox(
                label="🗣️ Output Language Code",
                placeholder="e.g., en, es, fr (optional)",
                info="Final output language (optional)"
            )
    
    with gr.Row():
        submit_button = gr.Button("🚀 Process", variant="primary", size="lg")
        clear_button = gr.Button("🗑️ Clear", variant="secondary")
    
    result_text = gr.Textbox(
        label="✨ Result",
        lines=4,
        max_lines=8,
        show_copy_button=True
    )
    
    with gr.Row():
        tts_button = gr.Button("🔊 Convert to Speech", variant="secondary")
        audio_output = gr.Audio(label="🎵 Audio Output")
    
    # Event handlers
    submit_button.click(
        process_input,
        inputs=[input_text, input_audio, feature, target_language, output_language],
        outputs=[result_text, audio_output]
    )
    
    tts_button.click(
        tts_function,
        inputs=[result_text],
        outputs=[audio_output]
    )
    
    clear_button.click(
        lambda: ("", None, "", "", "", None),
        outputs=[input_text, input_audio, target_language, output_language, result_text, audio_output]
    )
    
    # Add examples
    gr.Examples(
        examples=[
            ["Hello, how are you today?", None, "Translation", "es", ""],
            ["What time is it?", None, "Voice Command", "", ""],
            ["The quick brown fox jumps over the lazy dog.", None, "Transcription", "", ""],
        ],
        inputs=[input_text, input_audio, feature, target_language, output_language]
    )
    
    gr.Markdown("""
    ### Language Codes Reference:
    - **English**: en
    - **Spanish**: es
    - **French**: fr
    - **German**: de
    - **Hindi**: hi
    - **Chinese**: zh
    - **Japanese**: ja
    - **Portuguese**: pt
    - **Russian**: ru
    - **Arabic**: ar
    
    ### 🔧 Troubleshooting:
    - Ensure your microphone is working for audio input
    - Use clear audio files for better speech recognition
    - Check language codes for translation features
    - Internet connection required for translation and TTS services
    """)

# Launch the application
if __name__ == "__main__":
    iface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        debug=True
    )
