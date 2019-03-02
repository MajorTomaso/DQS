from tkinter import *
import tkinter.messagebox
class Login(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.createPage()
        self.createButtons()


    def createPage(self):
    	self.txtDisplay = Text(self, height=2, width=50)
    	self.txtDisplay.tag_configure('boldfont', font=('MS',8, 'bold'))

    	self.txtDisplay.insert(END, "\t\tPlease Login")


    	self.txtDisplay['state'] = DISABLED
    	self.txtDisplay.pack()


    def createButtons(self):
    	button_lecturer = Button(self, text="Lecturer", font = ('MS', 8, 'bold'))
    	button_lecturer['command'] = self.lecturerImport
    	button_lecturer.pack()

    	button_student = Button(self,text="Student", font=('MS',8,'bold'))
    	button_student['command'] = self.studentImport
    	button_student.pack()
    def lecturerImport(self):
    	root.destroy()
    	import lecturerChoice
    

    def studentImport(self):
   		root.destroy()
   		import studentChoice
   	




#Main
root = Tk()
root.title("Login")
app = Login(root)
root.mainloop()