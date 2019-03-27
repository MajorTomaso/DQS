import csv
from tkinter import *
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

class DisplayResults(Frame):

	def __init__(self,master):

		Frame.__init__(self,master)
		self.pack()
		self.retrieveResponse()
		self.createButtons()

	def retrieveResponse(self):

		self.txtDisplay = Text(self, height = 15, width=90)
		self.txtDisplay.tag_configure('boldfont', font=('MS', 8, 'bold'))
		self.txtDisplay.tag_configure('normfont', font=('MS',8))

		tabs = ""
		tabs += ("\t" + "\t" + "\t" + "\t" + "\t")
		self.txtDisplay.insert(END, "Student" + tabs + "Mark/Grade" + tabs + "Pass/Fail\n")

		for student,performance in student_results.items():
			self.txtDisplay.insert(END, student + tabs + performance[0] +"%" + tabs + performance[1] + "\n")

		self.txtDisplay.insert(END, "\n\nSummary of all marks" + tabs + str(summary) +"%" )
		self.txtDisplay['state'] = DISABLED
		self.txtDisplay.pack()

	def createButtons(self):
		button_invidivual = Button(self, text="View Individual Results", font = ('MS', 8, 'bold'))
		button_invidivual['command'] = self.openResultsWindow
		button_invidivual.pack()
	def openResultsWindow(self):
		t1 = Toplevel(root)
		showIndResults(t1)

class showIndResults(Frame):	
	def __init__(self,master):
		Frame.__init__(self,master)
		self.pack()
		self.showResults()
	def showResults(self):
		self.txtDisplay = Text(self, height = 15, width=95)
		self.txtDisplay.tag_configure('boldfont', font=('MS',8, 'bold'))
		self.txtDisplay.tag_configure('normfont', font=('MS',8))

		self.txtDisplay.insert(END, "Student\t" + "\tQ1" + "\tQ2" + "\tQ3" + "\tQ4" + "\tQ5" + "\tQ6" + "\tQ7" + "\tQ8" + "\tQ9" + "\tQ10\n")
		a = 0
		for i in student_questions:
			for k in i:
				if a % 11 == 0:
					self.txtDisplay.insert(END, k + "\t\t")
				else:
					self.txtDisplay.insert(END, k + "\t")
				a+=1



		self.txtDisplay['state'] = DISABLED
		self.txtDisplay.pack()


#Main
root = Tk()
root.title("Summative Assessment")
app = DisplayResults(root)
root.mainloop()
