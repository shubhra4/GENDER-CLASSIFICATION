# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 14:29:01 2020

@author: user
"""
from tkinter import *
from tkinter import simpledialog
from tkinter.messagebox import *
from googletrans import Translator

#get funcn gives you value
def getvals():
    sentence=textvalue.get()
    translator=Translator()
    t_sentence=translator.translate(sentence,src='en',dest='ca')
    t_text.insert(0, t_sentence)
    print(t_sentence)
    
root=Tk()

text=Label(root,text="Text to be translated")
t_text=Label(root,text="Translated Text")
t_text.place(x=25, y=25, anchor="center")


#to pack use grid(row,column)
text.grid()
t_text.grid()

#Variable classes in tkinter
#Boolean_Var,Double_Var,IntVar,StringVar 
textvalue=StringVar()

#to input value we use ENTRYWIDGET
textentry=Entry(root,textvariable=textvalue)
t_textentry=Entry(root)
#pack
textentry.grid(row=0,column=1)
t_textentry.grid(row=0,column=2)

Button(text="Submit",command=getvals).grid()

root.mainloop()
