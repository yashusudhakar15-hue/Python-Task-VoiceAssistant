
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You:", command)
        return command

    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""

    except sr.RequestError:
        speak("Please check your internet connection.")
        return ""

speak("Hello! I am your voice assistant.")

while True:
    command = listen()

    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + current_time)

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + today)

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        break

    else:
        speak("I can tell you the time and date, or open Google and YouTube.")
