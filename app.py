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
    with  sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            audio = r.listen(source, 			timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return None
    try:
        text = r.recognize_google(audio)
        print("User: ", text)
        return text.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("API error: ", e)
        return None
   
# Time function


def tell_time():
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}"


# Date Function
def tell_date():
    today = datetime.date.today()
    return f"Today is {today.strftime('%A, %B %d, %Y')}"


# Search Function
def Search(website):
    if not website:
        return "Please specify what to search."
    if"." not in website:
        url = f"https://www.google.com/search?q={website}"
    else:
        url = "https://" + website
    webbrowser.open(url)
    return f"Opened {website}"


# Open Function
def open_website(website):
    if not website:
        return "Which website should I open?"
   
    website = website.lower().replace(" ", "")
   
    if not website.startswith("http"):
        website = "https://" + website


    try:
        webbrowser.open(website)
        return f"Opened {website}"
    except Exception:
        return "Sorry, I couldn't open that website."


# Command Parser
def parse_command(command):
    if not command:
        return "I didn't catch that. Please say again."
    elif 'time' in command:
        return tell_time()
    elif 'date' in command:
        return tell_date()
    elif 'search' in command:
        site = command.replace('search', '').strip()
        return Search(site)
    elif 'open' in command:
        site = command.replace('open', '').strip()
        return open_website(site)
    elif 'exit' in command or 'quit' in command:
        return "exit"
    else:
        return "I can only tell you the time or date. Please ask accordingly."
   


speak("Hello! How can I assist you today?")


while True:
    command = listen()
    result = parse_command(command)


    if result == "exit":
        speak("Goodbye!")
        break
   
    speak(result)



