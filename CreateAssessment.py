from tkinter import *
import tkinter.messagebox
import pickle
import os

class CreateAssessment(Frame):
    # GUI Setup
    def __init__(self, master):
        # Initialise Questionnaire Class
        Frame.__init__(self, master)
        self.grid()

        self.createTypeOfTest()
        self.createPage()
        self.createButtons()
        self.setDate()

    def createPage(self):
        # Create widgets to select a degree programme from a list
        lblProg = Label(self, text='Time allowed for \ntest in minutes:', font=('MS', 8,'bold'))
        lblProg.grid(row=0, column=0, columnspan=2, sticky=E)

        self.listTime = Listbox(self, height= 3)
        scroll = Scrollbar(self, command= self.listTime.yview)
        self.listTime.configure(yscrollcommand=scroll.set)

        self.listTime.grid(row=0, column=2, columnspan=2)
        scroll.grid(row=0, column=4, sticky=W)

        for item in ["10", "15", "20", "25", "30"]:
            self.listTime.insert(END, item)
        self.listTime.selection_set(END)

        lblQ1= Label(self, text="Question 1", font=('MS', 10, "bold"))
        lblQ1.grid(row=13, column=0)

        self.varQ1 = StringVar()
        self.entQ1 = Entry(self, textvariable=self.varQ1)
        self.entQ1.grid(row=14, column=0)

        lblQ2= Label(self, text="Question 2", font=('MS', 10, "bold"))
        lblQ2.grid(row=15, column=0)

        self.varQ2 = StringVar()
        self.entQ2 = Entry(self, textvariable=self.varQ2)
        self.entQ2.grid(row=16, column=0)

        lblQ3= Label(self, text="Question 3", font=('MS', 10, "bold"))
        lblQ3.grid(row=17, column=0)

        self.varQ3 = StringVar()
        self.entQ3 = Entry(self, textvariable=self.varQ3)
        self.entQ3.grid(row=18, column=0)

        lblQ4= Label(self, text="Question 4", font=('MS', 10, "bold"))
        lblQ4.grid(row=19, column=0)

        self.varQ4 = StringVar()
        self.entQ4 = Entry(self, textvariable=self.varQ4)
        self.entQ4.grid(row=20, column=0)

        lblQ5= Label(self, text="Question 5", font=('MS', 10, "bold"))
        lblQ5.grid(row=21, column=0)

        self.varQ5 = StringVar()
        self.entQ5 = Entry(self, textvariable=self.varQ5)
        self.entQ5.grid(row=22, column=0)

        lblQ6= Label(self, text="Question 6", font=('MS', 10, "bold"))
        lblQ6.grid(row=13, column=1)

        self.varQ6 = StringVar()
        self.entQ6 = Entry(self, textvariable=self.varQ6)
        self.entQ6.grid(row=14, column=1)

        lblQ7= Label(self, text="Question 7", font=('MS', 10, "bold"))
        lblQ7.grid(row=15, column=1)

        self.varQ7 = StringVar()
        self.entQ7 = Entry(self, textvariable=self.varQ7)
        self.entQ7.grid(row=16, column=1)

        lblQ8= Label(self, text="Question 8", font=('MS', 10, "bold"))
        lblQ8.grid(row=17, column=1)

        self.varQ8 = StringVar()
        self.entQ8 = Entry(self, textvariable=self.varQ8)
        self.entQ8.grid(row=18, column=1)

        lblQ9= Label(self, text="Question 9", font=('MS', 10, "bold"))
        lblQ9.grid(row=19, column=1)

        self.varQ9 = StringVar()
        self.entQ9 = Entry(self, textvariable=self.varQ9)
        self.entQ9.grid(row=20, column=1)

        lblQ10= Label(self, text="Question 10", font=('MS', 10, "bold"))
        lblQ10.grid(row=21, column=1)

        self.varQ10 = StringVar()
        self.entQ10 = Entry(self, textvariable=self.varQ10)
        self.entQ10.grid(row=22, column=1)

        lblFileName = Label(self, text="Test Name:")
        lblFileName.grid(row=16, column = 2, sticky=E)
        self.testname = StringVar()
        eName = Entry(self, textvariable=self.testname)
        eName.grid(row=16, column=3)

    def createTypeOfTest(self):

        lblSecTitle = Label(self, text = 'Type of Test:', font=('MS', 8,'bold'))
        lblSecTitle.grid(row=4, column= 0)
        lblForm = Label(self, text = 'Formative', font=('MS', 8,'bold'))
        lblForm.grid(row=5, column= 0)
        lblSum = Label(self, text = 'Summative', font=('MS', 8,'bold'))
        lblSum.grid(row=6, column= 0)

        self.testVar = IntVar()
        form = Radiobutton(self, variable=self.testVar, value=1)
        form.grid(row=5, column= 1)
        summ = Radiobutton(self, variable= self.testVar, value=2)
        summ.grid(row=6, column= 1)


    def setDate(self):
        Label(self, text="Start Date").grid(row=10)
        Label(self, text="End Date").grid(row=11)

        self.startD = StringVar()
        self.startM = StringVar()
        self.startY = StringVar()
        self.endD = StringVar()
        self.endM = StringVar()
        self.endY = StringVar()

        self.ent1 = Entry(self, width= 3, textvariable=self.startD)
        self.ent2 = Entry(self, width = 3, textvariable=self.startM)
        self.ent3 = Entry(self, width = 6, textvariable=self.startY)
        self.ent4 = Entry(self, width = 3, textvariable=self.endD)
        self.ent5 = Entry(self, width = 3, textvariable=self.endM)
        self.ent6 = Entry(self, width = 6, textvariable=self.endY)

        self.ent1.grid(row=10, column=1)
        self.ent2.grid(row=10, column=2)
        self.ent3.grid(row=10, column=3)
        self.ent4.grid(row=11, column=1)
        self.ent5.grid(row=11, column=2)
        self.ent6.grid(row=11, column=3)

    def createButtons(self):
        butClear = Button(self, text='Clear',font=('MS', 10,'bold'), command=self.clear)
        butClear.grid(row=18, column=3)

        butSubmit = Button(self, text='Submit',font=('MS', 10,'bold'), command=self.submit)
        butSubmit.grid(row=18, column=2)


    def clear(self):
        self.testname.set("")
        self.listTime.selection_clear(0,END)
        self.startD.set("")
        self.startM.set("")
        self.startY.set("")
        self.endD.set("")
        self.endM.set("")
        self.endY.set("")
        self.testVar.set(0)
        self.varQ1.set("")
        self.varQ2.set("")
        self.varQ3.set("")
        self.varQ4.set("")
        self.varQ5.set("")
        self.varQ6.set("")
        self.varQ7.set("")
        self.varQ8.set("")
        self.varQ9.set("")
        self.varQ10.set("")

    def submit(self):
        try:
            self.listTime.curselection()[0]
            listProp = True
        except:
            listProp = False
        if (listProp == False or (len(self.startD.get()) == 0) or (len(self.startM.get()) == 0) or (len(self.startY.get()) == 0) or (len(self.endD.get()) == 0) or
                (len(self.endM.get()) == 0) or (len(self.endY.get()) == 0) or self.testVar.get() == 0 or (len(self.testname.get()) == 0) or
                (len(self.varQ1.get()) == 0) or (len(self.varQ2.get()) == 0) or (len(self.varQ3.get()) == 0) or (len(self.varQ4.get()) == 0) or
                (len(self.varQ5.get()) == 0) or (len(self.varQ6.get()) == 0) or (len(self.varQ7.get()) == 0) or (len(self.varQ8.get()) == 0) or
                (len(self.varQ9.get()) == 0) or (len(self.varQ10.get()) == 0)):
            tkinter.messagebox.showwarning("Submit Error", "Select all of the boxes.")
        else:
            index = self.listTime.curselection()[0]
            strTime = str(self.listTime.get(index))

            inList = [strTime, self.startD.get() + "/" + self.startM.get() + "/" + self.startY.get(), self.endD.get() + "/" + self.endM.get() + "/" + self.endY.get(), self.varQ1.get(), self.varQ2.get(), self.varQ3.get(), self.varQ4.get(), self.varQ5.get(), self.varQ6.get(),
                                self.varQ7.get(), self.varQ8.get(), self.varQ9.get(), self.varQ10.get()]
            if self.testVar.get() == 1:
                directory = os.getcwd() + "\\formPickle\\" + self.testname.get() + ".pickle"
            else:
                directory = os.getcwd() + "\\sumPickle\\" + self.testname.get() + ".pickle"
            pickle_out = open(directory, "wb")
            pickle.dump(inList, pickle_out)
            pickle_out.close()
            tkinter.messagebox.showwarning("Submitted", "You have created a test successfully!")
            root.destroy()


#main
root = Tk()
root.title("Create Assessment")
app = CreateAssessment(root)
root.mainloop()
