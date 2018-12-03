#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 8:26:05 2018

@author: Han
"""

import tkinter as tk
from tkinter import ttk #make button fancy
import sqlite3

LARGE_FONT = ("Verdana", 12) # set up a front for future use


class app(tk.Tk): 
    
    def __init__(self,*args, **kwargs):
        
        tk.Tk.__init__(self,*args, **kwargs)

        tk.Tk.wm_title(self, "Child-Computer Interaction Project")
        
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}
        # loop to switch pages
        for F in (StartPage, PageChildren, PageChores, PageBank,
                  PageParents, PageEditBank, PageEditChores, PageAllKids): 
            
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, page): # function to show the page "page"

        frame = self.frames[page]
        frame.tkraise()

    def ConnectDataBase(self): # function to connect the app database
        #conn = sqlite3.connect('/Users/Han/Documents/CS 4980 Child-Computer Interaction(2018 FALL)/Child_Computer_Interaction_Project/AppData.db')
        conn = sqlite3.connect('AppData.db')
        print("Opened database successfully")

        conn.close()

    def CreateKidsTable(self):
        #conn = sqlite3.connect('/Users/Han/Documents/CS 4980 Child-Computer Interaction(2018 FALL)/Child_Computer_Interaction_Project/AppData.db')
        conn = sqlite3.connect('AppData.db')
        conn.execute('''CREATE TABLE if not exists Kids
            (name text)''')
        print ("Kids Table created successfully")
        conn.close()

    def CreateChoreTable(self):
        #conn = sqlite3.connect('/Users/Han/Documents/CS 4980 Child-Computer Interaction(2018 FALL)/Child_Computer_Interaction_Project/AppData.db')
        conn = sqlite3.connect('AppData.db')
        conn.execute('''CREATE TABLE if not exists Chore
            (Chore text, time text, status text)''')
        print ("Chore Table created successfully")
        conn.close()


class StartPage(tk.Frame):  # this is the start page for the app
    
    
    
    def __init__(self, parent, controller):

        controller.ConnectDataBase()

        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text = "Home", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = ttk.Button(self, text = "Children", 
                            command = lambda: controller.show_frame(PageAllKids))
        button1.pack(pady = 50, padx = 10)
        
        button2 = ttk.Button(self, text = "Parents",
                            command = lambda: controller.show_frame(PageParents))
        button2.pack(pady = 50, padx = 10)


class PageAllKids(tk.Frame): # Kids select their own page (for multiple children family use)

    def __init__(self, parent, controller):

        controller.CreateKidsTable()
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Find your page", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Kid 1",
                            command = lambda: controller.show_frame(PageChildren))
        button1.pack()

        button2 = tk.Button(self, text = "Kid 2",
                            command = lambda: controller.show_frame(PageChildren))
        button2.pack()

        button3 = tk.Button(self, text = "Kid 3",
                            command = lambda: controller.show_frame(PageChildren))
        button3.pack()

        button4 = tk.Button(self, text = "Home",
                            command = lambda: controller.show_frame(StartPage))
        button4.pack()

class PageChildren(tk.Frame): # Children main page
    def changeName(label,name):
        label['text'] = "Welcome " + name
        
    def getName(textBox):
        name = textBox.get()
        return (name)

    def __init__(self, parent, controller):
        
        
        tk.Frame.__init__(self, parent)

        #Logo = tk.PhotoImage(file = "images.gif")
        
        label = tk.Label(self, text = "Please Type your name", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        nameBox = tk.Entry(self)
        nameBox.pack()
        
        button1 = tk.Button(self, text = "Change Name",
                            command = lambda:PageChildren.changeName(label,PageChildren.getName(nameBox)))
        button1.pack()

        button2 = tk.Button(self, text = "Chores",
                            command = lambda: controller.show_frame(PageChores))
        #button1.grid(row = 3, column = 3)
        button2.pack()

        button3 = tk.Button(self, text = "Bank",
                            command = lambda: controller.show_frame(PageBank))
        button3.pack()

        button4 = tk.Button(self, text = "Back",
                            command = lambda: controller.show_frame(PageAllKids))
        button4.pack()

        button5 = tk.Button(self, text = "Home",
                            command = lambda: controller.show_frame(StartPage))
        button5.pack()


class PageChores(tk.Frame): # Children chore page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Chores", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Home",
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

class PageBank(tk.Frame): # Children bank page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Bank", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Home",
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

#####################################################
# Parent's pages starts from here. Not finished here, but I do have a prototype in Adobe XD       
class PageParents(tk.Frame): # Parents main page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Welcome ! xxx's Parents", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Edit Chores",
                            command = lambda: controller.show_frame(PageEditChores))
        button1.pack()
        
        button2 = tk.Button(self, text = "Edit Bank",
                            command = lambda: controller.show_frame(PageEditBank))
        button2.pack()
        
        button3 = tk.Button(self, text = "Back to home",
                            command = lambda: controller.show_frame(StartPage))
        button3.pack()

class PageEditBank(tk.Frame): # Parents edit bank page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Edit Bank", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Home",
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

class PageEditChores(tk.Frame): # Parents edit Chore page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Edit Chore", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Home",
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

main = app()
main.geometry("400x300")
main.mainloop()
                


