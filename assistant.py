import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print("You said:", command)
    except:
        return "none"

    return command.lower()

speak("Hello Aman, I am your voice assistant")

while True:
    command = take_command()

    if command == "none":
        continue

    if 'hello' in command:
        speak("Hello Aman")

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak("The time is " + time)

    elif 'date' in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    elif 'wikipedia' in command:
        speak("Searching Wikipedia")
        command = command.replace("wikipedia", "")
        result = wikipedia.summary(command, sentences=2)
        speak(result)

    elif 'search' in command:
        speak("What should I search?")
        query = take_command()
        if query != "none":
            webbrowser.open("https://www.google.com/search?q=" + query)

    elif 'exit' in command or 'stop' in command:
        speak("Goodbye Aman")
        break