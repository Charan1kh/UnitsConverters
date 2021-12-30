# import required modules
from tkinter import *
import tkinter as tk
from tkinter.ttk import Progressbar
from time import sleep
import webbrowser

# create converter class.
class converter():
	# constructor
	def __init__(self,unit):

		win.deiconify()
		
		# win.geometry("350x500")
		win.resizable(0,0)
		win.title("Converter")
		icon=PhotoImage(file=r'convert.png')
		win.iconphoto(False,icon)

		# Calling Center function to
		# center the window.
		center(win,350,500)
		
		# Assigning Current Unit,
		# to the converter,
		# selected by user.
		self.unit=unit

		# Input Part of the window(Top Half).
		upr=Label(win,bg="#add8e6",
				width=400,height=250)
		upr.place(x=0,y=0)

		# Output Part of the
		# window(Bottom Half).
		lwr=Label(win,bg="#189AB4",
				width=400,height=250
				,bd=0)
		lwr.place(x=0,y=250)

		# Hamburger Menu which contains
		# the available conversion options.
		self.menu_lb=Listbox(win,selectmode=SINGLE,
							height=0,font=("Helvetica",10))
		# Binding event to select
		# the option from ListBox.
		self.menu_lb.bind('<>',self.option)
		
		#Loading hamburger menu with options.
		options=["","","Length","Temperature",
				"Speed","Time","Mass"]
		
		for i in range(len(options)):
			self.menu_lb.insert(i,options[i])


		# Hamburger menu icon
		self.pic=PhotoImage(file=r"menu.png")
		self.menu=Button(win,image=self.pic,width=35,
						height=30,bg="#add8e6",bd=0,
						command=lambda:self.select('m'))
		self.menu.place(x=0,y=0)
		
		# Input Entry to take the user input.
		self.inp_stg=StringVar()
		self.inp=Entry(win,bg="#add8e6",fg="white",
					font=("Helvetica",14),
					text=self.inp_stg,bd=1)
		self.inp.place(x=120,y=100,width=116,
					height=40)
		self.inp.bind('',self.operation)
		self.inp.bind('',self.operation)

		# Loading the sub-menu box.
		self.lb_menu=unit["lb"]

		# Input Listbox(i.e., Meter etc)
		self.lb=Listbox(win,selectmode=SINGLE,
						height=0)		
		self.lb.bind('<>',self.option)

		# Input Unit Display Label selected by customer.
		self.disp=Label(win,text=self.lb_menu[0],
						bg="white",fg="black")
		self.disp.place(x=120,y=160,width=100,
						height=20)

		# DownArrow Button to Activate Listbox sub-menu to selection conversion units.
		self.down=PhotoImage(file=r"down.png")
		scroll_upr=Button(win,image=self.down,
						width=14,height=18,bd=0,
						command=lambda:self.select(0))
		scroll_upr.place(x=220,y=160)

		# Output Entry to display the output.
		self.opt_stg=StringVar()
		
		self.opt=Entry(win,bg="#189AB4",fg="black",
					font=("Helvetica",14),
					text=self.opt_stg,bd=1)
		
		self.opt.place(x=120,y=350,width=116,
					height=40)
		self.opt.bind('',self.operation)


		self.lb1=Listbox(win,selectmode=SINGLE,
						height=0)
		self.lb1.bind('<>',self.option)
		
		for i in range(len(self.lb_menu)):
			self.lb1.insert(i,self.lb_menu[i])
			self.lb.insert(i,self.lb_menu[i])	

		# Output unit display.
		self.disp1=Label(win,text=self.lb_menu[1],
						bg="#ffffff",fg="black")
		self.disp1.place(x=120,y=410,width=100,
						height=20)

		# Button to open sub-menu list.
		scroll_dwn=Button(win,image=self.down,
						width=14,height=18,bd=0,
						command=lambda:self.select(1),
						bg="#f5f5f5")
		
		scroll_dwn.place(x=220,y=410)

		# To display the formulae used
		# to convert the current units.
		# StringVar() to update the input
		# and output entry fields after
		# every keystroke.
		self.form=StringVar()
		self.formulae=Label(win,text="",bg="#189AB4",
							fg="white",
							font=("Helvetica",10))
		self.formulae.place(x=50,y=450,width=250,
							height=25)

		# Current position of I/P and O/P
		# sub-menu is stored in a dictionary
		# and accessed through the dictionary.
		self.para=unit["para"]
		self.para1=unit["para1"]

		#print(self.para,self.para1)

	# After shifting from parameter to
	# other paramter(i.e., From length
	# to Mass) we need reset and assign
	# the converter class with
	#respective inputs and outputs.	
	def set_unit(self,unit):
		global exp_in,exp_out
		
		# Input Expression.
		exp_in=""
		
		# Output Expression.
		exp_out=""
		
		# Input StringVar()
		self.inp_stg.set("")
		
		# Output StringVar()
		self.opt_stg.set("")
		
		# Current Parameter(i.e.,Length,Mass etc.)
		self.unit=unit
		
		# Accessing the position of unit display
		# label position through dictionary
		self.lb_menu=unit["lb"]
		
		# Deleting Input Listbox to assign
		# the current parameter values.
		self.lb.delete(0,END)
		
		# Deleting Output Listbox
		# to assign the current
		# parameter values
		self.lb1.delete(0,END)

		self.lb.place(y=0,height=0)
		self.lb1.place(y=250,height=0)

		# Initialising the unit display
		# label with initial unit
		# (i.e.,Tonne,Kilogram)
		self.disp['text']=self.lb_menu[0]
		self.disp1['text']=self.lb_menu[1]

		# Changing the length and
		# position of Listbox(Sub-Menu)
		# according to the length
		# of the list
		self.para=unit["para"]
		self.para1=unit["para1"]

		# Appending Options of the
		# list to Listbox.
		for i in range(len(self.lb_menu)):
			self.lb1.insert(END,self.lb_menu[i])
			self.lb.insert(i,self.lb_menu[i])

		# Clearing the formulae Label
		# after changing to another
		# parameter.
		self.formulae['text'] = "Formulae: "
					+ operator.replace("{}",
						"Unit")

		# Centering the window.
		center(wind,500,230)
		win.update()

	# Performs Operation by taking
	# user input(Value and unit
	# to be converted).
	def operation(self,event):	
		
		global exp_in,operator,exp_out

		# Taking Input and Output
		# Units to convert from display.
		self.inp_unit = self.disp['text']
		self.opt_unit = self.disp1['text']
	
		try:
		# We can access the widget
		# by the checking the place /
		# position of event occurence.
			widget = event.widget
		
			if(widget == self.inp):
				win.update()

				# Retrieving the operator stored
				# in dictionary using unit
				# display label.
				index = self.unit[self.opt_unit][-1]
				operator = self.unit[self.inp_unit][index]
				# print("exp: ",operator,exp_in)

				# As this is a unit converter
				# we don't need characters so
				# we are checking for numbers itself.
				if(event.char >= '0' and event.char <= '9'):
					exp_in = self.inp_stg.get()
					
					#Taking the value after every
					# keystroke and updating
					# the output
					exp_out = str(eval(operator.format(exp_in)))
					self.opt_stg.set(exp_out)
				
				elif((event.char=='\b') or
					(len(self.inp_stg.get())=='0'
					and event.char<='9')):
					exp_out = self.opt_stg.get()
					exp_in = str(eval(operator.format(exp_out)))
					self.inp_stg.set(exp_in)
					
				elif(event.char == '\b' or
					(len(self.opt_stg.get())
