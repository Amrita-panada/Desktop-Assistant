import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


# Taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id) 

engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150) #normal speed of speaking

#speak funtion

def speak(text):
    """This funtion takes text and returns voice
    args:
        text (_type_):string
    """
    engine.say(text)
    engine.runAndWait()

#speak("Hellow minakshi how are you")

#speech recognijation funtion
def taskCommand():
    """this funtion will recognize voice & return text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"User Said:{query}\n")
        except Exception as e:
            print("say that again please...")
            return "None"
        return query


#The function for wish me by using time
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir. How are you doing")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon sir. How are you doing")

    else:
        speak("Good evening sir. How are you doing")
    
    speak("I am JARVIS. Tell me sir how can i help you")

    
'''text=taskCommand()
speak(text)'''



if __name__ == '__main__':
    wish_me()

    while True:

        query=taskCommand().lower()
        

        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace('wikipedia',"")
            result=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "youtube" in query:
            speak("opening youTube")
            webbrowser.open("youtube.com") #you can open any site 
        
        elif "github" in query:
            speak("opening github")
            webbrowser.open("github.com")
        
        elif "time" in query:
            strTime = datetime.datetime.now().strtime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'ok bye' in query:
            speak("ok amrita. I am always here to help you.bye bye")
            exit()


