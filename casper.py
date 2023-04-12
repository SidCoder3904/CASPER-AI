# (C.A.S.P.E.R) Cognitive Adaptive Speech-enabled Personal Evolving Robot 

import pyttsx3
import speech_recognition as sr
import wikipedia as wk
import webbrowser as web
from datetime import *
import time
import os
import customtkinter as ctk
from PIL import Image, ImageTk

#setting up casper 

bg_mode = 'dark'
ctk.set_appearance_mode(bg_mode)
ctk.set_default_color_theme('green')

class Assistant(ctk.CTk):
    def __init__(self, name, owner, wakeword):
        super().__init__()

        #defining properties

        self.name=name
        self.owner=owner
        self.wakeword=wakeword
        self.spkr = pyttsx3.init('sapi5')
        self.spkr.setProperty('rate', 160)
        self.lstnr = sr.Recognizer()
        self.mic = sr.Microphone()
        self.hr = datetime.now().hour
        self.mnt = datetime.now().minute

        self.title("C.A.S.P.E.R")
        self.geometry('1000x1000')
        self.font='courier new'

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.frame = ctk.CTkFrame(
            master=self,
            corner_radius=10)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.name_display = ctk.CTkLabel(
            master=self.frame,
            text='C.A.S.P.E.R',
            font=ctk.CTkFont(size=50, family=self.font))
        self.name_display.pack(pady=10, padx=10)
        
        self.imag = ImageTk.PhotoImage(Image.open('C:/Users/DELL/Desktop/sid/projects/casper/costume1.png'))
        self.wake_button = ctk.CTkButton(
            master=self.frame,
            image=self.imag,
            text=None,
            font=(self.font, 80),
            fg_color='transparent',
            command=self.wake,
            hover=False)
        self.wake_button.pack()

        self.chat = ctk.CTkLabel(
            master = self.frame,
            corner_radius = 10,
            height = 50,
            width = 500,
            text = None,
            justify='left',
            anchor = 'w',
            font=ctk.CTkFont(size=15, family=self.font))
        self.chat.place(relx=0, anchor='w') # move the text to the left side of frame
        self.chat.place(x=0, y=0)
        self.chat.pack(padx=10, pady=10)

    # defining actions
    def welcome(self) :
        os.system('cls')
        hr=self.hr%12
        if hr==0 :
            hr=12
        mnt=str(self.mnt)
        if(self.mnt<10) :
            mnt = '0'+str(mnt)
        if(self.hr<12 and self.hr>0) :
            msg=f"Good-morning {self.owner}, {self.name} here, it's {str(hr)}:{mnt} AM"
        elif(self.hr>=12 and self.hr<17) :
            msg=f"Good-afternoon {self.owner}, {self.name} here, it's {str(hr)}:{mnt} PM"
        else :
            msg=f"Good-evening {self.owner}, {self.name} here, it's {str(hr)}:{mnt} PM"
        speak(msg)

    def listen_cmd(self) :
        while True :
            os.system('cls')
            print('Listening...')
            try :
                with sr.Microphone() as source :
                    self.lstnr.adjust_for_ambient_noise(source, duration=0.2)
                    audio = self.lstnr.listen(source)
                    try :
                        command = self.lstnr.recognize_google(audio)
                    except :
                        continue
                    os.system('cls')
                    return command
            except :
                continue
        
    def passive(self) :
        ctk.set_appearance_mode('light')
        self.wake_button.destroy()
        self.chat.configure(fg_color = 'grey')
        self.update()
        self.welcome()
        while True :
            os.system('cls')
            print('...')
            try :
                with self.mic as source :
                    self.lstnr.adjust_for_ambient_noise(source, duration=0.2)
                    audio = self.lstnr.listen(source)
                    try :
                        command = self.lstnr.recognize_google(audio)
                    except :
                        continue
                    os.system('cls')
                    if self.wakeword in command.lower() :
                        if 'sleep' in command.lower() :
                            speak('ok, see ya !')
                            os._exit(0)
                        speak("yes sir !")
                        return
            except :
                continue

    def respond(self, command) :
        response = 'i cant answer yet. sorry'
        speak(response)

    def wake(self) :
        while True :
            self.passive()
            command=self.listen_cmd()
            self.respond(command)

def speak(msg) :
    txt=''
    for i in msg :
        txt+=i
        CASPER.chat.configure(text=txt)
        time.sleep(0.01)
        CASPER.update()
    CASPER.spkr.say(msg)
    CASPER.spkr.runAndWait()

#doing actions
if __name__ == "__main__":
    CASPER = Assistant('CASPER', 'Sid', 'casper')
    CASPER.mainloop()
    os.system('cls')