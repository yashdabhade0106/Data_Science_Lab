# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:19:48 2024

@author: yash

Advanced Python 
"""
lst = []
for num in range (0,20):
    lst.append(num)
print(lst)

# we can write same method using list comrehension 

lst = [num for num in range (0,20)]
print(lst)

###########################

names = ['dada','mama','kaka']
lst=[name.capitalize() for name in names ]
print(lst)

#list comrehension with if statement 
def is_even (num):
    return num%2 == 0
lst = [num for num in range (10) if is_even(num)]
print(lst)

# for loop in for loop using list comrehension

lst = [f"{x}{y}"for x in range (3) for y in range (3)]
print (lst)

#Dictionary comrehension 

dict = {x:x*x for x in range (3)}
print(dict)

#Generaator 
#It is a another way of creating iterators
# in a simple way where 
# it is uesd the keyword " yield "
#instead of returing it in a defined function 
# generators are implemented using a function

gen = (x for x in range (3))
print(gen)
for num in gen :
    print(num)

###########################
# gen = handle/reference 

gen = ( x for x in range (3))
next (gen)
next(gen)
#########################
# Function which returns multiple values

def range_even (end):
    for num in range (0,end,2):
        yield num
        
for num in range_even (6):
    print(num)

###########################
gen= range_even(6)
next(gen)
next(gen)
next(gen)

##############################
#Chaining generator

def lenghts(itr):
    for ele in itr :
        yield len(ele)

def hide (itr):
    for ele in itr :
        yield ele*'*'

'''
"ele*" appears to be a placeholder for an element from an iterable 
the asterisk (*) is likely just a charater used to 
represent a placeholder or a wildcard . for 
instance , if you are iterating over a list of elements , "ele*"
could symbolize any element in that list . 
It's a generic represntatipon that does'nt correspond to any specific 
syntax in python or itertools 

'''

passwords = ["not-good","give'm-pass","00100=100"]
for password in hide(lenghts(passwords)):
    print(password)

#########################

import random
noun=input("Enter a noun : ")
adjective=input(" enter a adjective : ")
special_char = input(" Enter a Special charater : ")
num = random.randrange(0,99)
password = [noun+adjective+special_char+str(num) ]
print(password)

def lenghts(password):
    for ele in password :
        yield len(ele)

def hide (password):
    for ele in password :
        yield ele*'*'
print(password)

####################################

#Enumerate
#printing list with index 
lst = ["milk","egg","bread"]
for index in range (len(lst)):
    print(f"{index++1} {lst[index]}")
    
##################################
#same code with implemented using enumerate 
lst = ["milk","egg","bread"]
for index,item in enumerate (lst,start=1):
    print(f"{index} {item}")

###############################
# use of zip function 
name = ["dada","mama","kaka"]
info = [9850,6032,9785]
for nm, inf in zip (name,info):
    print(nm,inf)

#################################
#use of zip function with mis match list 
name = ["dada","mama","kaka","baba"]
info = [9850,6032,9785]
for nm, inf in zip (name,info):
    print(nm,inf)
#it will not display excess mismatch item in name
#i.e baba

#############################
#zip_longest 

from itertools import zip_longest 
name = ["dada","mama","kaka","baba"]
info = [9850,6032,9785]
for nm, inf in zip_longest (name,info):
    print(nm,inf)

################################
# use of fill value instead none 
from itertools import zip_longest 
name = ["dada","mama","kaka","baba"]
info = [9850,6032,9785]
for nm, inf in zip_longest (name,info,fillvalue=0):
    print(nm,inf)

#####################################
# use of all(),if all the values are true 
#then it will produce output 
#value must be non zero , +ve or -ve
lst=[2,3,-6,8,9]
if all (lst):
    print("all values are true")
else:
    print("there are null values")    

##########################

lst=[2,3,0,8,9]
if all (lst):
    print("all values are true")
else:
    print("there are null values")  

#############################
#use of any if any one non zero values

lst=[0,0,0,-8,0,]
if any (lst):
    print(" It has some non zero value")
else:
    print("Useless")
#####################
#use of any 
lst=[0,0,0,0,0]
if any (lst):
    print(" It has some non zero value")
else:
    print("Useless")

#count()

from itertools import count 
counter = count()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

###########################
#now let us start from 1

from itertools import count 
counter = count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

############################
#cycle()
#suppose you have repeated tasks to be done then you 

import itertools 

instructions = ("Eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)

####################################
#repeat()

from itertools import repeat
for msg in repeat ("Keep Patience ",times=3):
  print(msg)

#########################
#combinations ()

from itertools import combinations
player = ["John","Jani","Janardhan"]
for i in combinations(player,2):
    print(i)
    
##############################

from itertools import combinations
player = ["John","Jani","Janardhan","Janta","Jay"]
for i in combinations(player,2):
    print(i)

#########################
# permutations()

from itertools import permutations
player = ["John","Jani","Janardhan"]
for seat in permutations(player,2):
    print(seat)

#product()

from itertools import product
team_a = ['Rohit','Pandya','Bumrah']
team_b = ['Virat','Dhoni','Sachin']
for pair in product(team_a,team_b):
    print(pair)

########################
''' 
In python, assignment statements (obj_b=obj_a)
do not creare real copies. It only creates a new vriable
with the same reference . so when you want to make actual copies 
of mutable objects (list,dict) and want to modify the copy without affecting
the original youy have to be careful.
for 'real' copies we can use the copy module
However for compound,nested objects


'''
#Assignment operation 
# This will only create a new vafriable with same reference.
list_a = [1,2,3,4,5]
list_b = list_a

list_a[0] = -10
print(list_a)
print(list_b)


""" 26 march 2024  """

#shallow copy 
#one level deep . modifying on level 1 does not affect
#use copy.copy()
import copy 
lst_a = [1,2,3,4,5]
lst_b = copy.copy(lst_a)

# not affects the other list
lst_b [0] = -10
print (lst_a)
print(lst_b)
 
#[1,2,3,4,5]
#[-10,2,3,4,5]
###############################

#But with nested objects, modifying on level 2 or deep copy 

lst_a = [[1,2,3,4,5],[6,7,8,9,10]]
lst_b = copy.copy(lst_a)

# Affects the other !
lst_a [0][0] = -10
print(lst_a)
print(lst_b)

#[[-10,2,3,4,5],[6,7,8,9,10]]
#[[-10,2,3,4,5],[6,7,8,9,10]]

#############################
#Deep copy 
#Full independent clones. use copy.deepcopy().
import copy 
lst_a = [[1,2,3,4,5],[6,7,8,9,10]]
lst_b = copy.deepcopy(lst_a)
# not affects the other 
lst_a [0][0] = -10
print(lst_a)
print(lst_b)

#[[-10,2,3,4,5],[6,7,8,9,10]]
#[[1,2,3,4,5],[6,7,8,9,10]]

###############################
#"C:/DataScience/1-Python/buzzers.csv.xls"
import pandas as pd
f1 = pd.read_csv('C:/DataScience/1-Python/buzzers.csv.xls')

#############################
#check for working directory
import os 
with open ('C:/DataScience/1-Python/buzzers.csv.xls') as raw_data:
    print(raw_data.read())
  
#############################
# Reading CSV as data as lists
import csv
with open ('C:/DataScience/1-Python/buzzers.csv.xls') as raw_data:
    for line in csv.reader(raw_data):
        print(line)
        
##############################
# Reading CSV as data as Dictionaries
import csv
with open ('C:/DataScience/1-Python/buzzers.csv.xls') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)

######################
#pre-requisite to decorator
def plus_one (number):
    number1 = number + 1 
    return number1
plus_one(5)


##############################
# Defining Function inside other function 
def plus_one (number):
    
    def add_one(number):
        number1 = number + 1 
        return number1
    
    result = add_one(number)
    return result
plus_one(4)

###########################
#Passing function as arguments
#to other Functions

    
def plus_one(number):
   result1 = number + 1 
   return result1

def function_call (function ):
    result=function(5)
    return result

function_call(plus_one)

############################
#Function returning other functions

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello=hello_function()
hello()

#Always remenber when you call hello_function()
#Need for decorators
import time
def calc_square(numbers):
    start=time.time()
    result = []
    for number in numbers :
        result.append(number*number)
    end = time.time()
    total_time=(end-start)*1000
    print(f"Total time for execution square is {total_time}")
    return result


def calc_cube(numbers):
    start=time.time()
    result = []
    for number in numbers :
        result.append(number*number*number)
    end = time.time()
    total_time=(end-start)*1000
    print(f"Total time for execution cube is {total_time}")
    return result

array = range (1,100000)
out_square= calc_square(array)
out_cube = calc_cube(array)




########################################
#27/03/2024
##########################################
## a python decorator is a function that takesin a function
# and returns it by adding some functionallity

def say_hi():
    return 'hello there'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
decorate=uppercase_decorator(say_hi)
decorate()

##########################
### however the python provides a much easier way 
## for us to apply decorators 
## we simply use the @ symbol before 
# the function we;d like to decorate
######################

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()

###########################################

## applying multiple decorators  to a single
# function. however the decorators will be applied
# in the order that we;ve called them 

def split_string(function):
    def wrapper():
        func =function()
        splitted_string=func.split()
        return splitted_string
    return wrapper
def uppercase_decorator(function):
    def wrapper():
        func = function()
        
        make_uppercase=func.upper()
        
        return make_uppercase
    return wrapper 
    
@split_string
@uppercase_decorator
@uppercase_decorator    
def say_hi():
    return 'hello there'
say_hi()
        ##################################
        
        
import time
def time_it(func):
    def wrapper(args,*kwargs):
        start=time.time()
        result = func(args,*kwargs)
        end = time.time()
        total_time = (end-start)*1000
        print(func.__name__+f"took {total_time} mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    
   result=[]
   for number in numbers:
      result.append(number*number)
   return result
  
@time_it
def calc_cube(numbers):
    
   result=[]
   for number in numbers:
      result.append(number*number*number)
   return result   

array=range(1,100000)
out_square = calc_square(array)
out_cube=calc_cube(array)
        
#################################
#Exception handling

try:
    numetr=50
    denom=int(input("enter the denominator"))
    quot=numetr/denom
    print(quot)
    print("division performed succesfully")
except ZeroDivisionError:
    print("this is divide by zero")

##################################
""" 28 march 2024 """

try:
    numetr=50
    denom=int(input("enter the denominator"))
    quot=numetr/denom
    print(quot)
    print("division performed succesfully")
except ZeroDivisionError:
    print("Denominator is ZERO is not allowed ")
except ValueError:
    print("Only INTEGERS should be entered")

################################
 # Handling exceptions without naming them 
 
try:
     numetr=50
     denom=int(input("enter the denominator"))
     quot=numetr/denom
     print(quot)
     print("division performed succesfully")
except ValueError:
     print("Only INTEGERS should be entered")
except:
    print(" OOPS ....... SOME EXCEPTION RAISED ")

###################################
# Handling exception using try......except...else

try:
    numetr=50
    denom=int(input("enter the denominator"))
    quot=numetr/denom
    print(quot)
    print("division performed succesfully")
except ZeroDivisionError:
    print("Denominator is ZERO is not allowed ")
except ValueError:
    print("Only INTEGERS should be entered")
else:
    print("The result of devision operation is ",quot)

##################################
# Handling exception using try...except...else...finally

try:
    numetr=50
    denom=int(input("enter the denominator"))
    quot=numetr/denom
    print(quot)
    print("division performed succesfully")
except ZeroDivisionError:
    print("Denominator is ZERO is not allowed ")
except ValueError:
    print("Only INTEGERS should be entered")
else:
    print("The result of devision operation is ",quot)
finally:
    print("OVER AND OUT !!!")

##########################
""" 29 march 2024 """

# Classes
class Human:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o
        
    def do_work(self):
        if self.occupation == "Tennis player":
         print(self.name,"plays tennis ")
        elif self.occupation == "actor":
         print(self.name," Shoots film ")   
         
    def speaks (self):
       print(self.name," Says how are you ? ")

tom = Human("tom_cruise","actor")
tom.do_work()
tom.speaks()

#########################
class Vehicle:
    def general_usage(self):
        print(" General use : transporation ")
        
class Car (Vehicle):
    def __init__(self):
        print("I'm car ")
        self.wheels = 4
        self.has_root = True
        
    def specific_usage(self):
        self.general_usage()
        print("specific use : commute to work, vacation with family ")
        
class Motorcycle(Vehicle):
    def __init__(self):
        print("I'm a motor cycle ")
        self.wheels = 2
        self.has_roof = False 
        
    def specific_usage(self):
        self.general_usage()
        print(" specific use : Local commutation, racing ")

c =Car()
m = Motorcycle()
c.specific_usage()
m.specific_usage()
#print(Issubclass(Car,MotorCycle))

###########################

class Father():
    def skills (self):#This is not constructor
        print("i like gardening, progaramming ")
    
class Mother ():
    def skills (self):#This is not constructor
        print ("I like cooking , art ")
        
class Child(Father,Mother):
    def skills (self):
        Father.skills(self)
        Mother.skills(self)
        print(" I like sports ")
        
c = Child()
c.skills()        

####################################

def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

# Example usage
import math

# Function for which derivative needs to be approximated
def f(x):
    return math.sin(x)

# Point at which derivative is to be approximated
x = math.pi / 4

# Step size
h = 0.01

# Calculate derivative using backward difference formula
approx_derivative = backward_difference(f, x, h)
print("Approximate derivative at x =", x, "is", approx_derivative)



''' 2 April 2024 '''
































