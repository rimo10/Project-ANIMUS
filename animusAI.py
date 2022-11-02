import datetime
import json
import os
import webbrowser

import pyttsx3
import requests
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print("Recognising...")
            results = r.recognize_google(audio, language='en-in')
            print(f"User said :{results}\n")

        except Exception as e:
            print("Say that again please...")
            speak("Say that again please...")
            return "None"
        return results


if __name__ == '__main__':
    print("Welcome to ANIMUS AI")
    speak("Welcome to ANIMUS AI")
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            print("Here's what i found:")
            print(results)
            speak("According to Wikipedia...")
            speak(results)

        elif 'open youtube' in query:
            print("Opening Youtube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("Opening Google...")
            speak("Opening Google...")
            webbrowser.open("google.com")

        elif 'top 10 news today' in query:
            speak("Top news headlines of the world...Let's begin")
            url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=38dca99b8e6f40f2a6eab2a86110e6b9'
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            k = 1
            for article in arts:
                print(f"News {k}")
                print(article['title'] + ". " + article['description'])
                speak(f"News {k}")
                speak(article['title'])
                speak(article['description'])
                k = k + 1

        elif 'time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is:{strTime}")
            speak(f"The time is{strTime}")

        # elif 'run command prompt' in query:
        #     path = 'C:\\Users\\KIIT\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System ' \
        #            'Tools\\Command Prompt.lnk '
        #     os.startfile(path)

        elif 'exit' in query:
            print("Exiting the ANIMUS AI")
            speak("Exiting the ANIMUS AI")
            break
