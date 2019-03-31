import csv
import os
from tkinter import *
import tkinter.messagebox
import collections
student_results = {}
sum_all_percentages = 0
number_of_students = 0
student_questions = []
with open('SummativeResults.csv') as all_results:
	all_results = csv.reader(all_results)
	next(all_results,None)
	for row in all_results:
		student_results[row[0]] = [row[i] for i in range(11, 13)]
		sum_all_percentages += float(row[11])
		number_of_students += 1
		student_questions.append([row[i] for i in range(0,11)])
summary = round(sum_all_percentages/number_of_students,2)


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
		global student_and_results
		student_and_results = []
		with open('SummativeResults.csv') as all_results:
			all_results = csv.reader(all_results)
			next(all_results,None)
			for row in all_results:
				if row[0] == filename:
					student_results[row[1]] = [row[i] for i in range(12, 14)]
					student_and_results.append(row[1])
					sum_all_percentages += float(row[12])
					number_of_students += 1
					student_questions.append([row[i] for i in range(2,12)])
					student_and_results.append([row[i] for i in range(2,12)])
					summary = round(sum_all_percentages/number_of_students,2)
			student_results = collections.OrderedDict(student_results)
			print(student_results)
			print(student_and_results)
			lblGrid= Label(self, width = "15", height = "5")
			lblGrid.grid(row=0, column=0)
			tabs = "\t\t\t\t"
			Label(self, text = "Results for %s "%filename[:-7]  , font=('MS', 10, 'bold')).grid(row=0, column=1)
			Label(self, text=("Student" + tabs + "Mark" + tabs + "Pass/Fail"), font=('MS',10,"bold")).grid(row=1, column=0, columnspan = 7)
			for student,performance in student_results.items():
				Label(self, text=(student + tabs + performance[0] + tabs + performance[1]) , font=('MS',10,"bold")).grid(row=list(student_results.keys()).index(student) +5,column=0, columnspan=6)
	def createButtons(self):
		butView = Button(self, text='View Individual Results',font=('MS', 10,'bold'), command = self.openResultsWindow)
		butView.grid(row=15, column=1) 		
	def openResultsWindow(self):
 		t1 = Toplevel(self)
 		DisplayResults(student_and_results)

class DisplayResults(Frame):
    def __init__(self, student_result):
        Frame.__init__(self)
        self.grid()
        self.createPage(student_result)
    def createPage(self, student_result):
            pass








# class DisplayResults(Frame):

# 	def __init__(self,master):

# 		Frame.__init__(self,master)
# 		self.pack()
# 		self.retrieveResponse()
# 		self.createButtons()

# 	def retrieveResponse(self):

# 		self.txtDisplay = Text(self, height = 15, width=90)
# 		self.txtDisplay.tag_configure('boldfont', font=('MS', 8, 'bold'))
# 		self.txtDisplay.tag_configure('normfont', font=('MS',8))

# 		tabs = ""
# 		tabs += ("\t" + "\t" + "\t" + "\t" + "\t")
# 		self.txtDisplay.insert(END, "Student" + tabs + "Mark/Grade" + tabs + "Pass/Fail\n")

# 		for student,performance in student_results.items():
# 			self.txtDisplay.insert(END, student + tabs + performance[0] +"%" + tabs + performance[1] + "\n")

# 		self.txtDisplay.insert(END, "\n\nSummary of all marks" + tabs + str(summary) +"%" )
# 		self.txtDisplay['state'] = DISABLED
# 		self.txtDisplay.pack()

# 	def createButtons(self):
# 		button_invidivual = Button(self, text="View Individual Results", font = ('MS', 8, 'bold'))
# 		button_invidivual['command'] = self.openResultsWindow
# 		button_invidivual.pack()
# 	def openResultsWindow(self):
# 		t1 = Toplevel(root)
# 		showIndResults(t1)

# class showIndResults(Frame):	
# 	def __init__(self,master):
# 		Frame.__init__(self,master)
# 		self.pack()
# 		self.showResults()
# 	def showResults(self):
# 		self.txtDisplay = Text(self, height = 15, width=95)
# 		self.txtDisplay.tag_configure('boldfont', font=('MS',8, 'bold'))
# 		self.txtDisplay.tag_configure('normfont', font=('MS',8))

# 		self.txtDisplay.insert(END, "Student\t" + "\tQ1" + "\tQ2" + "\tQ3" + "\tQ4" + "\tQ5" + "\tQ6" + "\tQ7" + "\tQ8" + "\tQ9" + "\tQ10\n")
# 		a = 0
# 		for i in student_questions:
# 			for k in i:
# 				if a % 11 == 0:
# 					self.txtDisplay.insert(END, k + "\t\t")
# 				else:
# 					self.txtDisplay.insert(END, k + "\t")
# 				a+=1



# 		self.txtDisplay['state'] = DISABLED
# 		self.txtDisplay.pack()


# #Main
root = Tk()
root.title("Summative Assessment")
app = ChooseTest(root)
root.mainloop()
