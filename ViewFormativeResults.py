import csv
from tkinter import *
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

        self.listTest.grid(row=0, column=1)
        scroll.grid(row=0, column=4, sticky=W)

        butSelect = Button(self, text='Select',font=('MS', 10,'bold'), command = self.Select)
        butSelect.grid(row=2, column=1, sticky=E)

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
    	global rootSum
    	rootSum = Toplevel(self)
    	index = self.listTest.curselection()[0]
    	strName = str(self.listTest.get(index))
    	global filename1
    	filename1 = strName
    	root.destroy()
    	DisplayResults(strName)
class DisplayResults(Frame):
	def __init__(self, filename):
		Frame.__init__(self)
		self.grid()
		self.createPage(filename)
		# self.createButtons()
	def createPage(self,filename):
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
				if row[0] == filename:
					Q1Sum += int(row[1])
					Q2Sum += int(row[2])
					Q3Sum += int(row[3])
					Q4Sum += int(row[4])
					Q5Sum += int(row[5])
					Q6Sum += int(row[6])
					Q7Sum += int(row[7])
					Q8Sum += int(row[8])
					Q9Sum += int(row[9])
					Q10Sum += int(row[10])
					number_of_attempts += 1
		def perc(sumcorrect, number_of_attempts):
			try:
				percentage = sumcorrect/number_of_attempts*100
				return round(percentage,1)
			except:
				return 0
		all_questions_sum = [Q1Sum,Q2Sum,Q3Sum,Q4Sum,Q5Sum,Q6Sum,Q7Sum,Q8Sum,Q9Sum,Q10Sum]
		least_often_answered = all_questions_sum.index(min(all_questions_sum)) + 1
		Label(self, width="15", height="2").grid(row=0, column=0)
		Label(self, text="Results for %s"%filename[:-7], font=('MS',12,"bold")).grid(row=0, column=3, columnspan=5)
		Label(self, text="NUMBER OF TIMES A QUESTION WAS ANSWERED CORRECTLY",font=('MS',11)).grid(row=1, column=2, columnspan=8)
		Label(self, text="PERCENTAGE OF TIMES A QUESTION WAS ANSWERED CORRECTLY",font=('MS',11)).grid(row=6, column=2, columnspan=8)
		for i in range(0,10):
			Label(self, text=("Q" + str(i+1) +"\t"), font=('MS',10,"bold")).grid(row=2, column=i+1,sticky="W")
			Label(self, text=all_questions_sum[i], font=('MS', 10, "bold")).grid(row=3, column=i+1,sticky="W")
			Label(self, text=("Q" + str(i+1) +"\t"), font=('MS',10,"bold")).grid(row=7, column=i+1,sticky="W")
			Label(self, text=str((perc(all_questions_sum[i], number_of_attempts)))+"%", font=('MS', 10, "bold")).grid(row=8, column=i+1,sticky="W")
		Label(self, text="The question most often answered incorrectly: Question" + str(least_often_answered)).grid(row=9, column=0, columnspan=5, sticky="W")
		Label(self, text="Number of total attempts: " + str(number_of_attempts)).grid(row=10, column=0, columnspan=5, sticky="W")





# #Main
root = Tk()
root.title("Formative Assessment")
app = ChooseTest(root)
root.mainloop()
