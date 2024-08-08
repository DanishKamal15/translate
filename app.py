import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os

# Initialize the translator
translator = Translator()

# Title of the app
st.title("Language Translator with Voice")

# User input text
input_text = st.text_area("Enter text to translate", "")

# Language selection
languages = {
    "Afrikaans": "af",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-cn",
    "Dutch": "nl",
    "English": "en",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Portuguese": "pt",
    "Russian": "ru",
    "Spanish": "es",
    "Urdu": "ur"
}

language = st.selectbox("Select language to translate to", list(languages.keys()))

# Translate button
if st.button("Translate"):
    if input_text:
        # Perform the translation
        translated = translator.translate(input_text, dest=languages[language])
        st.write(f"Translated text in {language}:")
        st.write(translated.text)
        
        # Convert translated text to speech
        tts = gTTS(translated.text, lang=languages[language])
        tts.save("translated_audio.mp3")
        
        # Play the audio
        audio_file = open("translated_audio.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
        
        # Clean up the temporary audio file
        os.remove("translated_audio.mp3")
    else:
        st.write("Please enter some text to translate.")

# Displaying the translated text
st.write("\n")
