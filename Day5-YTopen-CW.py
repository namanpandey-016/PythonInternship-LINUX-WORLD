#program to open youtube video using voice command
import speech_recognition as sr
import pywhatkit
mic = sr.Recognizer()
with sr.Microphone() as source:
    print("Start speaking...")
    voice = mic.listen(source)
    text = mic.recognize_google(voice)
    print("Now Opening ", text)
    
pywhatkit.playonyt(text)
