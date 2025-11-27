#Open ai chatbot
import google.generativeai as genai
import pyttsx3
import speech_recognition as sr

key = "AIzaSyChmitMjN0DL9cOz197bpEw3tbsjnmYFmc"
mic = sr.Recognizer()
with sr.Microphone() as source:
    print("Start speaking...")
    voice = mic.listen(source)
    
    

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")
while True:
    response = mic.recognize_google(voice)
    print(f"Now Opening {response}")

    if response.lower()=="exit":
        print("Bye Bye")
        
        break
    response = model.generate_content(response)
    print("Yuvi :", response.text)




