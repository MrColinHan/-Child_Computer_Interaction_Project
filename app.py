#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 00:26:05 2018

@author: Han
"""

from tkinter import * #Tk, Label, Button


window = Tk()
window.geometry('500x500')
 
window.title("Child & Computer Interaction Project")

label1 = Label(window, text="HOME")
label1.pack()
#lbl.grid(anchor = "center")


button1 = Button(window, text="Children")
button1.pack()
def clicked():
    button1.configure(text="Button was clicked !!")
#button1.grid(column=0, row=1)

window.mainloop()
