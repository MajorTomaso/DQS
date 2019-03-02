#!/usr/bin/python3
from tkinter import *
import tkinter.messagebox
class studentChoice(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.createPage()
        self.createButtons()

    def createPage(self):
    	self.txtDisplay = Text(self, height=10, width=50)
    	self.txtDisplay.tag_configure('boldfont', font=('MS',8, 'bold'))

    	self.txtDisplay.insert(END, "\t\tChoose a test")


    	self.txtDisplay['state'] = DISABLED
    	self.txtDisplay.pack()

    def createButtons(self):
    	button_lecturer = Button(self, text="Summative Assessment", font = ('MS', 8, 'bold'))
    	button_lecturer['command'] = self.Summative
    	button_lecturer.pack()

    	button_student = Button(self,text="Formative Assessment", font=('MS',8,'bold'))
    	button_student['command'] = self.Formative
    	button_student.pack()
    def Summative(self):
    	root.destroy()
    	import SummativeAssessment
    	

    def Formative(self):
    	root.destroy()
    	import FormativeAssessment


#Main
root = Tk()
root.title("Choose a test")
app = studentChoice(root)
root.mainloop()