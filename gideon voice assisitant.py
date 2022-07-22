from datetime import datetime
from email.mime import audio
from http import server
import smtplib
from multiprocessing.spawn import _main
from threading import main_thread
from unittest import result
import os
from pip import main
import pyttsx3
import importlib
im
import wikipedia
import speech_recognition as sr
import webbrowser
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.now().hour)
    if hour>-0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Gideon. How may I help you today,sir")

def sendEmail(to,content):
    server=smtplib.SMTP


def takeCommand():
    #It takes microphone input from user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 0.5 #how much time before it considers the phrase complete\
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("User said:",query)
    except Exception as e:
        #print(e) #would print exception
        print("Say that again please...")
        return("None")
    return query
if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'the time' in query:
            strTime=datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'open steam' in query:
            codePath="C:\\Program Files (x86)\\Steam\\Steam.exe"
            os.startfile(codePath)
        elif 'open chrome' in query:
            codePath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'email to aakash' in query:
            try:
                speak("what should I say?")
                content=takeCommand()
                to="aakashp2000@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry I was not able to send this email")
