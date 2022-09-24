from tkinter import *
from PIL import ImageTk , Image
from tkinter import ttk
from googletrans import Translator , LANGUAGES

root = Tk()
root.geometry("1000x1000")
root.title("Translator")
root.config(bg="white")

title_label = Label(root,text="Translator",bg="white")
title_label.place(relx=0.5,rely=0.1,anchor=CENTER)

label1 = Label(root,text="Enter Text")
label1.place(relx=0.2,rely=0.3,anchor=W)
textarea1 = Text(root,width=30,height=10)
textarea1.place(relx=0.1,rely=0.5,anchor=W)
root.mainloop()
