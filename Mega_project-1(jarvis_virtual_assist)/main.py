import speech_recognition as sr
import webbrowser
import pyttsx3
import music_lib
from openai import OpenAI
import requests
from gtts import gTTS
import pygame
import os

recogizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="3cd82fc5b20847788a031f8b32562f94"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    tts=gTTS('text')
    tts.save('temp.mp3')
    
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove('temp.mp3')
    
def aiProcess(command):
    
    client=OpenAI(    
        api_key="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"
)
    stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"system","content":"you are a virtual assistant named jarvis skilled in gereral tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}],
    stream=True,
)
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")       
def processCommand(c):
    if "open google"in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube"in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open facebook "in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=music_lib.music[song]
        webbrowser.open(link)
        
        
    elif "news"in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code==200:
            data=r.json()
            articles=data.get('articles',[])
            for article in articles:
                speak(article['title'])
            
    else:
        #let openAi handle the request
        output=aiProcess(c)
        speak(output)
    
    
if __name__=="__main__":
    speak("Initializing jarvis....")    
    
    # listen for the wake word "jarvis"
    while True:
        r=sr.Recognizer()
           
        print("Recognizing....")   
        try:
            with sr.Microphone()as source:
                 print("Listening...!")
                 audio=r.listen(source,timeout=2,phrase_time_limit=1)
    
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")
                #Listen for command 
                with sr.Microphone()as source:
                 print("jarvis active...!")
                 audio=r.listen(source)
                 command=r.recognize_google(audio)    
                 
                 processCommand(command)
                
                           
        except Exception as e:
            print("Error;{0}".format(e))
        
        
        
        
# last play 9.59.43