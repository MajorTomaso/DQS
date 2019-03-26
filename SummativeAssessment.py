#!/usr/bin/python3
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
        directory = os.getcwd() + "\\sumPickle"
        listFile = []
        for file in os.listdir(directory):
            if file.endswith(".pickle"):
                listFile.append(file)

        for item in listFile:
            self.listTest.insert(END, item)
        self.listTest.selection_set(END)

    def Select(self):
        global rootSum
        rootSum = Toplevel(self)
        index = self.listTest.curselection()[0]
        strName = str(self.listTest.get(index))
        root.withdraw()
        SummativeAssessment(rootSum, strName)

class SummativeAssessment(Frame):

    def __init__(self, master, filename):
        self.filename = filename
        global filename1
        filename1=filename
        print(filename)
        directory = os.getcwd() + "\\sumPickle\\" + filename
        pickle_in = open(directory, "rb")
        inList = pickle.load(pickle_in)
        print(inList)

        currentDate = datetime.now()
        dateFormat = "%d/%m/%Y"
        startDate = datetime.strptime(inList[1], dateFormat)
        endDate = datetime.strptime(inList[2], dateFormat)
        if (currentDate > endDate) == True:
            rootSum.destroy()
            errorText = "Test is unavailable after " + inList[2]
            tkinter.messagebox.showwarning("Date Error", errorText)
            root.deiconify()
        elif(currentDate < startDate) == True:
            rootSum.destroy()
            errorText = "Test is available from " + inList[1]
            tkinter.messagebox.showwarning("Date Error", errorText)
            root.deiconify()
        else:
            Frame.__init__(self, master)
            self.grid()
            self.createPage(inList)
            root.after(int(inList[0]) * 1000, lambda: (tkinter.messagebox.showwarning("Time Exceeded", "The test duration has been exceeded, you cannot continue the test."), root.destroy()))


    def createPage(self, inList):

        lblGrid= Label(self, width = "15", height = "2")
        lblGrid.grid(row=0, column=0)

        lblTitle = Label(self, text='Summative Assessment', font=('MS', 12,'bold'))
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
        lblQ5.grid(row=9, column=1, sticky=W)

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

        lblgrid=Label(self)
        lblgrid.grid(row=21,column=0)

        lblQ11=Label(self, text="Enter your name: ", font=('MS', 10, "bold"))
        lblQ11.grid(row=22,column=0, sticky=E)

        self.varQ11 = StringVar()
        self.entQ11 = Entry(self, textvariable=self.varQ11)
        self.entQ11.grid(row=22,column=1, sticky=W)

        butSub = Button(self, text='Submit',font=('MS', 10,'bold'), command= self.Submit)
        butSub.grid(row=22, column=2)


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
            student_result.append(d[0])
            for row in reader:
                if row[0] == filename1:
                    for i in range (1, len(d)):
                        if d[i] == row[i]:
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
root.title("Summative Assessment")
app = ChooseTest(root)
root.mainloop()
