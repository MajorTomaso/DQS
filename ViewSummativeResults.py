import csv
import os
from tkinter import *
import tkinter.messagebox
import collections


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
        global rootSum
        rootSum = Toplevel(self)
        index = self.listTest.curselection()[0]
        strName = str(self.listTest.get(index))
        global filename1
        filename1 = strName
        root.destroy()
        CalculateResults(strName)
    
            
class CalculateResults(Frame):
	def __init__(self, filename):
		Frame.__init__(self)
		self.grid()
		self.createPage(filename)
		self.createButtons()
	def createPage(self, filename):
		student_results = {}
		sum_all_percentages = 0
		number_of_students = 0
		student_questions = []
		counter = 0
		global student_and_results
		student_and_results = {}
		with open('SummativeResults.csv') as all_results:
			all_results = csv.reader(all_results)
			next(all_results,None)
			for row in all_results:
				if row[0] == filename:
					student_results[row[1]] = [row[i] for i in range(12, 14)]
					student_and_results[row[1]] = [row[i] for i in range(2,12)]
					sum_all_percentages += float(row[12])
					number_of_students += 1
					student_questions.append([row[i] for i in range(2,12)])
					summary = round(sum_all_percentages/number_of_students,2)
					counter += 1
			student_results = collections.OrderedDict(student_results)
			lblGrid= Label(self, width = "15", height = "5")
			lblGrid.grid(row=0, column=0)
			lblGrid = Label(self, width="15", height="2")
			lblGrid.grid(row=0, column=0)
			Label(self, width="25", height="2", text = "Results for %s "%filename[:-7]  , font=('MS', 10, 'bold')).grid(row=0, column=1)
			Label(self, text="Student", font=('MS',10,"bold")).grid(row=1, column=0)
			Label(self, text="Mark", font=('MS',10,"bold")).grid(row=1, column=1)
			Label(self, text="Pass/Fail", font=('MS',10,"bold")).grid(row=1, column=2)
			lblGrid = Label(self, width="15", height="2")
			lblGrid.grid(row=0, column=2)
			for student,performance in student_results.items():
				Label(self, text=student , font=('MS',10,"bold")).grid(row=list(student_results.keys()).index(student)+5,column=0)
				Label(self, text=performance[0] , font=('MS',10,"bold")).grid(row=list(student_results.keys()).index(student)+5,column=1)
				Label(self, text= performance[1], font=('MS',10,"bold")).grid(row=list(student_results.keys()).index(student)+5, column=2)

	def createButtons(self):
		butView = Button(self, text='View Individual Results',font=('MS', 10,'bold'), command = self.openResultsWindow)
		butView.grid(row=15, column=1) 		
	def openResultsWindow(self):
		root1 = Toplevel(self)
		DisplayResults(root1, student_and_results)

class DisplayResults(Frame):
    def __init__(self,master, student_result):
        Frame.__init__(self,master)
        self.grid()
        self.createPage(student_result)
    def createPage(self, student_result):
    	Label(self, width="15", height="2").grid(row=0, column=0)
    	Label(self, text="Results for %s"%filename1[:-7], font=('MS',10,"bold")).grid(row=0, column=3, columnspan = 5)
    	Label(self, text="Student", font=('MS',10,"bold")).grid(row=2, column=0)
    	for student,performance in student_result.items():
            Label(self, text=student, font=('MS',10,"bold")).grid(row= list(student_result.keys()).index(student)+5, column=0)
            for i in range(0,10):
                Label(self, text=("Q" + str(i+1) + "\t"), font=('MS',10,"bold")).grid(row=2, column=i+1)
                if int(performance[i]) == 1:
                    Label(self, text=('✔' + '\t'), font=('MS',10,"bold")).grid(row=list(student_result.keys()).index(student)+5, column=i+1)
                else:
                    Label(self, text=('✘' + '\t'), font=('MS',10,"bold")).grid(row=list(student_result.keys()).index(student)+5, column=i+1)
 


root = Tk()
root.title("Summative Assessment")
app = ChooseTest(root)
root.mainloop()
