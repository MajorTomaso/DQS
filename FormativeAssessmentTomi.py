#!/usr/bin/python3
from tkinter import *
import tkinter.messagebox
class FormAssessment(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createPage()
        
    def createPage(self):
        
        lblGrid= Label(self, width = "15", height = "2")
        lblGrid.grid(row=0, column=0)

        lblTitle = Label(self, text='Formative Assessment', font=('MS', 12,'bold'))
        lblTitle.grid(row=0, column=1)

        lblGrid= Label(self, width = "15", height = "2")
        lblGrid.grid(row=0, column=2)

        lblQ1= Label(self, text="Question 1", font=('MS', 10, "bold"))
        lblQ1.grid(row=1, column=0)

        self.varQ1 = StringVar()
        self.entQ1 = Entry(self, textvariable=self.varQ1)
        self.entQ1.grid(row=2, column=0)

        lblQ2= Label(self, text="Question 2", font=('MS', 10, "bold"))
        lblQ2.grid(row=3, column=0)

        self.varQ2 = StringVar()
        self.entQ2 = Entry(self, textvariable=self.varQ2)
        self.entQ2.grid(row=4, column=0)

        lblQ3= Label(self, text="Question 3", font=('MS', 10, "bold"))
        lblQ3.grid(row=5, column=0)

        self.varQ3 = StringVar()
        self.entQ3 = Entry(self, textvariable=self.varQ3)
        self.entQ3.grid(row=6, column=0)

        lblQ4= Label(self, text="Question 4", font=('MS', 10, "bold"))
        lblQ4.grid(row=7, column=0)

        self.varQ4 = StringVar()
        self.entQ4 = Entry(self, textvariable=self.varQ4)
        self.entQ4.grid(row=8, column=0)

        lblQ5= Label(self, text="Question 5", font=('MS', 10, "bold"))
        lblQ5.grid(row=9, column=0)

        self.varQ5 = StringVar()
        self.entQ5 = Entry(self, textvariable=self.varQ5)
        self.entQ5.grid(row=10, column=0)

        lblQ6= Label(self, text="Question 6", font=('MS', 10, "bold"))
        lblQ6.grid(row=1, column=1)

        self.varQ6 = StringVar()
        self.entQ6 = Entry(self, textvariable=self.varQ6)
        self.entQ6.grid(row=2, column=1)

        lblQ7= Label(self, text="Question 7", font=('MS', 10, "bold"))
        lblQ7.grid(row=3, column=1)

        self.varQ7 = StringVar()
        self.entQ7 = Entry(self, textvariable=self.varQ7)
        self.entQ7.grid(row=4, column=1)

        lblQ8= Label(self, text="Question 8", font=('MS', 10, "bold"))
        lblQ8.grid(row=5, column=1)

        self.varQ8 = StringVar()
        self.entQ8 = Entry(self, textvariable=self.varQ8)
        self.entQ8.grid(row=6, column=1)

        lblQ9= Label(self, text="Question 9", font=('MS', 10, "bold"))
        lblQ9.grid(row=7, column=1)

        self.varQ9 = StringVar()
        self.entQ9 = Entry(self, textvariable=self.varQ9)
        self.entQ9.grid(row=8, column=1)

        lblQ10= Label(self, text="Question 10", font=('MS', 10, "bold"))
        lblQ10.grid(row=9, column=1)

        self.varQ10 = StringVar()
        self.entQ10 = Entry(self, textvariable=self.varQ10)
        self.entQ10.grid(row=10, column=1)
 
        butSub = Button(self, text='Submit',font=('MS', 10,'bold'), command= self.Submit)
        butSub.grid(row=11, column=2)

    def Submit(self):
        if (len(self.varQ1.get()) == 0) or (len(self.varQ2.get()) == 0) or (len(self.varQ3.get()) == 0) or (len(self.varQ4.get()) == 0) or (len(self.varQ5.get()) == 0) or (len(self.varQ6.get()) == 0) or (len(self.varQ7.get()) == 0) or (len(self.varQ8.get()) == 0) or (len(self.varQ9.get()) == 0) or (len(self.varQ10.get()) == 0):
            tkinter.messagebox.showwarning("Entry Error", "Answer all of the questions.")
        else:
            #The results will be stored in a list
            d = [self.varQ1.get(), self.varQ2.get(), self.varQ3.get(), self.varQ4.get(), self.varQ5.get(), self.varQ6.get(),
                 self.varQ7.get(), self.varQ8.get(), self.varQ9.get(), self.varQ10.get()]

            matchList = []
            student_result = []
            import csv
            with open("FormativeAnswers.csv") as csvfile:
                csvAns = csv.reader(csvfile)
                for answers in csvAns:
                    listAns = answers
                    i = 0;
                    while i != len(listAns):
                        if listAns[i] == d[i]:
                            matchList.append(listAns[i])
                        i = i + 1
            with open("FormativeAnswers.csv") as csvfile:            
                reader = csv.reader(csvfile)
                row1 = next(reader)
                for i in range (0, len(d)): 
                    if d[i] == row1[i]:
                        student_result.append(1)
                    else:
                        student_result.append(0)
            print(matchList)
            print(student_result)
            with open('FormativeResults.csv', mode='a', newline='') as results_file:
                write_results = csv.writer(results_file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                write_results.writerow(student_result)           
            try:
                if finAttempt == True:
                    global root3
                    root3 = Toplevel(self)
                    Answers(root3, len(matchList))
                    root.withdraw()
            except:
                global root2
                root2 = Toplevel(self)
                Retry(root2, len(matchList))
                root.withdraw() #Disappear
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
        root.deiconify()
        #clear form
        root2.destroy()

    def Final(self):
        global finAttempt
        finAttempt = True
        root2.destroy()
        root.deiconify()

class Answers(Frame):
    def __init__(self, master, correctMarks):
        Frame.__init__(self, master)
        self.grid()
        marks = correctMarks
        self.createPage(marks)
        
    def createPage(self, marks):
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

        lblQ1A= Label(self, text="The answer for Question 1", font=('MS', 8))
        lblQ1A.grid(row=3, column=0, sticky = W, columnspan = 2)

        lblQ2= Label(self, text="Question 2", font=('MS', 10, "bold"))
        lblQ2.grid(row=4, column=0, sticky = W)

        lblQ2A= Label(self, text="The answer for Question 2", font=('MS', 8))
        lblQ2A.grid(row=5, column=0, sticky = W, columnspan = 2)
        
        lblQ3= Label(self, text="Question 3", font=('MS', 10, "bold"))
        lblQ3.grid(row=6, column=0, sticky = W)

        lblQ3A= Label(self, text="The answer for Question 3", font=('MS', 8))
        lblQ3A.grid(row=7, column=0, sticky = W, columnspan = 2)

        lblQ4= Label(self, text="Question 4", font=('MS', 10, "bold"))
        lblQ4.grid(row=8, column=0, sticky = W)

        lblQ4A= Label(self, text="The answer for Question 4", font=('MS', 8))
        lblQ4A.grid(row=9, column=0, sticky = W, columnspan = 2)

        lblQ5= Label(self, text="Question 5", font=('MS', 10, "bold"))
        lblQ5.grid(row=10, column=0, sticky = W)

        lblQ5A= Label(self, text="The answer for Question 5", font=('MS', 8))
        lblQ5A.grid(row=11, column=0, sticky = W, columnspan = 2)

        lblQ6= Label(self, text="Question 6", font=('MS', 10, "bold"))
        lblQ6.grid(row=12, column=0, sticky = W)

        lblQ6A= Label(self, text="The answer for Question 6", font=('MS', 8))
        lblQ6A.grid(row=13, column=0, sticky = W, columnspan = 2)
        
        lblQ7= Label(self, text="Question 7", font=('MS', 10, "bold"))
        lblQ7.grid(row=14, column=0, sticky = W)

        lblQ7A= Label(self, text="The answer for Question 7", font=('MS', 8))
        lblQ7A.grid(row=15, column=0, sticky = W, columnspan = 2)

        lblQ8= Label(self, text="Question 8", font=('MS', 10, "bold"))
        lblQ8.grid(row=16, column=0, sticky = W)

        lblQ8A= Label(self, text="The answer for Question 8", font=('MS', 8))
        lblQ8A.grid(row=17, column=0, sticky = W, columnspan = 2)

        lblQ9= Label(self, text="Question 9", font=('MS', 10, "bold"))
        lblQ9.grid(row=18, column=0, sticky = W)

        lblQ9A= Label(self, text="The answer for Question 9", font=('MS', 8))
        lblQ9A.grid(row=19, column=0, sticky = W, columnspan = 2)

        lblQ10= Label(self, text="Question 10", font=('MS', 10, "bold"))
        lblQ10.grid(row=20, column=0, sticky = W)

        lblQ10A= Label(self, text="The answer for Question 10", font=('MS', 8))
        lblQ10A.grid(row=21, column=0, sticky = W, columnspan = 2)
        
#main
root = Tk()
root.title("Formative Assessment")
app = FormAssessment(root)
root.mainloop()
