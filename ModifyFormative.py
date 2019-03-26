from tkinter import *
import tkinter.messagebox
import pickle
import os
from datetime import datetime
import copy
import os
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
        ModifyForm(rootForm, strName)

class ModifyForm(Frame):

    def __init__(self, master, filename):
        self.filename = filename
        directory = os.getcwd() + "\\formPickle\\" + filename
        pickle_in = open(directory, "rb")
        inList = pickle.load(pickle_in)
        ansList = []
        import csv
        with open("FormativeAnswers.csv") as csvfile:            
                reader = csv.reader(csvfile)
                for row in reader:
                    if row[0] == filename:
                        for i in range(1,11):
                            ansList.append(row[i])
                            
        print(ansList)
        Frame.__init__(self, master)
        self.grid()
        self.createPage()
        self.setDate()
        self.initForm(inList, filename.strip(".pickle"), ansList)
        self.createButton()

    def createPage(self):

        lblProg = Label(self, text='Time allowed for \ntest in minutes:', font=('MS', 8,'bold'))
        lblProg.grid(row=0, column=0, columnspan=2, sticky=E)

        self.listTime = Listbox(self, height= 3)
        scroll = Scrollbar(self, command= self.listTime.yview)
        self.listTime.configure(yscrollcommand=scroll.set)

        self.listTime.grid(row=0, column=2, columnspan=2)
        scroll.grid(row=0, column=4, sticky=W)

        for item in ["10", "15", "20", "25", "30"]:
            self.listTime.insert(END, item)

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

        lblempty= Label(self, text="\t\t\t", font=('MS', 10, "bold"))
        lblempty.grid(row=23, column=0)

        lblempty1= Label(self, text="\t\t\t", font=('MS', 10, "bold"))
        lblempty1.grid(row=24, column=0)
        
        lblAns1= Label(self, text="Answer 1", font=('MS', 10, "bold"))
        lblAns1.grid(row=25, column=0)

        self.varAns1 = StringVar()
        self.entAns1 = Entry(self, textvariable=self.varAns1)
        self.entAns1.grid(row=26, column=0)

        lblAns2= Label(self, text="Answer 2", font=('MS', 10, "bold"))
        lblAns2.grid(row=27, column=0)

        self.varAns2 = StringVar()
        self.entAns2 = Entry(self, textvariable=self.varAns2)
        self.entAns2.grid(row=28, column=0)

        lblAns3= Label(self, text="Answer 3", font=('MS', 10, "bold"))
        lblAns3.grid(row=29, column=0)

        self.varAns3 = StringVar()
        self.entAns3 = Entry(self, textvariable=self.varAns3)
        self.entAns3.grid(row=30, column=0)

        lblAns4= Label(self, text="Answer 4", font=('MS', 10, "bold"))
        lblAns4.grid(row=31, column=0)

        self.varAns4 = StringVar()
        self.entAns4 = Entry(self, textvariable=self.varAns4)
        self.entAns4.grid(row=32, column=0)

        lblAns5= Label(self, text="Answer 5", font=('MS', 10, "bold"))
        lblAns5.grid(row=33, column=0)

        self.varAns5 = StringVar()
        self.entAns5 = Entry(self, textvariable=self.varAns5)
        self.entAns5.grid(row=34, column=0)

        lblAns6= Label(self, text="Answer 6", font=('MS', 10, "bold"))
        lblAns6.grid(row=25, column=1)

        self.varAns6 = StringVar()
        self.entAns6 = Entry(self, textvariable=self.varAns6)
        self.entAns6.grid(row=26, column=1)

        lblAns7= Label(self, text="Answer 7", font=('MS', 10, "bold"))
        lblAns7.grid(row=27, column=1)

        self.varAns7 = StringVar()
        self.entAns7 = Entry(self, textvariable=self.varAns7)
        self.entAns7.grid(row=28, column=1)

        lblAns8= Label(self, text="Answer 8", font=('MS', 10, "bold"))
        lblAns8.grid(row=29, column=1)

        self.varAns8 = StringVar()
        self.entAns8 = Entry(self, textvariable=self.varAns8)
        self.entAns8.grid(row=30, column=1)

        lblAns9= Label(self, text="Answer 9", font=('MS', 10, "bold"))
        lblAns9.grid(row=31, column=1)

        self.varAns9 = StringVar()
        self.entAns9 = Entry(self, textvariable=self.varAns9)
        self.entAns9.grid(row=32, column=1)

        lblAns10= Label(self, text="Answer 10", font=('MS', 10, "bold"))
        lblAns10.grid(row=33, column=1)

        self.varAns10 = StringVar()
        self.entAns10 = Entry(self, textvariable=self.varAns10)
        self.entAns10.grid(row=34, column=1)

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

    def initForm(self, inList, filename, ansList1):
        selfList = copy.deepcopy(inList)
        ansList = copy.deepcopy(ansList1)
        temp = selfList[1]
        selfList[1] = temp.split("/")
        temp = selfList[2]
        selfList[2] = temp.split("/")

        referDic = {"10":0, "15":1, "20":2, "25":3, "30":4}
        self.listTime.selection_set(referDic[selfList[0]])
        self.startD.set(selfList[1][0])
        self.startM.set(selfList[1][1])
        self.startY.set(selfList[1][2])
        self.endD.set(selfList[2][0])
        self.endM.set(selfList[2][1])
        self.endY.set(selfList[2][2])
        self.varQ1.set(selfList[3])
        self.varQ2.set(selfList[4])
        self.varQ3.set(selfList[5])
        self.varQ4.set(selfList[6])
        self.varQ5.set(selfList[7])
        self.varQ6.set(selfList[8])
        self.varQ7.set(selfList[9])
        self.varQ8.set(selfList[10])
        self.varQ9.set(selfList[11])
        self.varQ10.set(selfList[12])
        self.varAns1.set(ansList[0])
        self.varAns2.set(ansList[1])
        self.varAns3.set(ansList[2])
        self.varAns4.set(ansList[3])
        self.varAns5.set(ansList[4])
        self.varAns6.set(ansList[5])
        self.varAns7.set(ansList[6])
        self.varAns8.set(ansList[7])
        self.varAns9.set(ansList[8])
        self.varAns10.set(ansList[9])
        

    def createButton(self):
        butSubmit = Button(self, text='Submit',font=('MS', 10,'bold'), command=self.submit)
        butSubmit.grid(row=22, column=3)

    def submit(self):
        filename = self.filename.strip(".pickle")
        print(filename)
        try:
            self.listTime.curselection()[0]
            listProp = True
        except:
            listProp = False
        if (listProp == False or (len(self.startD.get()) == 0) or (len(self.startM.get()) == 0) or (len(self.startY.get()) == 0) or (len(self.endD.get()) == 0) or
                (len(self.endM.get()) == 0) or (len(self.endY.get()) == 0) or
                (len(self.varQ1.get()) == 0) or (len(self.varQ2.get()) == 0) or (len(self.varQ3.get()) == 0) or (len(self.varQ4.get()) == 0) or
                (len(self.varQ5.get()) == 0) or (len(self.varQ6.get()) == 0) or (len(self.varQ7.get()) == 0) or (len(self.varQ8.get()) == 0) or
                (len(self.varQ9.get()) == 0) or (len(self.varQ10.get()) == 0)or (len(self.varAns1.get()) == 0) or (len(self.varAns2.get()) == 0) or
                (len(self.varAns3.get()) == 0) or (len(self.varAns4.get()) == 0) or (len(self.varAns5.get()) == 0) or (len(self.varAns6.get()) == 0) or
                (len(self.varAns7.get()) == 0) or (len(self.varAns8.get()) == 0) or (len(self.varAns9.get()) == 0) or (len(self.varAns10.get()) == 0)):
            tkinter.messagebox.showwarning("Submit Error", "Select all of the boxes.")
        else:
            index = self.listTime.curselection()[0]
            strTime = str(self.listTime.get(index))

            inList = [strTime, self.startD.get() + "/" + self.startM.get() + "/" + self.startY.get(), self.endD.get() + "/" + self.endM.get() + "/" + self.endY.get(), self.varQ1.get(), self.varQ2.get(), self.varQ3.get(), self.varQ4.get(), self.varQ5.get(), self.varQ6.get(),
                                self.varQ7.get(), self.varQ8.get(), self.varQ9.get(), self.varQ10.get()]
            ansList = [filename + ".pickle", self.varAns1.get(), self.varAns2.get(), self.varAns3.get(), self.varAns4.get(), self.varAns5.get(), self.varAns6.get(), self.varAns7.get(), self.varAns8.get(),
                       self.varAns9.get(), self.varAns10.get()]
            print(ansList)
            import csv
            with open('FormativeAnswers.csv') as csvfile:
                data = list(csv.reader(csvfile))
                print(data)
                print(filename)
            with open('FormativeAnswers1.csv', mode='w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                for row in data:
                    if row[0] != (filename + ".pickle") :
                        writer.writerow(row)
                        print('first if')
                    elif row[0] == (filename + ".pickle"):
                        print('second if')
                        writer.writerow(ansList)
            os.remove("FormativeAnswers.csv")
            os.rename('FormativeAnswers1.csv', 'FormativeAnswers.csv')
                        
                        
    
                
            directory = os.getcwd() + "\\formPickle\\" + filename + ".pickle"
            pickle_out = open(directory, "wb")
            pickle.dump(inList, pickle_out)
            pickle_out.close()
            tkinter.messagebox.showwarning("Submitted", "You have modified " + filename + " successfully!")
            root.destroy()
#main
root = Tk()
root.title("Modify Formative Assessment")
ChooseTest(root)
root.mainloop()
