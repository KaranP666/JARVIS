import speech_recognition as sr
import webbrowser as web
import bs4
import pyttsx3
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def CoronaVirus(Country):
                countries = str(Country).replace(" ","")

                url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

                result = requests.get(url)

                soups = bs4.BeautifulSoup(result.text,'lxml')

                corona = soups.find_all('div',class_ = 'maincounter-number')

                Data = []

                for case in corona:
                    span = case.find('span')
                    Data.append(span.string)

                cases , Death , recovored = Data

                Speak(f"Cases : {cases}")
                Speak(f"Deaths : {Death}")
                Speak(f"Recovered : {recovored}")