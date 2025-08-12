# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:43:26 2024

@author: yash
"""

print('Hello World')
x=1.5
print(x)
print (type(x))
x=100000000000000000000000000000
print(x)
print(type(x))

'''18 march 2024'''

age=input("Please enter your age:")
print(type(age))
print(age)

age1=input("Please enter your age:")
print(type(age1))
print(age1)

age2=input("Please enter your age:")
print(type(age2))
print(age2)

age=age1+age2
print(age)

'''IT TAKES INPUT IN A STRING FORMAT'''

age=int(input("Please enter your age:"))
print(type(age))
print(age)

age1=int(input("Please enter your age:"))
print(type(age1))
print(age1)

age2=int(input("Please enter your age:"))
print(type(age2))
print(age2)

age=age1+age2
print(age)

''' FLOAT NUMBER '''

exchange_rate = 1.5
print(type(exchange_rate))
print(exchange_rate)

int_value=100
string_value = '1.5'
float_value = float(int_value)
print('int value as a float:',float_value)
print(type(float_value))

'''COMPLEX NUMBER '''

c1 = 1j
c2 = 2
print('c1:',c1,'c2:',c2)
print(type(c1))
print(type(c2))
print(c1.imag)
print(c2.real)

'''BOOLEAN '''

all_okay = True
print(all_okay)
all_okay = False
print(all_okay)
print(type(all_okay))


status = bool(input('OK it is confirmed?:'))
print(status)
print(type(status))

'''ARETHMETIC'''

home = 10
away = 15
print(home + away)
print(type(home + away))
print(10*4)
print(type(10*4))
goals_for = 10
goals_against = 7
print ( goals_for - goals_against)
print(goals_for + goals_against)

print(100/20)
print(type(100/20))


print(100//20)
print(type(100//20))
'''19 march 2024 '''

print('Modulus division 100 % 13:', 100%13)
print('Modulus division 3 % 2 :',3%2)

'''but what if you are only intrested in 
remainder part of division ,the integer 
division operator has lost that ?
well in that case you can use the
 modulus operator '''
 
 # power operator
a = 5
b = 3
print(a ** b)

x = 0
x += 1# has the same behaviour as x = x+1

# None value
winner = None
print(winner is None )
#Alternative you can also write :
print(winner is not None)
# which will print out true only if thw 
winner = None
print('winner:',winner)
print('winner is none:',winner is None)
print('winner is not None :',winner is not None )
print (type(winner))

#comparison Operator
num = int (input('Enter the number:'))
if num > 0:
print(num)

#now let us give the indentation 
num = int (input('Enter the number:'))
if num > 0:
   print(num)
   
#Else in the If statement
num = int (input('Enter the number:'))  
if num < 0:
    print('Its negative')
else:
    print('Its not negative')    

# The use of elif
saving = float(input('Enter how much you have save in saving :'))
if saving == 0:
    print('Sorry no saving ')
elif saving < 500:
    print ('Its tidy sum ')
elif saving < 1000: 
    print ('Thats a tidy sum ' )
elif saving < 10000:
    print ('Welcome sir!')
else:
    print('thank you ')
        
#Iteeation/looping
#While loop

count = 1
print ('Starting')
while count <= 10:
  print(count)
  count+=1    

#For Loop
#loop over a set of value in a range

print('Print out values in a range ')
for i in range(2,10):
    print(i)
    print('Done')
    
###################################
    
print('Only print code if all iterations completed')
num = int(input('Ente a number to check for :'))
for i in range(0,16):
    if i == num:
        break
    print (i)
    print('Done')
    
# use of anonymous variable

for _ in range(0,10):
    print('.')
    print()

for _ in range(0,10):
    print('.',end='')
    print()

for _ in range(0,10):
    print('.',end='')
    #print()

' 20 march 2024 '

#python program to print odd number in given range

start , end = 4, 19
#iterating each number in list 
for num in range (start,end+1):
    
    #check condition
    if num %2 != 0:
        print (num,end = " ")

#python program to print even number in given range

start , end = 2, 21
#iterarting each number in list 
for num in range ( start, end+1):
    
    #check condition 
    if num % 2 == 0:
        print(num,end = " ")

x,y,z = 5,6,7
print(x)
print(y)
print(z)

x,y,z = 5
print(x)
print(y)
print(z)

####################################
#Global variable
x="awesome"
def my_function():
    print("python is "+x)
my_function ()    

x="awesome"
def my_function():
    x ="fantastic"
    print("python is "+x)
my_function ()    
print("python is "+x)


#getting data types

x=5
print(type(x))

##########################
x=range(6)
print(type(x))

##########################
x={"name":"ram","age":34}
print(type(x))

#########################
x=1
z=float(x)
print(z)

#########################
str1 = "hello"
str2= 2
str3= str1+str2
#########################
#string
#if you want multiple strings
x="""This is python. It is very poerful"""
print(x)

########################
#string slicing
x="""This is python. It is very poerful"""
print(x[2:8])

########################

#slice from start 
print(x[:3])

#slice to the end
print(x[4:])

#Negative indexing
print(x[-5:-2])

#modify string
print(x.upper())
#######################
x=x.upper()
print(x.lower())

########################
#remove white space , removes white space from intital to 

x="   This is python"
print (x.strip())

x="   This is python"  " remove space for left only"
print (x.ltrip())

x="This is python   "  " remove space for right only"
print (x.rtrip())
######################
x="Hello world "
print(x.replace("world","Nurd"))

######################

#Use of split which replace white space/or (,)

x="Hello world"
print(x.split(" "))

x="Hello,world"
print(x.split(","))
#####################

"""2nd shift """

x="Hello World"
string = x[::-2]
print(string)

x="Hello World"
string = x[::-1]
print(string)

#find method, searches the string for a specified value
x="This is python it is very poerful "
print(x.find("and"))
#################################

#string concatness
x="hello"
y="world"
print(x+y)

#to add white space 
x="hello"
y="world"
print(x+" "+y)

#string format
x=19
y="My name is Yash"
print(x+y)
#it will give error

print(f"my name is Yash and my age is  {x}")
######################
quantity=3
item_no=54
price=67
print(f"i want {quantity} pieces and item number is {item_no},its price is {price}")
#####################################
my_order = "I want {} pieces and item number is {} , its price is {}"
print(my_order.format(quantity,item_no,price))

#########################

my_order = "I want {0} pieces and item number is {1} , its price is {2}"
print(my_order.format(quantity,item_no,price))

#######################

text="This is fun fair and it has got big \"round rigo \""
print(text)

#Operator precedence
print(3*3+3/3-3)

"""rule for mathematics operations 
PEMDAS
P: paranthesis
E: exponential
M: multiplication
D: division       
A: addition 
S: subtraction
"""

#python list
lst=["cherry","banana","apple"]
print(lst)
#list item are indexed , the item has index[0]
print(lst[0])
print(lst[2])

#append() adds element at the end of the list
lst=["cherry","banana","apple"]
lst.append("mango")
print(lst)

#clear removes all the element from the list
lst=["cherry","banana","apple"]
lst.clear()
print(lst)

#copy() method
lst=["cherry","banana","apple"]
lst2=lst.copy()
print(lst2)

#############################
lst=["cherry","cherry","banana"]
lst.count("cherry")
#############################
#extend() add elements of second string to first
lst=[1,2,3]
lst1=[4,5,6]
lst.extend(lst1)
print(lst)
##############################
#insert() method, Insert the element at given position 
lst=["cherry","cherry","banana"]
lst.insert(1,"mango")
print(lst)
#########################
#pop() Removes the element at the specified position 
lst=["cherry","cherry","banana"]
lst.pop(2)
print(lst)
############################
lst=["cherry","cherry","banana"]
lst.remove("cherry")
print(lst)
############################
#reverse()
lst=["cherry","cherry","banana"]
lst.reverse()
print(lst)
############################

#sort() sort thr list alphabetically
lst=["cherry","cherry","banana"]
lst.sort()
print(lst)
############################
#Tupple
tup=("cherry","cherry","banana")
print(tup)
print(tup[2])
#once tuple is crdeated ,you can not change its value

x=("apple","banana","cherry")
x[1]='kiwi'
#First convert into list
y=list(x)
y[1]="kiwi"
#convert list to tuple 
x=tuple(y)
print(x)
##########################
x = ("apple",2,"cherry")
print(x)
#################################
#you can access tuple by refreing to the index
x = ("apple",2,"cherry")
print(x[1])
#################################
#to join two or more tuple you can use + 
tuple1=("a","b","c")
tuple2=(1,2,3)
tup1=tuple1+tuple2
print(tup1)

#Dectionary
dict1={"Brand":"Maruti","model":"2324","year":2011}
print(dict1)
print(len(dict1))
print(type(dict1))

dict2={ "Brand":["Maruti","Mahendra","Toyato"], "model":["a","b","c"],"year":[2011,2013,2022]}


dict1.get("model")
dict1.keys()
################################

"""21 march 2024 """

car = {
"brand":"Ford",
"model":"Mustang",
"year":1967
}
x=car.keys()
print(x)
car["color"]="Black"
x=car.keys()
print(x)

car = {
"brand":"Ford",
"model":"Mustang",
"year":1967
}
car.pop("model")
print(car)

#Accessing keys in the dictionary

for x in car:
    print (x)

#Accessing values in the dictionary

for x in car:
    print (car[x])

# if you want to access both keys and values 
# very important 

for keys,value in car.items():
    print("%s = %s"% (keys, value ))
    
 ##############################
# copying dictionary
   
car = {
"brand":"Ford",
"model":"Mustang",
"year":1967
}  
car2=car.copy()
print(car2)   
    
 ##############################
#Another way to make a copy is to use the    

car2=dict(car)   
print(car)
    
thisdict={
"brand":"Ford",
"model":"Mustang",
"year":1967
}
dict1=dict(thisdict)
dict1
    
 #A dictonary can contain dictonaries 
#This is called nested dicgtonaries 
our_family ={
"child1":{
"name":"Yuvraj",
"dob":"15-02-2004"
},
"child2":{
"name":"Aditya",
"dob":"20-03-2024",
}

}  
our_family 
    
 #clear():remove all elemnts from dictonary   
 
car = {
"brand":"Ford",
"model":"Mustang",
"year":1967
}
car.clear()
print(car)

# fromkey()
#create a dictonary with 3 keys 
x={"key1","key2","key3"}
y=0
thisdict=dict.fromkeys(x,y)
print(thisdict)

x={"key1","key2","key3"}
y={"11","22","33"}
thisdict=dict.fromkeys(x,y)
print(thisdict)

#get() to get the vaule of dictonary

car = {
"brand":"Ford",
"model":"Mustang",
"year":1967
}
car.get("model")

################################
#item() return the dictonary's key-value 
car = {
"brand":"Ford",
"model":"Mustang",
"year":1967
}
car.items()

#values() display all the values of dictonary
car = {
"brand":"Ford",
"model":"Mustang",
"year":1967
}
car.values()

#upodate () insert an item to the dictonary 

car = {
"brand":"Ford",
"model":"Mustang",
"year":1967
}
car.update({"colour":"Black"})
car
   
#for loop
fruits = ["Apple","Banana","Cherry"]
for i in fruits:
    print(i)
#########################
#use of break statement 

fruits=["apple","banana","orange"]
for i in fruits:
    print(i)
    if(i == "banana"):
      break
  
###################################

fruits=["apple","banana","orange"]
for i in fruits:
   
    if i == "banana":
      break
    print(i)

##############################
#continue with the continue statement 

fruits=["apple","banana","orange"]
for x in fruits:
    if x == "banana":
      continue
    print(x)
    
#Lambda function
#a lambda function is small anonymous function 
#a lambda can take any number of arguments, 
#but can only have one expression 

def add(a):
    sum=a+10
    return sum

add(20)

add=lambda a:a+10
print(add(20))

add=lambda a,b:a+b
print(add(5,6))

#finding odd numbers from the list
lst=[34,12,64,55,75,13,63]
odd_lst=list(filter(lambda x:(x%2 != 0),lst))
print(odd_lst)

#finding even numbers from the list
lst=[34,12,64,55,75,13,63]
even_lst=list(filter(lambda x:(x%2 == 0),lst))
print(even_lst)


#Square list 

lst =[1,2,3,4,5,6,7,8,9,10]
square_lst=list(map(lambda x:(x**2),lst))
print(square_lst)

""" 22 march 2024 """

print("Welcome to roller coaster ")
height=int(input("Enter your height in cm :"))
if height >=120:
    print("You are eligible for roller coaster ")
    age=int(input("Enter your age in years :"))
    bill=0
    if age<12:
        print("child's ticket is 5 $")
        bill=5
    elif age <19 and age >12 :
        print("teenger' ticket is 10$")
        bill=10
    elif age <= 40 and age >= 20 :   
        print ("Adult's ticket is 15$")
        bill=15
    else :
        print("Boomer's ticket is 20$")
        bill=20
    buy=int(input(" 1 You want popcorn? \n 2 You want to take pic? \n 3 You want ice cream? \n 4 Nothing\n"))
    if buy==1:
        print("Your popcorn will cost 11$ ")
        bill+=11
    elif buy==2:
        print("Your pic will cost 14$")
        bill+=14
    elif buy==3:
        print("Your ice cream will cost 10$")
        bill+=10
    elif buy==4:
        print ("Thank you For visting :)")
else:
    print("You are not eligible. Sorry!!!!")

print(f"Your bill is {bill}$")

##################################

#BMI 
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg : "))
BMI = round((weight/(height*height)),2)
if BMI <18.5:
    print(f"You are under weight and your BMI is {BMI}")
elif BMI >18.5 and BMI <25:
    print(f"You are a normal weight and your BMI is {BMI}")

elif BMI >25 and BMI <30:
    print(f"You are a over weight and your BMI is {BMI}")
        
elif BMI >30 and BMI <35:
    print(f"You are a obese and your BMI is {BMI}")
    
elif BMI >35 :
    print(f"You are a clinically obese and your BMI is {BMI}")
    
################################    
    
lst1=[1,2,3,5,6,7]

def is_duplicate(lst1):
    
    for i in range (len(lst1)-1):
        #compare current number with next number 
        if (lst1[i]==lst1[i+1]):
            return True
    return False 
print(is_duplicate(lst1))    

############################

lst1=[4,5,2,7,9,1,4]
lst1.sort()
def is_duplicate(lst1):
    
    for i in range (len(lst1)-1):
        #compare current number with next number 
        if (lst1[i]==lst1[i+1]):
            return True
    return False 
print(is_duplicate(lst1))  

##################################


def is_leap_year (year):
    if((year>0) and (year%4==0) and (year%100!=0) or (year%400==0)):
     return True  
    return False
 
is_leap_year(1900) 

#Mario pyramid 

for i in range (4):
    for j in range (4):
        print("#",end = " ")
    print ()

for i in range (4):
    for j in range (i+1):
        print ("#",end=" ")
    print()    

for i in range (4):
    for j in range (4-i):
        print ("#",end=" ")
    print()    

lst = [23,45,2,1,5,7,8,12]
def min_max (lst):
    
        min=lst[0]
        for i in lst:
          if i < min :
            min = i
        print("minimum number is ",min)

max= lst[0]
for i in (lst):
    if i > max :
        max = i
print ("maximum value is ",max)

min_max(lst)        
 
"""           
stra=int(input("Enter a string : "))
if stra == [ ]:
 print(" Please enetr a string ")
else :       
 print (f"enterd string is {stra}")
 strb = stra.reverse(stra)
 
 stra==strb
 print (" yes")
"""
def is_palindrom(input):
    if input=="":
        return "you entered wrong input "
    else:
        string=input [::-1]
        if string==input:
            return True
    return False    
    
print(is_palindrom ("step on no pets"))

#users=["admin","manger","empoley","staf","worker"]
user=input("Enter users status : ")


if user=="admin":
      print ("Hello admin , would you like to see status report ?")
elif user=="manger":
      print("Hello manger ")
elif user=="empoley":
      print("Hello empoley ")
elif user=="staf":
      print("Hello staf ")
elif user == "worker":
      print("hello worker ")
else:
      print("User not verified ")

#################################
#pick the adjective 
adjective=['sleepy','slow','smelly','wet','fat','red',
           'orange','yellow','green','blue','purple','fluffy',
           'white','proud','brave']
#pick the noun 
nouns = ['apple','dinosaur','ball','totaster',
         'goat','dragon','hammer','duck','panda']

#pick the words 
import random
import string
adjective= random.choice(adjective)
noun = random.choice(nouns)

#pick the number 
number = random.randrange(0,100)

#select the special character 
special_char = random.choice(string.punctuation)
#create new secure password
password = adjective + noun + str(number) + special_char
print("Your new password is : ",password)

print ("Welcome to password picker !")
while True:
    adjective = random.choice(adjective)
    noun = random.choice(nouns)
    number = random.randrange(0,100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number)+ special_char 
    print("Your new password is :",password)
    response = input("Would you like genreat another password ? ")
    if response == "n":
        break
# noun upper case

print ("Welcome to password picker !")
while True:
    adjective = random.choice(adjective)
    
    noun = random.choice(nouns)
    noun2 =noun.upper()
    number = random.randrange(0,100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun2 + str(number)+ special_char 
    print("Your new password is :",password)
    response = input("Would you like genreat another password ? ")
    if response == "n":
        break

"""25 march 2024 """


































