import os
import sys
import asyncio

# Function to install required libraries
def install_packages():
    try:
        import speech_recognition
        import pyttsx3
        import googletrans
        import gtts
        import pygame
    except ImportError:
        print("Installing required packages...")
        os.system(f"{sys.executable} -m pip install speechrecognition pyttsx3 googletrans==4.0.0-rc1 gtts pygame pyaudio")
        print("Installation complete. Please restart the script if necessary.")
        sys.exit(0)

# Install missing packages before proceeding
install_packages()

import speech_recognition as sr
import pyttsx3
from googletrans import Translator
from gtts import gTTS
import pygame
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()
translator = Translator()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def record_audio():
    """Record English audio and convert it to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Please say something in English.")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand. Please try again.")
        return None
    except sr.RequestError:
        speak("There was an issue with the speech recognition service.")
        return None

async def translate_to_hindi(text):
    """Translate English text to Hindi"""
    translation = await asyncio.to_thread(translator.translate, text, src="en", dest="hi")
    return translation.text

def text_to_speech_hindi(text):
    """Convert Hindi text to speech and play it"""
    tts = gTTS(text=text, lang="hi")
    tts.save("translated_audio.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("translated_audio.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

    os.remove("translated_audio.mp3")  # Remove file after playing

async def main():
    """Main function to run the speech translation process"""
    text = record_audio()
    if text:
        translated_text = await translate_to_hindi(text)
        print(f"Translated (Hindi): {translated_text}")
        text_to_speech_hindi(translated_text)

if __name__ == "__main__":
    asyncio.run(main())
