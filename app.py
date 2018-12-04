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
        # a loop to switch pages
        for F in (StartPage, PageChildren, PageChores, PageBank,
                  PageParents, PageEditBank, PageEditChores, PageAllKids): 
            
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, page): # a function to show the page

        frame = self.frames[page]
        frame.tkraise()
################ functions for database starts here:
        
    def ConnectDataBase(): # just for testing
        conn = sqlite3.connect('AppData.db')
        print("Opened database successfully")
        conn.close()


    def CreateKidsTable(): # create a Kids Table if there is no Kids Table in the database

        conn = sqlite3.connect('AppData.db')
        print("Opened database successfully")
        conn.execute('''CREATE TABLE if not exists Kids
            (number INT, name TEXT, age INT)''')
        print ("Kids Table created successfully or already exists")
        conn.close()

    def InsertNewKid(self,number,name,age):
        # insert a new kid's info into the Kids table in the database
        # One kid has three properties: number, name and age
        # User only need to type name and age, number is only used to keep track of the number of Kids in a family
        # one number slot can only register for one kid, so there won't be two kids both have 1 as number
        conn = sqlite3.connect('AppData.db')
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * from Kids")
            rows = cur.fetchall()
            numList = []
            for row in rows:
                numList.append(row[0])
            if number not in numList:
                Kids_sql = "INSERT INTO Kids (number,name,age) VALUES (?,?,?)"
                cur.execute(Kids_sql,(number, name, age))
                print("Successfully insert "+ name + " into Kids Table")
            else:
                print("There's already a kid registered in this page. You can only update the name. ")
        conn.close()

    def UpdateKid(): # enable a kid to change a name or age
        pass
    
    def DeleteKid(): #enable a kid to delete his/her account
        pass

    def GetKidNameAge(self,num):
        # input is the kid's number, if the number exists then return the name
        # Otherwise return a default message
        conn = sqlite3.connect('AppData.db')
        with conn:
            cur = conn.cursor()
            curname = conn.cursor()
            curage = conn.cursor()
            cur.execute("SELECT * from Kids")
            rows = cur.fetchall()
            numberList = []
            for row in rows:
                numberList.append(row[0])
            if num in numberList:
                curname.execute('SELECT name from Kids WHERE number = '+str(num))
                curage.execute('SELECT age from Kids WHERE number = '+str(num))
                name = curname.fetchone()
                age = curage.fetchone()
                return ([name[0],age[0]])
            else:
                default = ["Please Type your name","Please Type your age"]
                return (default)
         

    def CreateChoreTable(self): # create a Chore Table if there is no Kids Table in the database
        conn = sqlite3.connect('AppData.db')
        conn.execute('''CREATE TABLE if not exists Chore
            (Chore text, time text, status text)''')
        print ("Chore Table created successfully or already exists")
        conn.close()
        
    def InsertNewChore(self):
        pass

    def CreateBankTable(self): # create a Bank Table if there is no Kids Table in the database
        conn = sqlite3.connect('AppData.db')
        conn.execute('''CREATE TABLE if not exists Bank
            (name text, figure text)''')
        print ("Bank Table created successfully or already exists")
        conn.close()
        
################ functions for database STOPs here########################

app.CreateKidsTable() # make sure the database has a Kids table so that the program can run properly 


class StartPage(tk.Frame):  # this is the start page for the app
    
    def __init__(self, parent, controller):

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

    def combine_funcs(a):
        def combined_func(args,kwargs):
            for f in funcs:
                f(args,kwargs)
        return combined_func
        
        
    def changeInfo(labelx,labely,name,age):
        labelx['text'] = "Welcome " + name
        labely['text'] = "Age: " + str(age)
    def getInput(textBox):
        Input = textBox.get()
        return (Input)

    def __init__(self, parent, controller):        
        
        tk.Frame.__init__(self, parent)

        #Logo = tk.PhotoImage(file = "images.gif")

        
        label1 = tk.Label(self, text = "Welcome "+controller.GetKidNameAge(1)[0], font = LARGE_FONT)
        label1.pack(pady = 10, padx = 10)

        nameBox = tk.Entry(self)
        nameBox.pack()

        label2 = tk.Label(self, text = "Age: "+ str(controller.GetKidNameAge(1)[1]), font = LARGE_FONT)
        label2.pack(pady = 10, padx = 10)

        ageBox = tk.Entry(self)
        ageBox.pack()

        RefreshButton = tk.Button(self,text = "refresh",
                                  command = lambda:PageChildren.combine_funcs(
                                      PageChildren.changeInfo((label1,label2,controller.GetKidNameAge(1)[0],controller.GetKidNameAge(1)[1])),
                                      controller.InsertNewKid(1,PageChildren.getInput(nameBox),PageChildren.getInput(ageBox))))
                                  #PageChildren.changeInfo(label1,label2,
                                                                          #controller.GetKidNameAge(1)[0],controller.GetKidNameAge(1)[1]))
        RefreshButton.pack()

        #button1 = tk.Button(self, text = "Click to change your Infor",
        #                    command = lambda:PageChildren.changeInfo(label1,label2,
                                                                     #PageChildren.getInput(nameBox),PageChildren.getInput(ageBox)))
        #button1.pack()

        buttonSql = tk.Button(self, text = "Update Database",
                            command = lambda:controller.InsertNewKid(1,PageChildren.getInput(nameBox),PageChildren.getInput(ageBox)))
        buttonSql.pack()

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
                


