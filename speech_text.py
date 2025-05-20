import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

def speak_text(command):
    """Convert text to speech."""
    engine.say(command)
    engine.runAndWait()

def recognize_speech():
    """Recognize speech and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio).lower()
            print(f"You said: {text}")
            speak_text(text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

# Main loop
while True:
    user_input = recognize_speech()
    
    if user_input == "exit":
        print("Exiting...")
        speak_text("Goodbye!")
        break  # Exit the loop when the user says "exit"
