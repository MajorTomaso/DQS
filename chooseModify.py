from tkinter import *
import tkinter.messagebox
class chooseModify(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.createPage()
        self.createButtons()

    def createPage(self):
    	self.txtDisplay = Text(self, height=2, width=50)
    	self.txtDisplay.tag_configure('boldfont', font=('MS',8, 'bold'))

    	self.txtDisplay.insert(END, "\t\tChoose a test to modify")


    	self.txtDisplay['state'] = DISABLED
    	self.txtDisplay.pack()

    def createButtons(self):
    	button_summative = Button(self, text="Modify Summative Test", font = ('MS', 8, 'bold'))
    	button_summative['command'] = self.Summative
    	button_summative.pack()
    	

    	button_formative = Button(self,text="Modify Formative Test", font=('MS',8,'bold'))
    	button_formative['command'] = self.Formative
    	button_formative.pack()
    def Summative(self):
        root.destroy()
        import ModifySummative

    def Formative(self):
        root.destroy()
        import ModifyFormative




#Main
root = Tk()
root.title("Choose a test to modify")
app = chooseModify(root)
root.mainloop()

