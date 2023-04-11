# Cognitive Adaptive Speech-enabled Personal Evolving Robot (C.A.S.P.E.R)

import pyttsx3
import speech_recognition as sr
import wikipedia as wk
import webbrowser as web
from datetime import *
import time
import os

# declaring casper

class Assistant():
    def __init__(self, name, owner, wakeword):
        super().__init__()
        self.name=name
        self.owner=owner
        self.wakeword=wakeword
        self.spkr = pyttsx3.init('sapi5')
        self.spkr.setProperty('rate', 160)
        self.lstnr = sr.Recognizer()
        self.mic = sr.Microphone()
        self.hr = datetime.now().hour
        self.mnt = datetime.now().minute

CASPER = Assistant('CASPER', 'Sid', 'casper')

#defining actions

def wish() :
        hr=CASPER.hr%12
        if hr==0 :
            hr=12
        mnt=CASPER.mnt
        if(CASPER.hr<12 and CASPER.hr>0) :
            msg=f"Good-morning {CASPER.owner}, {CASPER.name} here, it's {str(hr)}:{str(mnt)} AM"
        elif(CASPER.hr>=12 and CASPER.hr<17) :
            msg=f"Good-afternoon {CASPER.owner}, {CASPER.name} here, it's {str(hr)}:{str(mnt)} PM"
        else :
            msg=f"Good-evening {CASPER.owner}, {CASPER.name} here, it's {str(hr)}:{str(mnt)} PM"
        speak(msg)

def speak(msg) :
    for i in msg :
        print(i, end='')
        time.sleep(0.005)
    print('\n')
    CASPER.spkr.say(msg)
    CASPER.spkr.runAndWait()


def wake() :
    while True :
        os.system('cls')
        print('Listening...')
        try :
            with CASPER.mic as source :
                CASPER.lstnr.adjust_for_ambient_noise(source, duration=0.2)
                audio = CASPER.lstnr.listen(source)
                try :
                    command = CASPER.lstnr.recognize_google(audio)
                except :
                    continue
                os.system('cls')
                if CASPER.wakeword in command.lower() :
                    if 'sleep' in command.lower() :
                        speak('ok, see ya !')
                        os._exit(0)
                    wish()
                    return
        except :
            continue
        
def wake2() :
    while True :
        os.system('cls')
        print('...')
        try :
            with CASPER.mic as source :
                CASPER.lstnr.adjust_for_ambient_noise(source, duration=0.2)
                audio = CASPER.lstnr.listen(source)
                try :
                    command = CASPER.lstnr.recognize_google(audio)
                except :
                    continue
                os.system('cls')
                if CASPER.wakeword in command.lower() :
                    if 'sleep' in command.lower() :
                        speak('ok, see ya !')
                        os._exit(0)
                    return
        except :
            continue

def listen_cmd() :
    while True :
        os.system('cls')
        print('Listening...')
        try :
            with sr.Microphone() as source :
                CASPER.lstnr.adjust_for_ambient_noise(source, duration=0.2)
                audio = CASPER.lstnr.listen(source)
                try :
                    command = CASPER.lstnr.recognize_google(audio)
                except :
                    continue
                os.system('cls')
                return command
        except :
            continue

def respond(command) :
    response = 'i cant answer yet. sorry'
    speak(response)

wake()
while True :
    wake2()
    command = listen_cmd()
    respond(command)
