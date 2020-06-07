import tkinter as tk
from tkinter import *
from tkinter import ttk

class ButtonClick:
	def __init__(self):
		pass

	def btn1(self):
		pass

class Calculator:

	def __init__(self, master):
		self.master = master.title("Python Math Calculator")

		self.frame1 = Frame(master, bg="red")
		self.frame1.grid(row=3, column=0, pady=2)

		self.sec_frame = Frame(master, bg="blue")
		self.sec_frame.grid(row=2, column=0)

		self.on_off = IntVar()

		self.screen = Text(master, state=DISABLED, width=47, height=3, font=("Poor Richard", 13))
		self.screen.grid(row=1, column=0, pady=10, columnspan=1, padx=36)

	def calculate_ques(self):
		word = self.screen.get(1.0, END)
		# addition level
		if "+" in word:
			try:
				ind = word.index("+")
				side1 = word[0:ind]
				new = ind+1
				side2 = word[new:-1]
				total = eval(side1)+eval(side2)
				print(total)
				self.screen.configure(state=NORMAL)
				self.screen.delete(1.0, END)
				self.screen.insert(1.0, f"{total}")
				self.screen.configure(state=DISABLED)
			except:
				self.screen.configure(state=NORMAL)
				self.screen.delete(1.0, END)
				self.screen.insert(1.0, "Error")
				self.screen.configure(state=DISABLED)
				# addition level
		if "*" in word:
			try:
				ind = word.index("*")
				side1 = word[0:ind]
				new = ind+1
				side2 = word[new:-1]
				product = eval(side1)*eval(side2)
				print(product)
				self.screen.configure(state=NORMAL)
				self.screen.delete(1.0, END)
				self.screen.insert(1.0, f"{product}")
				self.screen.configure(state=DISABLED)
			except:
				self.screen.configure(state=NORMAL)
				self.screen.delete(1.0, END)
				self.screen.insert(1.0, "Error")
				self.screen.configure(state=DISABLED)


		if "/" in word:
			try:
				ind = word.index("/")
				side1 = word[0:ind]
				new = ind+1
				side2 = word[new:-1]
				divide = eval(side1) / eval(side2)
				print(divide)
				print(side1, side2)
				new_divide = round(divide, 3)
				self.screen.configure(state=NORMAL)
				self.screen.delete(1.0, END)
				self.screen.insert(1.0, f"{new_divide}")
				self.screen.configure(state=DISABLED)
			except:
				self.screen.configure(state=NORMAL)
				self.screen.delete(1.0, END)
				self.screen.insert(1.0, "Error")
				self.screen.configure(state=DISABLED)		

		if "-" in word:
			try:
				ind = word.index("-")
				side1 = word[0:ind]
				new = ind+1
				side2 = word[new:-1]
				minus = eval(side1) - eval(side2)
				self.screen.configure(state=NORMAL)
				self.screen.delete(1.0, END)
				self.screen.insert(1.0, f"{minus}")
				self.screen.configure(state=DISABLED)
			except:
				self.screen.configure(state=NORMAL)
				self.screen.delete(1.0, END)
				self.screen.insert(1.0, "Error")
				self.screen.configure(state=DISABLED)




	def btn0(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "0")
		self.screen.configure(state=DISABLED)

	def btn1(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "1")
		self.screen.configure(state=DISABLED)

	def btn2(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "2")
		self.screen.configure(state=DISABLED)

	def btn3(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "3")
		self.screen.configure(state=DISABLED)

	def btn4(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "4")
		self.screen.configure(state=DISABLED)

	def btn5(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "5")
		self.screen.configure(state=DISABLED)

	def btn6(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "6")
		self.screen.configure(state=DISABLED)

	def btn7(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "7")
		self.screen.configure(state=DISABLED)

	def btn8(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "8")
		self.screen.configure(state=DISABLED)

	def btn9(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "9")
		self.screen.configure(state=DISABLED)

	def btnPoint(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, ".")
		self.screen.configure(state=DISABLED)


	def btnMU(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "*")
		self.screen.configure(state=DISABLED)

	def btnM(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "-")
		self.screen.configure(state=DISABLED)

	def btnA(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "+")
		self.screen.configure(state=DISABLED)

	def btnD(self):
		self.screen.configure(state=NORMAL)
		self.screen.insert(END, "/")
		self.screen.configure(state=DISABLED)



	def clear_text(self):
		self.screen.configure(state=NORMAL)
		self.screen.delete(1.0, END)
		self.screen.configure(state=DISABLED)

	def on_calc(self):
		self.button0.configure(state=NORMAL)
		self.button1.configure(state=NORMAL)
		self.button2.configure(state=NORMAL)
		self.button3.configure(state=NORMAL)
		self.button4.configure(state=NORMAL)
		self.button5.configure(state=NORMAL)
		self.button6.configure(state=NORMAL)
		self.button7.configure(state=NORMAL)
		self.button8.configure(state=NORMAL)
		self.button9.configure(state=NORMAL)
		self.button_mul.configure(state=NORMAL)
		self.button_plus.configure(state=NORMAL)
		self.button_min.configure(state=NORMAL)
		self.button_calc.configure(state=NORMAL)
		self.button_div.configure(state=NORMAL)
		self.button_clr_all.configure(state=NORMAL)
		self.button_point.configure(state=NORMAL)
		self.off.configure(state=NORMAL)
		self.on.configure(state=DISABLED)

	def off_calc(self):
		self.button0.configure(state=DISABLED)
		self.button1.configure(state=DISABLED)
		self.button2.configure(state=DISABLED)
		self.button3.configure(state=DISABLED)
		self.button4.configure(state=DISABLED)
		self.button5.configure(state=DISABLED)
		self.button6.configure(state=DISABLED)
		self.button7.configure(state=DISABLED)
		self.button8.configure(state=DISABLED)
		self.button9.configure(state=DISABLED)
		self.button_mul.configure(state=DISABLED)
		self.button_plus.configure(state=DISABLED)
		self.button_min.configure(state=DISABLED)
		self.button_calc.configure(state=DISABLED)
		self.button_div.configure(state=DISABLED)
		self.button_clr_all.configure(state=DISABLED)
		self.button_point.configure(state=DISABLED)
		self.screen.configure(state=NORMAL)
		self.screen.delete(1.0, END)
		self.screen.configure(state=DISABLED)
		self.off.configure(state=DISABLED)
		self.on.configure(state=NORMAL)

	def init_window(self, width=10, height=3, fgcolor="white", bgcolor="black", bdtype=0):
		self.width = width
		self.height = height
		self.fgcolor = fgcolor
		self.bgcolor = bgcolor
		self.bdtype = bdtype

		self.on_off.set(1)

		self.on = Radiobutton(self.sec_frame, text="ON", var=self.on_off, value=1, bd=6, fg="black", bg="red", command=self.on_calc, state=DISABLED)
		self.on.grid(row=0, column=0)

		self.off = Radiobutton(self.sec_frame, text="OFF", var=self.on_off, value=2, bd=6, fg="black", bg="red", command=self.off_calc)
		self.off.grid(row=0, column=1)

		self.button1 = Button(self.frame1, text="1", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btn1)
		self.button1.grid(row=0, column=0, padx=2, pady=2)

		self.button2 = Button(self.frame1, text="2", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btn2)
		self.button2.grid(row=0, column=1)

		self.button3 = Button(self.frame1, text="3", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btn3)
		self.button3.grid(row=0, column=2, padx=2)

		self.button_mul = Button(self.frame1, text="*", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btnMU)
		self.button_mul.grid(row=0, column=3, padx=2)

		self.button4 = Button(self.frame1, text="4", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btn4)
		self.button4.grid(row=1, column=0, pady=2)

		self.button5 = Button(self.frame1, text="5", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btn5)
		self.button5.grid(row=1, column=1)

		self.button6 = Button(self.frame1, text="6", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btn6)
		self.button6.grid(row=1, column=2)

		self.button_plus = Button(self.frame1, text="+", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btnA)
		self.button_plus.grid(row=1, column=3)

		self.button7 = Button(self.frame1, text="7", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btn7)
		self.button7.grid(row=2, column=0)

		self.button8 = Button(self.frame1, text="8", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btn8)
		self.button8.grid(row=2, column=1)

		self.button9 = Button(self.frame1, text="9", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btn9)
		self.button9.grid(row=2, column=2)

		self.button_min = Button(self.frame1, text="-", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btnM)
		self.button_min.grid(row=2, column=3)

		self.button0 = Button(self.frame1, text="0", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btn0)
		self.button0.grid(row=3, column=0, pady=3)

		self.button_div = Button(self.frame1, text="/", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btnD)
		self.button_div.grid(row=3, column=3)

		self.button_point = Button(self.frame1, text=".", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.btnPoint)
		self.button_point.grid(row=3, column=2)

		self.button_clr_all = Button(self.frame1, text="CE", bg=self.bgcolor, fg=self.fgcolor, font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=self.width, height=self.height, command=self.clear_text)
		self.button_clr_all.grid(row=3, column=1)

		self.button_calc = Button(self.frame1, text="=", bg="black", fg="white", font=("Lucida Sans Unicode", 13), bd=self.bdtype, width=26, height=2, command=self.calculate_ques)
		self.button_calc.grid(row=4, column=0, pady=2, columnspan=4)


	








def main():
	root = tk.Tk()
	root.configure(bg="#000000")
	root.resizable(width=False, height=False)
	root.geometry("500x510")
	mygui = Calculator(root)
	Calculator(root).init_window()
	root.mainloop()

if __name__ == "__main__":
	main()