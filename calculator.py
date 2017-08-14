# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 12:56:59 2017

@author: princess
"""
from tkinter import *

master=Tk()
display = Entry(master,width=11, justify='right', bd=0, bg='lightgrey')

master.title("Calculator")

class Calculator:
   # def init is an object creates five variables 
    def __init__(self):
        self.var1=""
        self.var2=""
        self.result=0      # result of last equation
        self.current=0       #Numbeer your on 
        self.operator=0      #number of operator
        
    def numb_butt(self, index): # numb butt button method takes the index as aparameter and add it to the proper variable 
        if self.current is 0:
            self.var1=str(self.var1)+str(index)
            display.delete(0, END)
            display.insert(0, string=self.var1)
        else:
            self.var2 = str(self.var2) + str(index)
            display.delete(0, END)
            display.insert(0, string=self.var2)
            
    def equate(self):  # def equate finds out what operator your using and add subtract multiply or divide based on that, updates the display 
        if self.operator is 0:
            self.result = float(self.var1) + float(self.var2)
        elif self.operator is 1:
            self.result = float(self.var1) - float(self.var2)
        elif self.operator is 2:
           self.result = float(self.var1) * float(self.var2)
        elif self.operator is 3:
            self.result = float(self.var1) / float(self.var2)
            display.delete(0, END)
            display.insert(0, string=self.result)
            
    def set_op(self, op):  # def set op sets operator equal to input clears screen and sets the current to the right variable.. if not =0, claers variable 2
        self.operator = op
        display.delete(0, END)
        if self.current is 0:
            self.current = 1
        else:
            self.equate()
            self.var2 = ""
           
    def claear(self):   # clear a method  reseting everything and clear the screen
        self.__init__()
        display.delete(0, END)
            
calc = Calculator()

b0= Button(master, text="0", command=lambda: calc.mumb_butt(0))
b1= Button(master, text="1", command=lambda: calc.mumb_butt(1))
b2= Button(master, text="2", command=lambda: calc.mumb_butt(2))
b3= Button(master, text="3", command=lambda: calc.mumb_butt(3))
b4= Button(master, text="4", command=lambda: calc.mumb_butt(4))
b5= Button(master, text="5", command=lambda: calc.mumb_butt(5))
b6= Button(master, text="6", command=lambda: calc.mumb_butt(6))
b7= Button(master, text="7", command=lambda: calc.mumb_butt(7))
b8= Button(master, text="8", command=lambda: calc.mumb_butt(8))
b9= Button(master, text="9", command=lambda: calc.mumb_butt(9))
  
            
            