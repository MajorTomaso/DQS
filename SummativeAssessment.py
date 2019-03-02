#!/usr/bin/python3
from tkinter import *
import tkinter.messagebox
class SummativeAssessment(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createPage()
        
    def createPage(self):
        
        lblGrid= Label(self, width = "15", height = "2")
        lblGrid.grid(row=0, column=0)

        lblTitle = Label(self, text='Summative Assessment', font=('MS', 12,'bold'))
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
        
        lblQ11=Label(self, text="Enter your name: ", font=('MS', 10, "bold"))
        lblQ11.grid(row=11,column=0)

        self.varQ11 = StringVar()
        self.entQ11 = Entry(self, textvariable=self.varQ11)
        self.entQ11.grid(row=11,column=1)

        butSub = Button(self, text='Submit',font=('MS', 10,'bold'), command= self.Submit)
        butSub.grid(row=11, column=2)


    def Submit(self):
        d = [self.varQ11.get(),self.varQ1.get(), self.varQ2.get(), self.varQ3.get(), self.varQ4.get(), self.varQ5.get(), self.varQ6.get(),
                 self.varQ7.get(), self.varQ8.get(), self.varQ9.get(), self.varQ10.get()]
        for value in d:
            if len(value)==0:
                tkinter.messagebox.showwarning("Entry Error", "Answer all of the questions.")
                break
        import csv
        student_result=[]
        with open('SummativeAnswers.csv') as csvfile:
            reader = csv.reader(csvfile)
            row1 = next(reader)
            student_result.append(d[0])
            for i in range (1, len(d)): 
                if d[i] == row1[i-1]:
                    student_result.append(1)
                else:
                    student_result.append(0)
        sum = 0
        for i in range(1,len(student_result)):
            sum+=student_result[i]
        student_result.append(sum*10)
        if sum*10 >= 40:
            student_result.append("P")
        else:
            student_result.append("F")
        with open('SummativeResults.csv', mode='a', newline='') as results_file:
            write_results = csv.writer(results_file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
            write_results.writerow(student_result)

        exit()




                
        


       
                        
root = Tk()
root.title("Formative Assessment")
app = SummativeAssessment(root)
root.mainloop()