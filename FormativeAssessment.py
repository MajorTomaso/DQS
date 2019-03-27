from tkinter import *
import tkinter.messagebox
import pickle
import os
from datetime import datetime

class ChooseTest(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createPage()
    def createPage(self):
        lblList = Label(self, text='Choose Test:', font=('MS', 10,'bold'))
        lblList.grid(row=0, column=0)

        self.listTest = Listbox(self, height= 3)
        scroll = Scrollbar(self, command= self.listTest.yview)
        self.listTest.configure(yscrollcommand=scroll.set)

        self.listTest.grid(row=0, column=2, columnspan=2)
        scroll.grid(row=0, column=4, sticky=W)

        butSelect = Button(self, text='Select',font=('MS', 10,'bold'), command = self.Select)
        butSelect.grid(row=1, column=2)

        #Gets current directory and adds path to the pickle folder
        directory = os.getcwd() + "\\formPickle"
        listFile = []
        for file in os.listdir(directory):
            if file.endswith(".pickle"):
                listFile.append(file)

        for item in listFile:
            self.listTest.insert(END, item)
        self.listTest.selection_set(END)

    def Select(self):
        global rootForm
        rootForm = Toplevel(self)
        index = self.listTest.curselection()[0]
        strName = str(self.listTest.get(index))
        root.withdraw()
        try:
            FormAssessment(rootForm, strName)
        except:
            rootForm.withdraw()
            tkinter.messagebox.showwarning("Date Error", "The date you chose is wrong.")
            root.destroy()

class FormAssessment(Frame):

    def __init__(self, master,filename):
        self.filename = filename
        global filename1
        filename1 = filename
        directory = os.getcwd() + "\\formPickle\\" + filename
        pickle_in = open(directory, "rb")
        inList = pickle.load(pickle_in)
        print(inList)

        currentDate = datetime.now()
        dateFormat = "%d/%m/%Y"
        startDate = datetime.strptime(inList[1], dateFormat)
        endDate = datetime.strptime(inList[2], dateFormat)
        if (currentDate > endDate) == True:
            rootForm.destroy()
            errorText = "Test is unavailable after " + inList[2]
            tkinter.messagebox.showwarning("Date Error", errorText)
            root.deiconify()
        elif(currentDate < startDate) == True:
            rootForm.destroy()
            errorText = "Test is available from " + inList[1]
            tkinter.messagebox.showwarning("Date Error", errorText)
            root.deiconify()
        else:
            Frame.__init__(self, master)
            self.grid()
            self.createPage(inList)
#            root.after(int(inList[0]) * 100, lambda: self.timer())

#    def timer(self):
#        try:
#            rootForm.state()
#            tkinter.messagebox.showwarning("Time Exceeded", "The test duration has been exceeded, you cannot continue the test.")
#            root.destroy()
#        except:
#            pass

    def createPage(self, inList):

        lblGrid= Label(self, width = "15", height = "2")
        lblGrid.grid(row=0, column=0)

        lblTitle = Label(self, text='Formative Assessment', font=('MS', 12,'bold'))
        lblTitle.grid(row=0, column=1)

        lblGrid= Label(self, width = "15", height = "2")
        lblGrid.grid(row=0, column=2)

        lblQ1= Label(self, text=inList[3], font=('MS', 10, "bold"))
        lblQ1.grid(row=1, column=1, sticky=W)

        self.varQ1 = StringVar()
        self.entQ1 = Entry(self, textvariable=self.varQ1, width=40)
        self.entQ1.grid(row=2, column=1, sticky=W)

        lblQ2= Label(self, text=inList[4], font=('MS', 10, "bold"))
        lblQ2.grid(row=3, column=1, sticky=W)

        self.varQ2 = StringVar()
        self.entQ2 = Entry(self, textvariable=self.varQ2, width=40)
        self.entQ2.grid(row=4, column=1, sticky=W)

        lblQ3= Label(self, text=inList[5], font=('MS', 10, "bold"))
        lblQ3.grid(row=5, column=1, sticky=W)

        self.varQ3 = StringVar()
        self.entQ3 = Entry(self, textvariable=self.varQ3, width=40)
        self.entQ3.grid(row=6, column=1, sticky=W)

        lblQ4= Label(self, text=inList[6], font=('MS', 10, "bold"))
        lblQ4.grid(row=7, column=1, sticky=W)

        self.varQ4 = StringVar()
        self.entQ4 = Entry(self, textvariable=self.varQ4, width=40)
        self.entQ4.grid(row=8, column=1, sticky=W)

        lblQ5= Label(self, text=inList[7], font=('MS', 10, "bold"))
        lblQ5.grid(row=9, column=1, columnspan=2, sticky=W)

        self.varQ5 = StringVar()
        self.entQ5 = Entry(self, textvariable=self.varQ5, width=40)
        self.entQ5.grid(row=10, column=1, sticky=W)

        lblQ6= Label(self, text=inList[8], font=('MS', 10, "bold"))
        lblQ6.grid(row=11, column=1, sticky=W)

        self.varQ6 = StringVar()
        self.entQ6 = Entry(self, textvariable=self.varQ6, width=40)
        self.entQ6.grid(row=12, column=1, sticky=W)

        lblQ7= Label(self, text=inList[9], font=('MS', 10, "bold"))
        lblQ7.grid(row=13, column=1, sticky=W)

        self.varQ7 = StringVar()
        self.entQ7 = Entry(self, textvariable=self.varQ7, width=40)
        self.entQ7.grid(row=14, column=1, sticky=W)

        lblQ8= Label(self, text=inList[10], font=('MS', 10, "bold"))
        lblQ8.grid(row=15, column=1, sticky=W)

        self.varQ8 = StringVar()
        self.entQ8 = Entry(self, textvariable=self.varQ8, width=40)
        self.entQ8.grid(row=16, column=1, sticky=W)

        lblQ9= Label(self, text=inList[11], font=('MS', 10, "bold"))
        lblQ9.grid(row=17, column=1, sticky=W)

        self.varQ9 = StringVar()
        self.entQ9 = Entry(self, textvariable=self.varQ9, width=40)
        self.entQ9.grid(row=18, column=1, sticky=W)

        lblQ10= Label(self, text=inList[12], font=('MS', 10, "bold"))
        lblQ10.grid(row=19, column=1, sticky=W)

        self.varQ10 = StringVar()
        self.entQ10 = Entry(self, textvariable=self.varQ10, width=40)
        self.entQ10.grid(row=20, column=1, sticky=W)

        butSub = Button(self, text='Submit',font=('MS', 10,'bold'), command= self.Submit)
        butSub.grid(row=21, column=2)


    def Submit(self):
        if (len(self.varQ1.get()) == 0) or (len(self.varQ2.get()) == 0) or (len(self.varQ3.get()) == 0) or (len(self.varQ4.get()) == 0) or (len(self.varQ5.get()) == 0) or (len(self.varQ6.get()) == 0) or (len(self.varQ7.get()) == 0) or (len(self.varQ8.get()) == 0) or (len(self.varQ9.get()) == 0) or (len(self.varQ10.get()) == 0):
            tkinter.messagebox.showwarning("Entry Error", "Answer all of the questions.")
        else:
            #The results will be stored in a list
            d = [self.varQ1.get(), self.varQ2.get(), self.varQ3.get(), self.varQ4.get(), self.varQ5.get(), self.varQ6.get(),
                 self.varQ7.get(), self.varQ8.get(), self.varQ9.get(), self.varQ10.get()]

            student_result = []
            import csv
            matchList = []
            answerList = []
            with open("FormativeAnswers.csv") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row[0] == filename1:
                        for i in range (0, len(d)):
                            answerList.append(row[i+1])
                            if d[i] == row[i+1]:
                                student_result.append(1)
                                matchList.append(1)
                            else:
                                student_result.append(0)

            print(student_result)
            with open('FormativeResults.csv', mode='a', newline='') as results_file:
                write_results = csv.writer(results_file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                write_results.writerow(student_result)

            try:
                if finAttempt == True:
                    global rootFin
                    rootFin = Toplevel(self)
                    Answers(rootFin, len(matchList), answerList)
                    rootForm.withdraw()
            except:
                global rootRet
                rootRet = Toplevel(self)
                Retry(rootRet, len(matchList))
                rootForm.withdraw() #Disappear
                #root.deiconify() Appear

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

class Retry(Frame):
    def __init__(self, master, correctMarks=0):
        Frame.__init__(self, master)
        self.grid()
        marks = correctMarks
        self.createPage(marks)
        self.createButtons()

    def createPage(self, marks):

        lblGrid= Label(self, width = "15", height = "2")
        lblGrid.grid(row=0, column=0)

        lblTitle = Label(self, text='Retry', font=('MS', 12,'bold'))
        lblTitle.grid(row=0, column=1)

        lblGrid= Label(self, width = "15", height = "2")
        lblGrid.grid(row=0, column=2)

        if marks < (round(0.4 * 10)): #If student gets less than %40 of marks.
            txtPass = "You Failed!"
        else:
            txtPass = "You Passed!"

        lblPass= Label(self, text=txtPass, font=('MS', 10, "bold"))
        lblPass.grid(row=1, column=0, sticky = E)

        txtMark = str(marks)

        lblMark= Label(self, text="You got " + txtMark + "/10", font=('MS', 10))
        lblMark.grid(row=1, column=1)

        lblGrid= Label(self, height = "2")
        lblGrid.grid(row=1, column=2)

        lblGrid= Label(self, height = "2", width = "15")
        lblGrid.grid(row=2, column=2)



    def createButtons(self):

        butRetry = Button(self, text='Retry',font=('MS', 10,'bold'), command = self.Retry)
        butRetry.grid(row=2, column=1)

        butFinal = Button(self, text='Final Attempt',font=('MS', 10,'bold'), command = self.Final)
        butFinal.grid(row=3, column=1)

    def Retry(self):
        rootForm.deiconify()
        rootRet.destroy()

    def Final(self):
        global finAttempt
        finAttempt = True
        rootRet.destroy()
        rootForm.deiconify()

class Answers(Frame):
    def __init__(self, master, correctMarks, answerList):
        Frame.__init__(self, master)
        self.grid()
        marks = correctMarks
        self.createPage(marks, answerList)

    def createPage(self, marks, answerList):
        lblGrid= Label(self, width = "15", height = "2")
        lblGrid.grid(row=0, column=0)

        lblTitle = Label(self, text='Answers', font=('MS', 12,'bold'))
        lblTitle.grid(row=0, column=1)

        lblGrid= Label(self, width = "15", height = "2")
        lblGrid.grid(row=0, column=2)

        if marks < (round(0.4 * 10)): #If student gets less than %40 of marks.
            txtPass = "You Failed, "
        else:
            txtPass = "You Passed, "

        lblMark= Label(self, text=txtPass + str(marks) + "/10", font=('MS', 10, "bold"))
        lblMark.grid(row=1, column=1)

        lblQ1= Label(self, text="Question 1", font=('MS', 10, "bold"))
        lblQ1.grid(row=2, column=0, sticky = W)

        lblQ1A= Label(self, text=answerList[0], font=('MS', 8))
        lblQ1A.grid(row=3, column=0, sticky = W, columnspan = 2)

        lblQ2= Label(self, text="Question 2", font=('MS', 10, "bold"))
        lblQ2.grid(row=4, column=0, sticky = W)

        lblQ2A= Label(self, text=answerList[1], font=('MS', 8))
        lblQ2A.grid(row=5, column=0, sticky = W, columnspan = 2)

        lblQ3= Label(self, text="Question 3", font=('MS', 10, "bold"))
        lblQ3.grid(row=6, column=0, sticky = W)

        lblQ3A= Label(self, text=answerList[2], font=('MS', 8))
        lblQ3A.grid(row=7, column=0, sticky = W, columnspan = 2)

        lblQ4= Label(self, text="Question 4", font=('MS', 10, "bold"))
        lblQ4.grid(row=8, column=0, sticky = W)

        lblQ4A= Label(self, text=answerList[3], font=('MS', 8))
        lblQ4A.grid(row=9, column=0, sticky = W, columnspan = 2)

        lblQ5= Label(self, text="Question 5", font=('MS', 10, "bold"))
        lblQ5.grid(row=10, column=0, sticky = W)

        lblQ5A= Label(self, text=answerList[4], font=('MS', 8))
        lblQ5A.grid(row=11, column=0, sticky = W, columnspan = 2)

        lblQ6= Label(self, text="Question 6", font=('MS', 10, "bold"))
        lblQ6.grid(row=12, column=0, sticky = W)

        lblQ6A= Label(self, text=answerList[5], font=('MS', 8))
        lblQ6A.grid(row=13, column=0, sticky = W, columnspan = 2)

        lblQ7= Label(self, text="Question 7", font=('MS', 10, "bold"))
        lblQ7.grid(row=14, column=0, sticky = W)

        lblQ7A= Label(self, text=answerList[6], font=('MS', 8))
        lblQ7A.grid(row=15, column=0, sticky = W, columnspan = 2)

        lblQ8= Label(self, text="Question 8", font=('MS', 10, "bold"))
        lblQ8.grid(row=16, column=0, sticky = W)

        lblQ8A= Label(self, text=answerList[7], font=('MS', 8))
        lblQ8A.grid(row=17, column=0, sticky = W, columnspan = 2)

        lblQ9= Label(self, text="Question 9", font=('MS', 10, "bold"))
        lblQ9.grid(row=18, column=0, sticky = W)

        lblQ9A= Label(self, text=answerList[8], font=('MS', 8))
        lblQ9A.grid(row=19, column=0, sticky = W, columnspan = 2)

        lblQ10= Label(self, text="Question 10", font=('MS', 10, "bold"))
        lblQ10.grid(row=20, column=0, sticky = W)

        lblQ10A= Label(self, text=answerList[9], font=('MS', 8))
        lblQ10A.grid(row=21, column=0, sticky = W, columnspan = 2)

        butClose = Button(self, text='Close',font=('MS', 10,'bold'), command = root.destroy)
        butClose.grid(row=22, column=3)


#main
root = Tk()
root.title("Formative Assessment")
ChooseTest(root)
root.mainloop()
