import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import operator
import pyautogui

engine = pyttsx3.init()

def say(text):
    print(f"Saarthee: {text}")
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print("Error:", e)
            say("Sorry, I didn't catch that. Please repeat.")
            return ""

if __name__ == '__main__':
    print("Saarthee - Your Desktop Assistant")
    say("Hello, I am Saarthee, your personal desktop assistant.")

    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        say("Good Morning Parth!")
    elif 12 <= hour < 18:
        say("Good Afternoon Parth!")
    else:
        say("Good Evening Parth!")

    while True:
        query = takeCommand().lower()

        if not query:
            continue

        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.org/"],
            ["google", "https://www.google.co.in/"],
            ["linkedin", "https://www.linkedin.com/feed/"]
        ]
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}, Parth...")
                webbrowser.open(site[1])

        if "tell me the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Parth, the time is {strfTime}")

        elif "open calculator" in query:
            say("Opening Calculator, Parth...")
            os.system("calc")

        elif "open notepad" in query:
            say("Opening Notepad, Parth...")
            os.system("notepad")

        elif "open command prompt" in query or "open cmd" in query:
            say("Opening Command Prompt, Parth...")
            os.system("start cmd")

        elif "take screenshot" in query or "screenshot" in query:
            say("Taking a screenshot, Parth...")
            screenshot = pyautogui.screenshot()
            file_name = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screenshot.save(file_name)
            say("Screenshot taken and saved in your current folder.")
            print(f"Screenshot saved as {file_name}")


        elif "exit" in query or "stop" in query or "quit" in query:
            say("Goodbye Parth, have a great day!")
            break
