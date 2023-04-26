# (C.A.S.P.E.R) Cognitive Adaptive Speech-enabled Personal Evolving Robot 

import pyttsx3
import speech_recognition as sr
from datetime import *
import time
import customtkinter as ctk
from PIL import Image, ImageTk
import smtplib
from AppOpener import open, close
# modules unused
import wikipedia as wk
import webbrowser as web
import os

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
        self.spkr.setProperty('rate', 180)
        self.lstnr = sr.Recognizer()
        self.mic = sr.Microphone()
        self.hr = datetime.now().hour
        self.mnt = datetime.now().minute

        self.title("C.A.S.P.E.R")  
        self.geometry('800x500')
        self.font='courier new'
        self.iconbitmap('casper/casper.ico')

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
        
        self.imag = ImageTk.PhotoImage(
            Image.open('casper/costume1.png'))
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
            height = 500,
            width = 500,
            text = '',
            justify='left',
            anchor = 'nw',
            font=ctk.CTkFont(size=15, family=self.font))
        self.chat.place(relx=0, anchor='w')
        self.chat.place(x=0, y=0)
        self.chat.pack(padx=10, pady=10)

    # defining actions
    def display(self, msg) :
        txt=self.chat.cget('text') + msg
        self.chat.configure(text=txt)
        self.update()

    def speak(self, msg) :
        txt=''
        msg=msg+'\n'
        for i in msg :
            self.display(i)
            time.sleep(0.01)
        self.spkr.say(msg)
        self.spkr.runAndWait()

    def welcome(self) :
        ctk.set_appearance_mode('light')
        self.wake_button.destroy()
        self.chat.configure(fg_color = 'grey')
        self.update()
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
        self.speak(msg)

    def listen_cmd(self) :
        self.display('Listening...\n')
        while True :
            try :
                with sr.Microphone() as source :
                    self.lstnr.adjust_for_ambient_noise(source, duration=0.2)
                    audio = self.lstnr.listen(source)
                    try :
                        command = self.lstnr.recognize_google(audio)
                    except :
                        continue
                    return command.lower()
            except :
                continue
   
    def start_listening(self) :
        self.display('...')
        while True :
            try :
                with self.mic as source :
                    self.lstnr.adjust_for_ambient_noise(source, duration=0.2)
                    audio = self.lstnr.listen(source)
                    try :
                        command = self.lstnr.recognize_google(audio)
                    except :
                        continue
                    command = command.lower()
                    if self.wakeword in command :
                        self.display(':)')
                        return command
                    if any(i in command.lower() for i in keyword.SLEEP) :
                        self.speak('ok, see ya !')
                        os._exit(0)
            except :
                continue

    def wake(self) :
        self.welcome()
        while True :
            command=self.start_listening()
            self.respond(command)

    def respond(self, command) :
        # send email
        if any(i in command for i in keyword.EMAIL) :
            mail()
        elif any(i in command for i in keyword.APP) :
            app_open_close(command)
        else :
            speak('i have not been trained to answer this, sorry.')

# some keywords for prompts

class keyword() :
    add_dir = {
        'myself' : 'siddharthverma3904@gmail.com',
        'mom' : 'lavitavermapdd@gmail.com',
        'samarth' : '2022csb1118@iitrpr.ac.in',
        'ojas' : '2022csb1099@iitrpr.ac.in'}
    
    app_dir = {
        ('whatsapp', 'whats app', 'what app', 'what\'sapp') : 'WhatsApp',
        ('spotify', 'music', 'song', 'songs') : 'Spotify',
        ('vscode', 'v s code', 'vs code') : 'Visual Studio Code',
        ('my folder', 'master folder', 'sid') : 'sid',
        (' ppt ', 'powerpoint', 'power point') : 'PowerPoint',
        ('canva', 'canve', 'canvas') : 'Canva',
        (' ps ', ' p s ', 'photoshop', 'photo shop') : 'Adobe Photoshop',
        ('youtube', 'utube', 'you tube', ' yt ', ' y t ') : 'YouTube',
        ('google', 'chrome', 'goggle', ' net ', 'new tab', 'browser') : 'Google Chrome',
        ('settings', 'controls', 'setting') : 'Settings'}
    
    SLEEP = ['sleep', 'snooze', 'shut down', 'bye']
    APP_OPEN = ['open', 'play', 'run', 'start']
    APP_CLOSE = ['close', 'kill']
    APP = APP_OPEN + APP_CLOSE
    EMAIL = ['email', 'mail', 'gmail']

# define tasks

# send mail
def mail() :
    CASPER.speak('to whom do you want to send a mail ?')
    reciever = CASPER.listen_cmd()
    for i in keyword.add_book :
        if i in reciever :
            reciever = keyword.add_dir[i]
            CASPER.speak('what do you want to send  ?')
            msg = CASPER.listen_cmd()
            CASPER.display(msg+'\n')
            sender = 'siddharthverma3904@gmail.com'
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(sender, 'mdgxbjotgvgujqem')
            s.sendmail(sender, reciever, msg)
            s.quit()
            CASPER.speak('mail sent !')
            return
    CASPER.display('person not found in address book, sorry.')
    return
    
def app_open_close(command) :
    if any(i in command for i in keyword.APP_OPEN) :
        for j in keyword.app_dir :
            if any(k in command for k in j) :
                try :
                    open(keyword.app_dir[j], match_closest=True)
                    return
                except Exception as e :
                    CASPER.display('an error occured while opening !')
                    print(e)
    else :
        CASPER.display('app not found, sorry.')

# doing actions(mainloop)

if __name__ == "__main__" :
    CASPER = Assistant('CASPER', 'Sid', 'casper')
    CASPER.mainloop()
    os.system('cls')