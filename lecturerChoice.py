from tkinter import *
import tkinter.messagebox
class lecturerChoice(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.createPage()
        self.createButtons()

    def createPage(self):
    	self.txtDisplay = Text(self, height=3, width=50)
    	self.txtDisplay.tag_configure('boldfont', font=('MS',8, 'bold'))

    	self.txtDisplay.insert(END, "\t\t      Menu")


    	self.txtDisplay['state'] = DISABLED
    	self.txtDisplay.pack()

    def createButtons(self):
    	button_lecturer = Button(self, text="View Summative Results", font = ('MS', 8, 'bold'))
    	button_lecturer['command'] = self.Summative
    	button_lecturer.pack()
    	

    	button_student = Button(self,text="View Formative Results", font=('MS',8,'bold'))
    	button_student['command'] = self.Formative
    	button_student.pack()

    	button_create = Button(self, text="Create Assessment", font = ('MS', 8, 'bold'))
    	button_create['command'] = self.CreateAssessment
    	button_create.pack()

    	button_modify= Button(self, text="Modify Assessment", font = ('MS', 8, 'bold'))
    	button_modify['command'] = self.ModifyAssessment
    	button_modify.pack()
    def Summative(self):
    	root.destroy()
    	import ViewSummativeResults
    	

    def Formative(self):
    	root.destroy()
    	import ViewFormativeResults
    def CreateAssessment(self):
        root.destroy()
        import CreateAssessment

    def ModifyAssessment(self):
        root.destroy()
        import chooseModify

#Main
root = Tk()
root.title("Lecturer Menu")
app = lecturerChoice(root)
root.mainloop()
