# (C.A.S.P.E.R) Cognitive Adaptive Speech-enabled Personal Evolving Robot 
# FEATURES: 
#   1, open/close apps
#   2, send email 
#   3, date/time/calendar 
#   4, jokes
#   5, enable/disable/change wakeword
#   6, website open

from keys import keyword
import pyttsx3
import speech_recognition as sr
from datetime import date, datetime, time
import calendar
import time
import customtkinter as ctk
from PIL import Image, ImageTk
import smtplib
from AppOpener import open, close
import pyjokes
import webbrowser as web
import os
# modules unused
import wikipedia as wk

#setting up casper 

bg_mode = 'dark'
ctk.set_appearance_mode(bg_mode)
ctk.set_default_color_theme('green')


class Assistant(ctk.CTk):
    def __init__(self, name, owner, wakeword, use_wakeword = True):
        super().__init__()

        #defining properties
        self.name=name
        self.owner=owner
        self.wakeword=wakeword
        self.use_wakeword=use_wakeword
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
        self.frame.pack(pady=20, padx=60, fill="both", expand=False)

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
            text = None,
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
        try :
            self.spkr.say(msg)
            self.spkr.runAndWait()
        except KeyboardInterrupt() as e :
            return

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
                    if self.use_wakeword :
                        if any(i in command for i in self.wakeword) :
                            self.display('\n')
                            if any(i in command.lower() for i in keyword.SLEEP) :
                                self.speak('ok, see ya !')
                                os._exit(0)
                            return command
                    else :
                        self.display('\n')
                        if any(i in command.lower() for i in keyword.SLEEP) :
                            self.speak('ok, see ya !')
                            os._exit(0)
                        return command
            except :
                print('bravo3')
                continue

    def wake(self) :
        self.welcome()
        while True :
            command=self.start_listening()
            self.respond(command)

    def respond(self, command) :
        # send email
        if any(i in command for i in keyword.ww) :#change for change ww
            if any(i in command for i in keyword.change_ww) :
                change_ww()
            else :
                use_ww(command) 
        elif any(i in command for i in keyword.EMAIL) :
            mail(command)
        elif any(i in command for i in keyword.OPEN_CLOSE) :
            for j in keyword.app_dir :
                if any(k in command for k in j) :
                    app_open_close(command) #add web search 
            for j in keyword.website_dir :
                if any(k in command for k in j) :
                    website_open(command)
        elif any(i in command for i in keyword.DTC) :
            date_time(command)
        elif any(i in command for i in keyword.JOKE) :
            joke()
        else :
            self.speak('i have not been trained to answer this, sorry.')

# define tasks

# wakeword usage
def use_ww(command) :
    if any(i in command for i in keyword.disable_ww) :
        CASPER.use_wakeword = False
        CASPER.speak('you can now call me without using a wakeword')
    elif any(i in command for i in keyword.enable_ww) :
        CASPER.wakeword = True
        CASPER.speak(f'you can now call me by calling out \'{(CASPER.wakeword).lower()}\'')
    else :
        CASPER.speak('pardon me, please repeat')
        CASPER.listen_cmd()

# change wakeword
def change_ww() :
    CASPER.speak('what do u want to call me as ?')
    CASPER.display('speak only the wakeword...')
    CASPER.wakeword = (CASPER.listen_cmd()).lower()
    CASPER.use_wakeword = True
    CASPER.speak(f'you can now call me by name: {CASPER.wakeword}')

# send mail
def mail(command) :
    if any(i in command for i in keyword.add_dir) :
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
    else :
        CASPER.speak('to whom do you want to send a mail ?')
        reciever = CASPER.listen_cmd()
        for i in keyword.add_dir :
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
    
def app_open_close(command) :
    if any(i in command for i in keyword.OPEN) :
        for j in keyword.app_dir :
            if any(k in command for k in j) :
                try :
                    open(keyword.app_dir[j], match_closest=True)
                    CASPER.speak(f'opening {keyword.app_dir[j]}')
                    return
                except Exception as e :
                    CASPER.display('an error occured while opening !')
                    print(e)
    if any(i in command for i in keyword.CLOSE) :
        for j in keyword.app_dir :
            if any(k in command for k in j) :
                try :
                    close(keyword.app_dir[j], match_closest=True)
                    CASPER.speak(f'closing {keyword.app_dir[j]}')
                    return
                except Exception as e :
                    CASPER.display('an error occured while closing !')
                    print(e)
    else :
        CASPER.display('app not found, sorry.')

def website_open(command) :
    if any(i in command for i in keyword.OPEN) :
        for j in keyword.website_dir :
            if any(k in command for k in j) :
                try :
                    web.open_new_tab(keyword.website_dir[j])
                    CASPER.speak(f'opening {j[0]}')
                    return
                except Exception as e :
                    CASPER.display('an error occured while opening !')
                    print(e)
    else :
        CASPER.display('unable to open site, sorry.')

def date_time(command) :
    if any(i in command for i in keyword.TIME) :
        hr=CASPER.hr%12
        if hr==0 :
            hr=12
        mnt=str(CASPER.mnt)
        if(CASPER.mnt<10) :
            mnt = '0'+str(mnt)
        if(self.hr<12 and self.hr>0) :
            CASPER.speak(f'its {str(hr)}:{mnt} AM.')
        else :
            CASPER.speak(f'its {str(hr)}:{mnt} PM.')
    elif any(i in command for i in keyword.DATE) :
        today = date.today()
        date = today.strftime('%d %B, %Y, %A')
        CASPER.speak(f'today is {date}')
    elif any(i in command for i in keyword.CALENDER) :
        display(calendar.month(int(today.strftime('%Y')), int(today.strftime('%m'))))
    else :
        display('i cant answer this query, sorry\n')

def joke() :
    joke = pyjokes.get_joke(language="en", category="all")
    CASPER.speak(joke + '\nHa Ha !')

# doing actions(mainloop)

if __name__ == "__main__" :
    CASPER = Assistant('CASPER', 'Sid', keyword.WAKEWORD)
    CASPER.mainloop()
    os.system('cls')