# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:56:08 2024

@author: yashd
"""
marks = [] 
def calculate_marks(marks):
    total_marks = sum(marks)
    average_marks = int(total_marks / 20)
    return average_marks

for i in range (1,21):
    marks = list(input("Enter the marks of students : "))
    marks.append(marks)
    
minimum = min(marks)
maximum = max(marks)  
  
print(" Minimum marks are :",minimum )    
print(" Maximun marks are :",maximum ) 
print(" Average marks are :",calculate_marks)

###################################################



marks = [] 
def calculate_marks(marks):
    total_marks = sum(marks)
    average_marks = int(total_marks / 20)
    return average_marks

for i in range (1,21):
    element=marks
    marks = list(input("Enter the marks of students : "))
    element.append(marks)
    
minimum = min(marks)
maximum = max(marks)  
  
print(" Minimum marks are :",minimum )    
print(" Maximun marks are :",maximum ) 
print(" Average marks are :",calculate_marks)
















