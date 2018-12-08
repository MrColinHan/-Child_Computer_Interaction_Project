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
                  PageParents, PageEditBank, PageEditChores, PageAllKids,PageChildren2,AddChores): 
            
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
        # if there's already a kid, clicking the same button will update name and age as long as name and age are not null
        conn = sqlite3.connect('AppData.db')
        strN = str(name)
        strA = str(age)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * from Kids")
            rows = cur.fetchall()
            numList = []
            for row in rows:
                numList.append(row[0])
            if (number not in numList) and (len(name) != 0) and (len(age) != 0):
                Kids_sql = "INSERT INTO Kids (number,name,age) VALUES (?,?,?)"
                cur.execute(Kids_sql,(number, name, age))
                print("Successfully insert "+ name + " into Kids Table")
            if (number in numList) and (len(name) != 0):
                update_name = "UPDATE Kids SET name = ? WHERE number = ?" 
                cur.execute(update_name,(strN,number))
                
                print("Successfully update name to " + name)
            if (number in numList) and (len(age) != 0):
                update_age = "UPDATE Kids SET age = ? WHERE number = ?"
                cur.execute(update_age,(strA,number))
                print("Successfully update age to " + age)
            else:
                print("There's nothing to update")
                
                #print("There's already a kid registered in this page. You can only update the name. ")
        conn.close()
    
    def DeleteKid(): #enable a kid to delete his/her account
        pass

    def GetKidNameAge(self,num,message):
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
                if message == 1:
                    default = ["Please Type your name","Please Type your age"]
                else:
                    default = ["Click to register"]
                return (default)

        
    def CreateChoreTable(): # create a Chore Table if there is no Kids Table in the database
        conn = sqlite3.connect('AppData.db')
        conn.execute('''CREATE TABLE if not exists Chore
            (number text,name text, times text, date text, status text)''')
        print ("Chore Table created successfully or already exists")
        conn.close()
        
    def InsertNewChore(self,num,name,time,date,status):
        
        conn = sqlite3.connect('AppData.db')
        with conn:
            cur = conn.cursor()
            Chore_sql = "INSERT INTO Chore (number,name,times,date,status) VALUES (?,?,?,?,?)"
            cur.execute(Chore_sql,(num, name, time,date,status))
            print("Successfully insert "+ name +" at "+ date + " into Chore Table")
            

    def getChoreInfo(self, num):
        
        conn = sqlite3.connect('AppData.db')
        with conn:
            cur = conn.cursor()
            curtimes = conn.cursor()
            curdate = conn.cursor()
            curstatus = conn.cursor()
            cur.execute("SELECT number FROM Chore")
            rows = cur.fetchall()
            numberList = []
            for row in rows:
                numberList.append(row[0])
            if num in numberList:

                curtimes.execute('SELECT times from Chore WHERE number = ?',(num))
                curdate.execute('SELECT date from Chore WHERE number = ?',(num))
                curstatus.execute('SELECT status from Chore WHERE number = ?',(num))
                '''
                times = curtimes.fetchall()
                timesList = []
                for i in times:
                    timesList.append(i)
                    
                date = curdate.fetchall()
                dateList = []
                for j in times:
                    dateList.append(i)
                    
                status = curstatus.fetchall()
                statusList = []
                for k in times:
                    statusList.append(i)

                result = []
                result.append(str(len(timesList)))
                for m in range(len(timesList)):
                    result.append(str(str(dateList[m])+str(statusList[m])))
                '''
                times = curtimes.fetchall()
                date = curdate.fetchall()
                status = curstatus.fetchall()
                result = ["Awesome! You've accomplished "+str(len(date)) +" times.",str(date[0][0]),status[0][0]] #need to change this part to show all the data,
                                                                                                       #need a loop before here (a loop for each fetchall)
                
                return (result)
            else:
                default = ["You don't have any record for this activity. You can start now!","0","0"]
                return (default)
                







    def CreateBankTable(self): # create a Bank Table if there is no Kids Table in the database
        conn = sqlite3.connect('AppData.db')
        conn.execute('''CREATE TABLE if not exists Bank
            (name text, figure text)''')
        print ("Bank Table created successfully or already exists")
        conn.close()
        
################ functions for database STOPs here########################

app.CreateKidsTable() # make sure the database has a Kids table so that the program can run properly 
app.CreateChoreTable() # make sure the database has a Chore table so that the program can run properly 

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

        button1 = tk.Button(self, text = controller.GetKidNameAge(1,0)[0],
                            command = lambda: controller.show_frame(PageChildren))
        button1.pack()

        button2 = tk.Button(self, text = controller.GetKidNameAge(2,0)[0],
                            command = lambda: controller.show_frame(PageChildren2))
        button2.pack()

        button3 = tk.Button(self, text = controller.GetKidNameAge(3,0)[0],
                            command = lambda: controller.show_frame(PageChildren))
        button3.pack()

        button4 = tk.Button(self, text = "Home",
                            command = lambda: controller.show_frame(StartPage))
        button4.pack()


class PageChildren(tk.Frame): # Kid 1's  main page

    '''def combine_funcs(a):
        def combined_func(args,kwargs):
            for f in funcs:
                f(args,kwargs)
        return combined_func''' # need to fix combine funcs
        
        
    def changeInfo(labelx,labely,name,age):
        labelx['text'] = "Welcome " + name
        labely['text'] = "Age: " + str(age)
    def getInput(textBox):
        Input = textBox.get()
        return (Input)

    def __init__(self, parent, controller):        
        
        tk.Frame.__init__(self, parent)

        #Logo = tk.PhotoImage(file = "images.gif")

        
        label1 = tk.Label(self, text = "Welcome "+ controller.GetKidNameAge(1,1)[0], font = LARGE_FONT)
        label1.pack(pady = 10, padx = 10)


        nameBox = tk.Entry(self)
        nameBox.pack()


        label2 = tk.Label(self, text = "Your Age: "+ str(controller.GetKidNameAge(1,1)[1]), font = LARGE_FONT)
        label2.pack(pady = 10, padx = 10)


        ageBox = tk.Entry(self)
        ageBox.pack()


        buttonSql = tk.Button(self, text = "Click here First!",#"Update Database",
                            command = lambda:controller.InsertNewKid(1,PageChildren.getInput(nameBox),PageChildren.getInput(ageBox)))
        buttonSql.pack()


        RefreshButton = tk.Button(self,text = "Then click here",#"refresh current page",
                                  command = lambda:PageChildren.changeInfo(label1,label2,
                                                                           controller.GetKidNameAge(1,1)[0],controller.GetKidNameAge(1,1)[1]))
        RefreshButton.pack()


        button2 = tk.Button(self, text = "Chores",
                            command = lambda: controller.show_frame(PageChores))
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

class PageChildren2(tk.Frame): # Kid 2's  main page
        
        
    def changeInfo(labelx,labely,name,age):
        labelx['text'] = "Welcome " + name
        labely['text'] = "Age: " + str(age)
    def getInput(textBox):
        Input = textBox.get()
        return (Input)

    def __init__(self, parent, controller):        
        
        tk.Frame.__init__(self, parent)
        
        label1 = tk.Label(self, text = "Welcome "+ controller.GetKidNameAge(2,1)[0], font = LARGE_FONT)
        label1.pack(pady = 10, padx = 10)


        nameBox = tk.Entry(self)
        nameBox.pack()


        label2 = tk.Label(self, text = "Your Age: "+ str(controller.GetKidNameAge(2,1)[1]), font = LARGE_FONT)
        label2.pack(pady = 10, padx = 10)


        ageBox = tk.Entry(self)
        ageBox.pack()


        buttonSql = tk.Button(self, text = "Click here First!",#"Update Database",
                            command = lambda:controller.InsertNewKid(2,PageChildren2.getInput(nameBox),PageChildren2.getInput(ageBox)))
        buttonSql.pack()


        RefreshButton = tk.Button(self,text = "Then click here",#"refresh current page",
                                  command = lambda:PageChildren2.changeInfo(label1,label2,
                                                                           controller.GetKidNameAge(2,1)[0],controller.GetKidNameAge(2,1)[1]))
        RefreshButton.pack()


        button2 = tk.Button(self, text = "Chores",
                            command = lambda: controller.show_frame(PageChores))
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

    def changeInfo(labelx,labely,labelz,labelw,x,y,z,w):
        labelx['text'] = "Sleep on time: "+ x
        labely['text'] = "Details: "+ "date: "+ y
        labelz['text'] = "Drink a lot of water: "+ z
        labelw['text'] = "Details: "+ "date: "+ w 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Chores Status", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
    
        Chore1 = tk.Label(self, text = "Sleep on time: "+ controller.getChoreInfo("1")[0], font = LARGE_FONT)
        Chore1.pack(pady = 10, padx = 10)

        Chore1Info = tk.Label(self, text = "Details: "+ "date: "+ controller.getChoreInfo("1")[1] + " status: "+
                              controller.getChoreInfo("2")[2], font = LARGE_FONT)
        Chore1Info.pack(pady = 10, padx = 10)
        
        Chore2 = tk.Label(self, text = "Drink a lot of water: "+ controller.getChoreInfo("2")[0], font = LARGE_FONT)
        Chore2.pack(pady = 10, padx = 10)

        Chore2Info = tk.Label(self, text = "Details: "+ "date: "+ controller.getChoreInfo("2")[1] + " status: "+
                              controller.getChoreInfo("2")[2], font = LARGE_FONT)
        Chore2Info.pack(pady = 10, padx = 10)

        buttonAddChore = tk.Button(self, text = "Add Today's Accomplishments",
                            command = lambda: controller.show_frame(AddChores))
        buttonAddChore.pack()

        buttonRefresh = tk.Button(self, text = "Refresh",
                            command = lambda: PageChores.changeInfo(Chore1,Chore1Info,Chore2,Chore2Info,
                                                                    controller.getChoreInfo("1")[0],
                                                                    controller.getChoreInfo("1")[1] + " status: "+ controller.getChoreInfo("2")[2],
                                                                    controller.getChoreInfo("2")[0],
                                                                    controller.getChoreInfo("2")[1] + " status: "+ controller.getChoreInfo("2")[2]))
        buttonRefresh.pack()
        

        buttonBack = tk.Button(self, text = "Back",
                            command = lambda: controller.show_frame(PageChildren))
        buttonBack.pack()
        
        buttonHome = tk.Button(self, text = "Home",
                            command = lambda: controller.show_frame(StartPage))
        buttonHome.pack()

class AddChores(tk.Frame):

    def getInput(textBox):
        Input = textBox.get()
        return (Input)
    def __init__(self, parent, controller): # Page enable children to add Chore to database 
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Add Accomplishments", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
      

        label1 = tk.Label(self, text = "Type a Date: ", font = LARGE_FONT)
        label1.pack(pady = 10, padx = 10)
        dateBox = tk.Entry(self)
        dateBox.pack()

        Chore1Button = tk.Button(self, text = "Click Here to Add Sleep on Time",
                            command = lambda: controller.InsertNewChore(1,"Sleep on Time",1,AddChores.getInput(dateBox),"Pending"))
        Chore1Button.pack()

        Chore2Button = tk.Button(self, text = "Click Here to Add Drink a lot of water",
                            command = lambda: controller.InsertNewChore(2,"Drink water",1,AddChores.getInput(dateBox),"Pending"))
        Chore2Button.pack()

        buttonBack = tk.Button(self, text = "Back",
                            command = lambda: controller.show_frame(PageChores))
        buttonBack.pack() 

        buttonHome = tk.Button(self, text = "Home",
                            command = lambda: controller.show_frame(StartPage))
        buttonHome.pack()

class PageBank(tk.Frame): # Children bank page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Bank", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)


        buttonBack = tk.Button(self, text = "Back",
                            command = lambda: controller.show_frame(PageChildren))
        buttonBack.pack()
        
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
                


