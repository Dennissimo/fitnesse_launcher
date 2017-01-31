#!/usr/bin/env python
import subprocess
import tkinter as tk
from tkinter import *
import os


class launcherwindow():

        def __init__(self,master):

                self.master = master
                self.frame = tk.Frame(master)
                self.lbl = Label(master , text = "Please choose an option:")
                self.lbl.pack()
                self.btn1 = Button(master , text = "Settings" , command = self.launch_settings)
                self.btn1.pack()
                self.btn2 = Button(master, text= "Run a script", state=DISABLED, command=self.launch_runmenu)
                self.btn2.pack()
                self.frame.pack()

        def launch_settings(self):
                self.newWindow = tk.Toplevel(self.master)
                self.app = settingsWindow(self.newWindow)

        def launch_runmenu(self):
            self.newWindow = tk.Toplevel(self.master)
#            self.app = runWindow(self.newWindow)


class settingsWindow():

        runFitnesseCmd=["run_fitnesse.cmd"]

        def __init__(self , master):
                self.var1 = IntVar() #This is the variable bound to checkbutton1 to get the checkbutton state value
                self.var2 = IntVar() #This is the variable bound to checkbutton2 to get the checkbutton state value
                self.var3 = IntVar() # This is the variable bound to checkbutton2 to get the checkbutton state value
                self.var4 = IntVar() # This is the variable bound to checkbutton2 to get the checkbutton state value
                self.var5 = IntVar()  # This is the variable bound to checkbutton2 to get the checkbutton state value
                self.var6 = IntVar()  # This is the variable bound to checkbutton2 to get the checkbutton state value
                self.master = master
                self.frame = tk.Frame(master)
                master.title("Settings")
                rootDirFF = open('settings.txt', encoding='utf-8', )
                rootDirIV = rootDirFF.read()
                self.label1 = tk.Label(self.frame, text = 'Please select only one environment!')
                self.label1.grid(row=0)
                self.entryBox1 = tk.Entry(master)
                self.entryBox1.grid(row=1)
                self.entryBox1.insert(0, rootDirIV)
                self.btn1 = tk.Button(master, text="Save root directory", command=self.set_rootDir)
                self.btn1.grid(row=2)
                self.checkBox1 = tk.Checkbutton(master, text="--team teamwsp2", variable=self.var1, command=self.set_varTeamEnv)
                self.checkBox1.grid(row=4)
                self.checkBox2 = tk.Checkbutton(master, text="--environment TEST2", variable=self.var2, command=self.set_varTest2Env)
                self.checkBox2.grid(row=5)
                self.checkBox3 = tk.Checkbutton(master, text="--environment ACC2", variable=self.var3, command=self.set_varAcc2Env)
                self.checkBox3.grid(row=6)
                self.checkBox4 = tk.Checkbutton(master, text="--browser firefox", variable=self.var4, command=self.set_varBrowFF)
                self.checkBox4.grid(row=8)
                self.checkBox5 = tk.Checkbutton(master, text="--browser chrome", variable=self.var5, command=self.set_varBrowCH)
                self.checkBox5.grid(row=9)
                self.checkBox6 = tk.Checkbutton(master, text="--browser iexplore", variable=self.var6, command=self.set_varBrowIE)
                self.checkBox6.grid(row=10)
                self.btn2 = Button(master, text="Press to Start FitNesse", state=NORMAL, command=self.start_fitnesse_decider)
                self.btn2.grid(row=11)
                #self.separator1 = tk.Canvas(master, width=200, height=100) disabled for now until I know WTF I want with it
                #self.separator1.grid()
                #self.separator1.create_line(100,100,0,0,fill='blue')
                self.frame.grid()

        def set_rootDir(self):
            rootDirNew = self.entryBox1.get()
            rootDirSaveState = open('settings.txt', mode='w', encoding='utf-8')
            rootDirSaveState.write(rootDirNew + "\\")
            print("Gedaan!" + " " + rootDirNew)

        def set_varTeamEnv(self):
            cBox1State = self.var1.get()
            if cBox1State == 1:
                    settingsWindow.runFitnesseCmd.append(" --environment TEST2 --team team34")
                    print(str(settingsWindow.runFitnesseCmd))
            elif cBox1State == 0:
                    settingsWindow.runFitnesseCmd.remove(" --environment TEST2 --team team34")
                    print(str(settingsWindow.runFitnesseCmd))

        def set_varTest2Env(self):
            cBox2State = self.var2.get()
            if cBox2State == 1:
                    settingsWindow.runFitnesseCmd.append(" --environment TEST2")
                    print(settingsWindow.runFitnesseCmd)
            elif cBox2State == 0:
                    settingsWindow.runFitnesseCmd.remove(" --environment TEST2")
                    print(settingsWindow.runFitnesseCmd)

        def set_varAcc2Env(self):
            cBox3State = self.var3.get()
            if cBox3State == 1:
                    settingsWindow.runFitnesseCmd.append(" --environment ACC2")
                    print(settingsWindow.runFitnesseCmd)
            elif cBox3State == 0:
                    settingsWindow.runFitnesseCmd.remove(" --environment ACC2")
                    print(settingsWindow.runFitnesseCmd)

        def set_varBrowFF(self):
            cBox4State = self.var4.get()
            if cBox4State == 1:
                    settingsWindow.runFitnesseCmd.append(" --browser firefox")
                    print(settingsWindow.runFitnesseCmd)
            elif cBox4State == 0:
                    settingsWindow.runFitnesseCmd.remove(" --browser firefox")
                    print(settingsWindow.runFitnesseCmd)

        def set_varBrowCH(self):
            cBox5State = self.var5.get()
            if cBox5State == 1:
                    settingsWindow.runFitnesseCmd.append(" --browser chrome")
                    print(settingsWindow.runFitnesseCmd)
            elif cBox5State == 0:
                    settingsWindow.runFitnesseCmd.remove(" --browser chrome")
                    print(settingsWindow.runFitnesseCmd)

        def set_varBrowIE(self):
            cBox6State = self.var6.get()
            if cBox6State == 1:
                    settingsWindow.runFitnesseCmd.append(" --browser iexplore")
                    print(settingsWindow.runFitnesseCmd)
            elif cBox6State == 0:
                    settingsWindow.runFitnesseCmd.remove(" --browser iexplore")
                    print(settingsWindow.runFitnesseCmd)

        def start_fitnesse_decider(self):
            #need to implement some logic to make sure start button can only be pressed when conditions are met, previous attempt did not work
            #self.btn2.configure(state=NORMAL)
            settingsWindow.fitnesse_batcreator(self)

        def fitnesse_batcreator(self):
            startList = settingsWindow.runFitnesseCmd
            startString = ''.join(startList)
            rootDir = open('settings.txt')
            rootDirFilled = rootDir.readline()
            #now that we have the start string and the place where fitnesse is installed, create a .bat file with the following structure:
            fitnesseBatchFile = "fitnesse_start.bat"
            inputEchoLine = "@echo:on"
            inputStartLine = "START /D " + str(rootDirFilled) + " /WAIT /B " + str(startString)
            try:
                os.remove(fitnesseBatchFile)
            except OSError:
                print("Het bestand kon niet worden verwijderd. Dit kan doordat het bestand nog niet bestond, of doordat het bestand een andere naam heeft gekregen.")
            file = open("fitnesse_start.bat", "w")
            file.write(inputEchoLine)
            file.write("\n")
            file.write(inputStartLine)
            file.close()
            settingsWindow.fitnesse_runner(self)

        def fitnesse_runner(self):
            print("Draai 'm zelf maar!!")
            #insert command here to start the batch file




'''
class runWindow():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        master.title("a")
        self.label1 = tk.Label(self.frame, text='Please choose a script to run:')
        self.label1.pack()
        self.frame.pack()
'''

root = Tk()
root.title("Script launcher v0.01")
root.geometry("350x120")
app = launcherwindow(root)
root.mainloop()
