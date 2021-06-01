import tkinter as tk
from tkinter.constants import COMMAND
import pyttsx3

engine = pyttsx3.init()
class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title ("Text-To-Speech Converter")
        self.root.resizable(0,0)
        self.root.configure(background="pink")
        self.label = tk.Label(self.root,bg = "pink",fg="royalblue",font= "Arial 25 bold", text="What do you want me to speak?")
        self.label.pack ()
        self.entry = tk.Entry (self.root, width=30, font= "Arial 20")
        self.entry.pack()
        self.button = tk.Button(self.root,bg = "pink",fg="royalblue",font= "Arial 25 bold", text="Speak",command = self.clicked )
        self.button.pack()
        self.root.mainloop()
    def clicked (self):
        text = self.entry.get()
        self.speak(text)

    def speak (self,text):
        engine.say(text)
        engine.runAndWait()

if __name__ == '__main__':
     temp = Widget()