#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:26:05 2018

@author: Han
"""

#from tkinter import * #Tk, Label, Button
import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

class app(tk.Tk):
    
    def __init__(self,*args, **kwargs):
        
        tk.Tk.__init__(self,*args, **kwargs)

        tk.Tk.wm_title(self, "Child-Computer Interaction Project")
        
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo): # loop to switch pages
            
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont): 

        frame = self.frames[cont]
        frame.tkraise()

#def print_(xxx):
#    print(xxx)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = "Start Page", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = ttk.Button(self, text = "Visit Page 1",
                            command = lambda: controller.show_frame(PageOne))#print_("heiheihei")
        button1.pack()

        button2 = ttk.Button(self, text = "Visit Page 2",
                            command = lambda: controller.show_frame(PageTwo))#print_("heiheihei")
        button2.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Page One!", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Back to home",
                            command = lambda: controller.show_frame(StartPage))#print_("heiheihei")
        button1.pack()

        button2 = tk.Button(self, text = "go to PageTwo",
                            command = lambda: controller.show_frame(PageTwo))#print_("heiheihei")
        button2.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Page Two!!", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Back to home",
                            command = lambda: controller.show_frame(StartPage))#print_("heiheihei")
        button1.pack()

        button2 = tk.Button(self, text = "go to page one",
                            command = lambda: controller.show_frame(PageOne))#print_("heiheihei")
        button2.pack()

main = app()
main.geometry("1280x720")
main.mainloop()
                


