from tkinter import *
from tkinter.messagebox import showinfo
import speech_recognition as sr
import os
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)
mainwindow = Tk()
mainwindow.title(' NOTES MAKER')
mainwindow.geometry('500x500')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='LightBlue')
text=''

def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="en-IN")
                file1 = open("myfile.txt", "a", encoding="utf-8")
                file1.writelines("SPEECH TO TEXT")
                file1.write('\n')
                file1.write(text)
                file1.write('\n')
                file1.close()
            except:
                pass
            return text

def text_read():
    global text1
    read_data=text1.get(1.0, "end-1c")
    engine.say(read_data)
    engine.runAndWait()
    print(read_data)
def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Audio-to-Text Converter ')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='pink')

    Label(speechtotextwindow, text='Audio-to-Text Converter by H&H', font=("Comic Sans MS", 15),
          bg='IndianRed').place(x=50)

    text = Text(speechtotextwindow, font=12, height=3, width=30)
    text.place(x=7, y=100)

    recordbutton = Button(speechtotextwindow, text='Record', bg='Sienna',
                          command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=140, y=50)

def texttospeech():
    global text1
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Audio-to-Text Converter ')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='pink')
    import pyttsx3
    Label(speechtotextwindow, text='Text-to-Audio Converter by H&H', font=("Comic Sans MS", 15),
          bg='IndianRed').place(x=50)

    text1 = Text(speechtotextwindow, font=12, height=3, width=30)
    text1.place(x=7, y=100)

    recordbutton = Button(speechtotextwindow, text='Voice', bg='Sienna',
                          command=text_read)
    recordbutton.place(x=140, y=50)

Label(mainwindow, text='Notes maker and Audio maker',
      font=('Times New Roman', 16), bg='red', wrap=True, wraplength=450).place(x=175, y=0)

speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='lightgreen',
                            command=SpeechToText)
speechtotextbutton.place(x=125, y=100)
texttospeech = Button(mainwindow, text='Text-To-Speech Conversion', font=('Times New Roman', 16), bg='lightgreen',
                            command=texttospeech)
texttospeech.place(x=125, y=300)
Label(mainwindow, text='DESIGNED',
      font=('Times New Roman', 16), bg='red', wrap=True, wraplength=450).place(x=200, y=400)
mainwindow.update()
mainwindow.mainloop()
