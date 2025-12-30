import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
from playsound import playsound

# Text to Speech  
engine = pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('volume',1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    print("Assistant: ", text)
    engine.say(text)
    engine.runAndWait()

# Speech to Text
r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening....")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return None     
    try:
        text = r.recognize_google(audio)
        print('User: ', text)
        return text.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("API error: ", e)
        return None
    
# Time Function

def tell_time():
    now = datetime.date.today()
    return f"The current time is {now.strftime('%I:%M %p')}"

# Date Function

def tell_date():
    today = datetime.date.today()
    return f"Today is {today.strftime('%A, %B %d, %Y')}"