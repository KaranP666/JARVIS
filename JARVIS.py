import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import bs4
import smtplib
import random

from feature import TakeCommand


engine = pyttsx3.init('sapi5') #it provides api to take voices
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir , Plese Tell me how may I help you")


def tekeCommand():
    #it takes microphone input from the user and returns String output
    r = sr.Recognizer() #Recognizer class helps to recognize Audio
    with sr.Microphone() as source:
        print("Listening...")
        r.phrase_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that agin please...")
        return "None"    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('gamerbuddy229@gmail.com', 'teyplqwcphsbzlix')
    server.sendmail('gamerbuddy229@gmail.com',to,content)
    server.close()    

if __name__ == "__main__":
    wishMe()
    while True:
        query = tekeCommand().lower()
        #logic for executing task based on Query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("Acconding to Wikipedia")
            print(results)
            speak(results)

        # elif 'STOP!' in query:
        #     speak("Thanks for interacting with me, I am sure krishna ma'am will give you 10 out of 10!")
        #     engine.exit()
        #     break

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open geeks for geeks' in query:
            webbrowser.open("https://www.geeksforgeeks.org/")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\abc\\Desktop\\JARVIS\\Music'
            songs = os.listdir(music_dir) #listdir will list all the files of music_dir
            print(songs)
            os.startfile(os.path.join(music_dir , random.choice(songs)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'open Chrome' in query:
            pathc = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(pathc)

        elif 'what can you do' in query:
            speak('Sir I can do many things! Like opening web browsers like google, YouTube, I can also search anything in Wikipedia! I can even play music,and if you wanna know know covid cases then just ask!')

#for covid cases
        
        elif 'covid cases' in query:
            from feature import CoronaVirus
            
            speak("which country's information ?")
            kk = TakeCommand()
            CoronaVirus(kk)
                
        elif 'email to karan' in query:
            try:
                speak("What should i say?")
                content =  tekeCommand()
                to = "karan.h.panchal786@gmail.com"
                sendEmail(to, content);
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email")