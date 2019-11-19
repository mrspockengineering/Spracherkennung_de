'''
Created on 17.11.2019
https://www.youtube.com/watch?v=OmqgTZheIQc

@author: Erazer
'''


import speech_recognition as sr     # pip install SpeechRecognition
import os
import re
import webbrowser
import webencodings
import twilio
import six


print("hallo Spracherkennung")

def talkToMe(audio):
    print(audio)
    os.system("say" + audio)
    
def myCommand():
    # hört auf deine Kommandos
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bereit...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command= r.recognize_google(audio, language='de-DE').lower()
        print('Du hast gesagt: '+ command + '\n')
        
    except sr.UnknownValueError:
        print('Dein letztes Kommando konnte nicht verstanden werden.')
        command = myCommand();
    return command

def assistent(command):
    # if statements, um Kommandos auszuführen
    if 'öffne Seite' in command:
        reg_ex = re.search('öffne seite(.*), command')
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Fertig')
    elif 'was geht' in command:
        talkToMe('Bin gerade am chillen')
    elif 'hello' in command:
        talkToMe('hallo')

talkToMe('Ich bin bereit für Befehle')
while True:
    #loopen, um mehrere Befehle auszuführen
    assistent(myCommand())
        
            
            