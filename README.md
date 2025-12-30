**Voice Assistant**

A simple Python-based voice assistant that can tell the time, date, search the web, and open websites using voice commands.

**Author:** Gravity On Mars

**Features**

**Text-to-Speech:** The assistant speaks responses using pyttsx3.

**Speech-to-Text:** Recognizes your voice commands using speech_recognition.

**Time & Date:** Tells the current time and date.

**Web Search:** Searches Google for your queries.

**Open Websites:** Opens specified websites in the default browser.

**Exit Command:** Say "exit" or "quit" to stop the assistant.

**Installation**

**Clone the repository:**

git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant


**Install required dependencies:**

pip install pyttsx3 speechrecognition playsound pyaudio

**Usage**

**Run the assistant:**

python assistant.py


Speak your commands clearly when the assistant says "Listening..."

**Examples of commands:**

"What is the time?"

"What is the date today?"

"Search for Python tutorials"

"Open github.com"

"Quit" or "Exit"

**How It Works**

The assistant uses speech_recognition to listen to your voice.

Converts speech to text using Google Web Speech API.

Parses the command to determine the requested action.

Responds using pyttsx3 text-to-speech engine.

Opens websites or searches Google if requested.

**Dependencies**

Python 3.8+

pyttsx3

speech_recognition

playsound

pyaudio

datetime

webbrowser

os

**Author**

Gravity On Mars
