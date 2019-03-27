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

        self.listTest.grid(row=0, column=1)
        scroll.grid(row=0, column=4, sticky=W)

        lblQ11=Label(self, text="Enter your name: ", font=('MS', 10, "bold"))
        lblQ11.grid(row=1,column=0, sticky=E)

        self.username = StringVar()
        self.entName = Entry(self, textvariable=self.username)
        self.entName.grid(row=1,column=1, sticky=W)

        butSelect = Button(self, text='Select',font=('MS', 10,'bold'), command = self.Select)
        butSelect.grid(row=2, column=1, sticky=E)

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
        username = self.username.get()
        global rootSum
        rootSum = Toplevel(self)
        try:
            index = self.listTest.curselection()[0]
            strName = str(self.listTest.get(index))
            root.withdraw()
            print(strName)
            SummativeAssessment(rootSum, strName, username)
        except:
            rootSum.withdraw()
            tkinter.messagebox.showwarning("Error","You need to select one of the tests!")
            root.deiconify()
            

class SummativeAssessment(Frame):

    def __init__(self, master, filename, username):
        self.filename = filename
        global filename1
        filename1=filename
        directory = os.getcwd() + "\\sumPickle\\" + filename
        pickle_in = open(directory, "rb")
        inList = pickle.load(pickle_in)

        currentDate = datetime.now()
        dateFormat = "%d/%m/%Y"
        startDate = datetime.strptime(inList[1], dateFormat)
        endDate = datetime.strptime(inList[2], dateFormat)

        import csv
        foundUser = False
        with open("SummativeResults.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == username:
                    foundUser = True
        if username == "":
            rootSum.destroy()
            tkinter.messagebox.showwarning("Error","You need to enter name !")
            root.deiconify()
            
        elif (currentDate > endDate) == True and foundUser:
            Frame.__init__(self, master)
            rootSum.withdraw()
            tkinter.messagebox.showwarning("Date Error", "You have completed test, you can view you feedback now!")
            rootView = Toplevel(self)
            introPage(rootView, username)
        elif (currentDate > endDate) == True:
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
            self.createPage(inList, username)
            root.after(int(inList[0]) * 1000, lambda: (tkinter.messagebox.showwarning("Time Exceeded", "The test duration has been exceeded, you cannot continue the test."), root.destroy()))


    def createPage(self, inList, username):
        self.username = username
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

        butSub = Button(self, text='Submit',font=('MS', 10,'bold'), command= self.Submit)
        butSub.grid(row=22, column=1)


    def Submit(self):
        d = [self.varQ1.get(), self.varQ2.get(), self.varQ3.get(), self.varQ4.get(), self.varQ5.get(), self.varQ6.get(),
                 self.varQ7.get(), self.varQ8.get(), self.varQ9.get(), self.varQ10.get()]
        for value in d:
            if len(value)==0:
                tkinter.messagebox.showwarning("Entry Error", "Answer all of the questions.")
                break
        import csv
        student_result=[]
        with open("SummativeAnswers.csv") as csvfile:
            reader = csv.reader(csvfile)
            student_result.append(self.username)
            for row in reader:
                if row[0] == filename1:
                    for i in range (0, len(d)):
                        if d[i] == row[i+1]:
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
        tkinter.messagebox.showwarning("Submitted", "You have successfully submitted a test!")
        root.destroy()

class introPage(Frame):
    def __init__(self, master, username):
        Frame.__init__(self, master)
        self.grid()
        self.createPage(username)

    def createPage(self, username):
        self.username = username
        lblProg = Label(self, text='Summative Answers', font=('MS', 12,'bold'), width = "20", height = "3")
        lblProg.grid(row=0, column=1)

        lblGrid= Label(self, width = "20", height = "3")
        lblGrid.grid(row=0, column=0)

        lblGrid= Label(self, width = "20", height = "3")
        lblGrid.grid(row=0, column=2)

        butView = Button(self, text='View Answers',font=('MS', 10,'bold'), command = self.View)
        butView.grid(row=1, column=1)

    def View(self):
        ansroot = Toplevel(self)
        answerPage(ansroot, self.username)
        root.withdraw()


class answerPage(Frame):
    def __init__(self, master, username):
        Frame.__init__(self, master)
        self.grid()
        self.answer(username)

    def answer(self, username):
        import csv
        mark =[]
        with open("SummativeResults.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == username:
                    mark.append(row[11])
                    mark.append(row[12])
        lblProg = Label(self, text='Answers for Question 1-10', font=('MS', 12,'bold'), width = "20", height = "3")
        lblProg.grid(row=0, column=0)

        lblQ1= Label(self, text="1. What is the cardinality of the following set?", font=('MS', 9,'bold'), anchor=W)
        lblQ1.grid(row=1, column=0, columnspan=3, sticky=W)
        lblQ1Ans= Label(self, text="3. (1 and {1} are different)", font=('MS', 9))
        lblQ1Ans.grid(row=2, column=0, columnspan=3, sticky=W)
        lblQ2= Label(self, text="2. What numbers are used in binary?", font=('MS', 9,'bold'), anchor=W)
        lblQ2.grid(row=3, column=0, sticky=W)
        lblQ2Ans= Label(self, text="0 and 1", font=('MS', 9))
        lblQ2Ans.grid(row=4, column=0, columnspan=3, sticky=W)
        lblQ3= Label(self, text="3. What does this symbol ∅ represent?", font=('MS', 9,'bold'), anchor=W)
        lblQ3.grid(row=5, column=0, sticky=W)
        lblQ3Ans= Label(self, text="Empty set", font=('MS', 9))
        lblQ3Ans.grid(row=6, column=0, columnspan=3, sticky=W)
        lblQ4= Label(self, text="4. What does HTML stand for?", font=('MS', 9,'bold'), anchor=W)
        lblQ4.grid(row=7, column=0, sticky=W)
        lblQ4Ans= Label(self, text="Hyper Text Markup Language", font=('MS', 9))
        lblQ4Ans.grid(row=8, column=0, columnspan=3, sticky=W)
        lblQ5= Label(self, text="5. How many bits are in a Byte?", font=('MS', 9,'bold'), anchor=W)
        lblQ5.grid(row=9, column=0, sticky=W)
        lblQ5Ans= Label(self, text="8 bits", font=('MS', 9), )
        lblQ5Ans.grid(row=10, column=0, columnspan=3, sticky=W)
        lblQ6= Label(self, text="6. What is RAM usually measure in?", font=('MS', 9,'bold'), anchor=W)
        lblQ6.grid(row=11, column=0, sticky=W)
        lblQ6Ans= Label(self, text="megabytes or gigabytes", font=('MS', 9))
        lblQ6Ans.grid(row=12, column=0, columnspan=3, sticky=W)
        lblQ7= Label(self, text="7. What is the name for a base 16 system used to simplify how binary is represented?", font=('MS', 9,'bold'), anchor=W)
        lblQ7.grid(row=13, column=0, sticky=W)
        lblQ7Ans= Label(self, text="Hexadecimal", font=('MS', 9))
        lblQ7Ans.grid(row=14, column=0, columnspan=3, sticky=W)
        lblQ8= Label(self, text="8. Convert 16 decimal to hexadecimal.", font=('MS', 9,'bold'), anchor=W)
        lblQ8.grid(row=15, column=0, sticky=W)
        lblQ8Ans= Label(self, text="Hexadecimal counts up to 16, including 0 so after the  15th number (F), the system starts at 10.", font=('MS', 9))
        lblQ8Ans.grid(row=16, column=0, columnspan=3, sticky=W)
        lblQ9= Label(self, text="9. Convert 1011 to decimal.", font=('MS', 9,'bold'), anchor=W)
        lblQ9.grid(row=17, column=0, sticky=W)
        lblQ9Ans= Label(self, text="[1 x 24]+ [0 x 23] + [1 x 22] + [1 x 21] = 11", font=('MS', 9))
        lblQ9Ans.grid(row=18, column=0, columnspan=3, sticky=W)
        lblQ10= Label(self, text="10. Convert 26 decimal to Ternary.", font=('MS', 9,'bold'), anchor=W)
        lblQ10.grid(row=19, column=0, sticky=W)
        lblQ10Ans= Label(self, text="26/3=8 remainder 2, 8/3=2 remainder 2, 2/3= 0 remainder 2. Read remainders backwards gives 222.", font=('MS', 9))
        lblQ10Ans.grid(row=20, column=0, columnspan=3, sticky=W)

        passFail = ""
        if mark[1] == 'P':passFail = "Passed"
        else: passFail = "Failed"
        lblMark = Label(self, text='Mark: '+mark[0]+"%     "+passFail, font=('MS', 12,'bold'), width = "20", height = "3")
        lblMark.grid(row=21, column=0,sticky=E)        

        butView = Button(self, text='Close',font=('MS', 10,'bold'), command = self.close)
        butView.grid(row=21, column=1, sticky=E)

    def close(self):
        root.destroy()






root = Tk()
root.title("Summative Assessment")
app = ChooseTest(root)
root.mainloop()
