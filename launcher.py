#!/usr/bin/env python
# import subprocess
import tkinter as tk
from tkinter import *
import os


class LauncherWindow:

        def __init__(self,master):

                self.master = master
                self.frame = tk.Frame(master)
                self.lbl = Label(master, text="Please choose an option:")
                self.lbl.pack()
                self.btn1 = Button(master, text="Settings" , command=self.launch_settings)
                self.btn1.pack()
                self.btn2 = Button(master, text="Run a script", state=DISABLED, command=self.launch_runmenu)
                self.btn2.pack()
                self.frame.pack()

        def launch_settings(self):
                self.newWindow = tk.Toplevel(self.master)
                self.app = SettingsWindow(self.newWindow)

        def launch_runmenu(self):
            self.newWindow = tk.Toplevel(self.master)
#            self.app = runWindow(self.newWindow)


class SettingsWindow:

        runfitnessecmd=["run_fitnesse.cmd"]

        def __init__(self , master):
                self.var1 = IntVar()  # This is the variable bound to checkbutton1 to get the checkbutton state value
                self.var2 = IntVar()  # This is the variable bound to checkbutton2 to get the checkbutton state value
                self.var3 = IntVar()  # This is the variable bound to checkbutton2 to get the checkbutton state value
                self.var4 = IntVar()  # This is the variable bound to checkbutton2 to get the checkbutton state value
                self.var5 = IntVar()  # This is the variable bound to checkbutton2 to get the checkbutton state value
                self.var6 = IntVar()  # This is the variable bound to checkbutton2 to get the checkbutton state value
                self.master = master
                self.frame = tk.Frame(master)
                master.title("Settings")
                rootdirff = open('settings.txt', encoding='utf-8', )
                rootdiriv = rootdirff.read()
                self.label1 = tk.Label(self.frame, text='Please select only one environment!')
                self.label1.grid(row=0)
                self.entryBox1 = tk.Entry(master)
                self.entryBox1.grid(row=1)
                self.entryBox1.insert(0, rootdiriv)
                self.btn1 = tk.Button(master, text="Save root directory", command=self.set_rootDir)
                self.btn1.grid(row=2)
                self.checkBox1 = tk.Checkbutton(master, text="--team teamwsp2", variable=self.var1, command=self.set_var_teamenvironment)
                self.checkBox1.grid(row=4)
                self.checkBox2 = tk.Checkbutton(master, text="--environment TEST2", variable=self.var2, command=self.set_var_test2environment)
                self.checkBox2.grid(row=5)
                self.checkBox3 = tk.Checkbutton(master, text="--environment ACC2", variable=self.var3, command=self.set_var_acc2environment)
                self.checkBox3.grid(row=6)
                self.checkBox4 = tk.Checkbutton(master, text="--browser firefox", variable=self.var4, command=self.set_var_browserfirefox)
                self.checkBox4.grid(row=8)
                self.checkBox5 = tk.Checkbutton(master, text="--browser chrome", variable=self.var5, command=self.set_var_browserchrome)
                self.checkBox5.grid(row=9)
                self.checkBox6 = tk.Checkbutton(master, text="--browser iexplore", variable=self.var6, command=self.set_var_browserie)
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

        def set_var_teamenvironment(self):
            cbox1state = self.var1.get()
            if cbox1state == 1:
                    SettingsWindow.runfitnessecmd.append(" --environment TEST2 --team team34")
                    # print(str(SettingsWindow.runfitnessecmd))
            elif cbox1state == 0:
                    SettingsWindow.runfitnessecmd.remove(" --environment TEST2 --team team34")
                    # print(str(SettingsWindow.runfitnessecmd))

        def set_var_test2environment(self):
            cbox2state = self.var2.get()
            if cbox2state == 1:
                    SettingsWindow.runfitnessecmd.append(" --environment TEST2")
                    # print(SettingsWindow.runfitnessecmd)
            elif cbox2state == 0:
                    SettingsWindow.runfitnessecmd.remove(" --environment TEST2")
                    # print(SettingsWindow.runfitnessecmd)

        def set_var_acc2environment(self):
            cbox3state = self.var3.get()
            if cbox3state == 1:
                    SettingsWindow.runfitnessecmd.append(" --environment ACC2")
                    # print(SettingsWindow.runfitnessecmd)
            elif cbox3state == 0:
                    SettingsWindow.runfitnessecmd.remove(" --environment ACC2")
                    # print(SettingsWindow.runfitnessecmd)

        def set_var_browserfirefox(self):
            cbox4state = self.var4.get()
            if cbox4state == 1:
                    SettingsWindow.runfitnessecmd.append(" --browser firefox")
                    # print(SettingsWindow.runfitnessecmd)
            elif cbox4state == 0:
                    SettingsWindow.runfitnessecmd.remove(" --browser firefox")
                    # print(SettingsWindow.runfitnessecmd)

        def set_var_browserchrome(self):
            cbox5state = self.var5.get()
            if cbox5state == 1:
                    SettingsWindow.runfitnessecmd.append(" --browser chrome")
                    # print(SettingsWindow.runfitnessecmd)
            elif cbox5state == 0:
                    SettingsWindow.runfitnessecmd.remove(" --browser chrome")
                    # print(SettingsWindow.runfitnessecmd)

        def set_var_browserie(self):
            cbox6state = self.var6.get()
            if cbox6state == 1:
                    SettingsWindow.runfitnessecmd.append(" --browser iexplore")
                    # print(SettingsWindow.runfitnessecmd)
            elif cbox6state == 0:
                    SettingsWindow.runfitnessecmd.remove(" --browser iexplore")
                    # print(SettingsWindow.runfitnessecmd)

        def start_fitnesse_decider(self):
            # need to implement some logic to make sure start button can only be pressed when conditions are met, previous attempt did not work
            # self.btn2.configure(state=NORMAL)
            SettingsWindow.fitnesse_batcreator(self)

        def fitnesse_batcreator(self):
            startlist = SettingsWindow.runfitnessecmd
            startstring = ''.join(startlist)
            rootdir = open('settings.txt')
            rootdirfilled = rootdir.readline()
            # now that we have the start string and the place where fitnesse is installed, create a .bat file with the following structure:
            fitnessebatchfile = "fitnesse_start.bat"
            inputecholine = "@echo:on"
            inputstartline = "START /D " + str(rootdirfilled) + " /WAIT /B " + str(startstring)
            try:
                os.remove(fitnessebatchfile)
            except OSError:
                print("This error appears when the bat file could not be removed: the file did not exist yet, or it was renamed. A new bat file has been created.")
            file = open("fitnesse_start.bat", "w")
            file.write(inputecholine)
            file.write("\n")
            file.write(inputstartline)
            file.close()
            SettingsWindow.fitnesse_runner(self)

        def fitnesse_runner(self):
            print("Bat file was created, you can run it from the directory where this repo was put.")
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
app = LauncherWindow(root)
root.mainloop()
