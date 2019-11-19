'''
Created on 17.11.2019

speech_recognition -> funktioniert mit headset SilverCrest SKBA -> tests
https://www.youtube.com/watch?v=BWFc9JsSELw

https://www.youtube.com/watch?v=vSzjnUS8u8k

https://realpython.com/python-speech-recognition/#how-speech-recognition-works-an-overview

Funktionen:
- diktiert TExt
- Funktionen 

@author: Erazer
'''

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

def speech_english():
    with sr.Microphone() as source:
        print("Speak into the microphone")
        audio = r.listen(source)
    
    try:
        print("Transcription: " + r.recognize_google(audio, language="de_DE"))      # english: r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Audio unintelligible")
    except sr.RequestError as e:
        print("Cannot obtain results; {0}".format(e))
        
while 1:
#    speech_english()
    erkennung = input("weiteres recog: y/n?")
    if erkennung == 'y':
        speech_english()
    if erkennung == 'n':
        print("ende"); break



'''tests:
this is fantastic and I want to tell you something
today I went home with my dog and I ask you something
today George and Mary went home and made some sex

hallo ich gehe nach Hause und möchte jetzt doch etwas essen
sie können den Computer mithilfe ihrer Stimme diktieren 
beispielsweise können Sie Text diktieren um ein Online Formular
auszufüllen oder diktieren Text in das Textverarbeitungsprogramm 
Word Pad um einen Brief einzugeben

ich gehe jetzt nach Hause, weil ich müde bin. Morgen wird es
wieder schön und hell und vermutlich 30 Grad heiß, weil das 
Wetter sehr warm ist wegen dem Klimawandel.


'''