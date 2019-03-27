from tkinter import *

class introPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()

        self.createPage()

    def createPage(self):
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
        answerPage(ansroot)
        root.withdraw()

class answerPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.answer()

    def answer(self):
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

        butView = Button(self, text='Close',font=('MS', 10,'bold'), command = self.close)
        butView.grid(row=21, column=0, sticky=E)

    def close(self):
        root.destroy()

root = Tk()
root.title("Summative Answers")
app = introPage(root)
root.mainloop()
