import csv
from tkinter import *
Q1Sum = 0
Q2Sum = 0
Q3Sum = 0
Q4Sum = 0
Q5Sum = 0
Q6Sum = 0
Q7Sum = 0
Q8Sum = 0
Q9Sum = 0
Q10Sum =0
with open('FormativeResults.csv') as all_results:
	all_results = csv.reader(all_results)
	next(all_results,None)
	number_of_attempts = 0
	for row in all_results:
		Q1Sum += int(row[0])
		Q2Sum += int(row[1])
		Q3Sum += int(row[2])
		Q4Sum += int(row[3])
		Q5Sum += int(row[4])
		Q6Sum += int(row[5])
		Q7Sum += int(row[6])
		Q8Sum += int(row[7])
		Q9Sum += int(row[8])
		Q10Sum += int(row[9])
		number_of_attempts += 1
all_questions_sum = [Q1Sum,Q2Sum,Q3Sum,Q4Sum,Q5Sum,Q6Sum,Q7Sum,Q8Sum,Q9Sum,Q10Sum]
least_often_answered = all_questions_sum.index(min(all_questions_sum)) + 1
def perc(sumcorrect):
	global number_of_students
	percentage = sumcorrect/number_of_attempts*100
	return round(percentage,1)
class DisplayResults(Frame):

	def __init__(self,master):

		Frame.__init__(self,master)
		self.pack()
		self.retrieveResponse()
		# self.createButtons()

	def retrieveResponse(self):

		self.txtDisplay = Text(self, height = 15, width=90)
		self.txtDisplay.tag_configure('boldfont', font=('MS', 8, 'bold'))
		self.txtDisplay.tag_configure('normfont', font=('MS',8))
		self.txtDisplay.insert(END, "\t\tNUMBER OF TIMES A QUESTION WAS ANSWERED CORRECTLY\n\n")
		self.txtDisplay.insert(END, "\tQ1\tQ2\tQ3\tQ4\tQ5\tQ6\tQ7\tQ8\tQ9\tQ10\n")
		self.txtDisplay.insert(END, "\t" + str(Q1Sum) + "\t" + str(Q2Sum)+ "\t" + str(Q3Sum) + "\t" + str(Q4Sum) + "\t" + str(Q5Sum) + "\t" + str(Q6Sum) + "\t" + str(Q7Sum) + "\t" + str(Q8Sum) + "\t" + str(Q9Sum) + "\t" + str(Q10Sum) + "\n\n")
		
		self.txtDisplay.insert(END, "\t\t PERCENTAGE OF TIME A QUESTION WAS ANSWERED CORRECTLY\n\n")
		self.txtDisplay.insert(END, "\tQ1\tQ2\tQ3\tQ4\tQ5\tQ6\tQ7\tQ8\tQ9\tQ10\n")
		self.txtDisplay.insert(END, "\t" + str(perc(Q1Sum)) + "%\t" + str(perc(Q2Sum))+ "%\t" + str(perc(Q3Sum)) + "%\t" + str(perc(Q4Sum)) + "%\t" + str(perc(Q5Sum)) + "%\t" + str(perc(Q6Sum)) + "%\t" + str(perc(Q7Sum)) + "%\t" + str(perc(Q8Sum)) + "%\t" + str(perc(Q9Sum)) + "%\t" + str(perc(Q10Sum)) + "%\n\n")
		
		self.txtDisplay.insert(END, "The question most often answered incorrectly: Question" + str(least_often_answered))

		self.txtDisplay.insert(END, "\nNumber of total attempts: " + str(number_of_attempts))

		self.txtDisplay['state'] = DISABLED
		self.txtDisplay.pack()


#Main
root = Tk()
root.title("Formative Assessment")
app = DisplayResults(root)
root.mainloop()