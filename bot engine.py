import threading
from tkinter import *
import speech_recognition
import pyttsx3 as ttk


def speak_off():
    global run
    run = False
    if not run:
        off.config(state='disabled')
        print('maszyna wyłączona')

    else:
        pass


def speak_tread():
    threading.Thread(target=speak).start()


def speak():
    global run
    run = True
    engine = ttk.init()
    while run:
        off.config(state='normal')
        recognizer = speech_recognition.Recognizer()
        on.config(state='disabled')
        try:
            with speech_recognition.Microphone() as mic:
                print("Powiedz coś!")
                recognizer.adjust_for_ambient_noise(mic)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio, language="pl-PL")
                text = text.lower()
                print(f'Powiedziałeś: {text}')
                if text == 'cześć':
                    engine.say('Witaj')
                    print(f'maszyna odpowiada: Witaj!')
                    engine.runAndWait()

                else:
                    engine.say('nie wiem co powiedzieć!')
                    engine.runAndWait()
                on.config(state='normal')
                off.config(state='normal')

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            print("Nie wiem co powiedziałeś!")
            on.config(state='normal')
            off.config(state='normal')
            off.after(2000, speak_off())


window = Tk()
window.geometry('200x200')
on = Button(window, text='on', command=speak_tread)
on.pack()
off = Button(window, text='off', command=speak_off, state='disabled')
off.pack()
window.mainloop()
