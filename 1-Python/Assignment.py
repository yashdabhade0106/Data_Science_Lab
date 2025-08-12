# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:58:24 2024

@author: yash
"""
# Question No 1
x = """ Ms.Jane H. Das 
   40 Theater Street 
   Sun City, AZ 85351
   USA"""
print(x)

# Question No 2
a = float(input("Enter the width of room in meter: "))
b = float(input("Enter the length of room in meter: "))
Area = a*b
print(f"Area of room is : {Area} meter")

# Question No 3
a = float(input("Enter the width of feild in feet : "))
b = float(input("Enter the length of feild in feet : "))
Area = (a*b)/43560
print(f"Area of feild is : {Area} acres")

# Question No 4
x=""" Drink containers holding one liter or
 less have a $0.10 deposit, and drink containers 
 holding more than one liter have a $0.25 deposit"""
print(x)
a=int(input("Enter the number of drink containers having 1 liter or less :"))
b=int(input("Enter the number of drink containers having more than 1 liter  :"))
c=a*0.10
d=b*0.25
e=c+d
print(f"Your total depost is {e} $")

# Question No 5
x=float(input("Enter the Meal amount : "))
local_tax = x*(5/100)
tip = x*(18/100)
Grand_total = (x+local_tax + tip)
print(f"Your tax amount is {local_tax},your tip is {tip} And grand total is {Grand_total}")

# Question No 6
height = float(input("Enter your height in feet : "))
height_inches=(height*12)
height_centimeter = ( height*100)
print(f"Height in inches {height_inches:.2f}")
print(f"Height in inches {height_centimeter:.2f}")



