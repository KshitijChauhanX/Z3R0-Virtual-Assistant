import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5') # sapi5 is Microsoft Speech
voices=engine.getProperty('voices')
# print(voices) prints all the available voices (2 by default) 
# print(voices[0].id) prints first voice
engine.setProperty('voice',voices[0].id) # sets first voice for use

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour) # gives hour which gets typecasted to int
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am ZERO, how may I help you?")

def takeCommand():
    # it takes input from mic and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1    #seconds of non speaking audio before a phase is considered complete
        r.energy_threshold=100
        audio=r.listen(source)
    try:
        print('Recognising...')
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Sorry sir I could not understand you, please say that again")
        return "None"
    return query    

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query, sentences=3)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query: 
            webbrowser.open('youtube.com')
        elif 'open stackoverflow' in query: 
            webbrowser.open('youtube.com')    
        elif 'open google' in query: 
            webbrowser.open('google.com')    
        elif 'play music' in query:
            music_dir='C:\\IDE'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) # Add random later
        elif 'time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {time}') 
        elif 'open code' in query:
            code_path='C:\\IDE\\Microsoft VS Code\\Code.exe'
            os.startfile(code_path)      
        
