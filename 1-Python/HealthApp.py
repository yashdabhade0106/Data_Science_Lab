# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:17:20 2024

@author: yashd
"""

print("YOURS HEALTH MONITORING APP")
print("** BASIC INFORMATION ABOUT YOU **")                                         # BASIC INFO
print("PLEASE SUPPORT US FOR GIVING RIGHT INFORMATION ABOUT YOU\n")

name =  ( input ("What Is Your Name : \n"))
name = name.capitalize()
age =  int( input ("What Is Your Age : \n"))


height = float (input("What Is Your Height In Meters : \n"))
weight = float ( input ("What Is Your Weight In Kilogram\n : \n"))

#####################################################################

BMI=  weight/(height)**2                                                         # Body Mass Index

print(" 1. WEIGHT RELATED MONITORIZATION \n")

print("Your Body Mass Index is :",BMI)


# conditions to calculate bmi

if BMI < 18.5:
    print("You Are An Underweight Person")
    print("SUGGESTION NO 01 ")
    print(" 1 Start eating more frequently \n 2 Don't avoid your meals  ")
    print("SUGGESTION NO 02 ")
    print(" 1 Do normal exercise  \n 2 Avoid cold drinks ")
    
elif 18.5 <= BMI < 25:
    
    print("You Are A Normal Weight Person")
    
    print(" TIP ")
    print(" Maintain your daily routiene ")
    
elif 25 <= BMI < 30:
    print("You Are An Overweight Person")
    
    print("SUGGESTION NO 01 ")
    print(" 1 Eat fresh vegetable  \n 2 Don't eat junk food  ")
    
    print("SUGGESTION NO 02 ")
    print(" 1 Start running at least 60 minutes  \n 2.dont play the mobile games,instaed play some ground level games   ")
    
else:
    print("You Are An Obese Person")
    
    print("SUGGESTION NO 01 ")
    print(" 1 Start walking at least 90 minutes  \n 2 . dont take more fatty food")
    
    print("SUGGESTION NO 02 ")
    print(" 1 avoid oily substance \n 2.do exercise at your best level")
    
#####################################################################    
    
print(" \n *How We Calculate BMI *\n")                                            # BMI FORMULA

print("BMI is a simple calculation using a person's height and weight.")
print("The Formula is BMI= ( weight in kilogram ) / ( height kin meters)^2")

print (" ** conditions **")

print(" BMI is often used to categorize weight status:")

print(" Underweight: BMI < 18.5 ")
print(" Normal weight: 18.5 ≤ BMI < 25 ")
print(" Overweight: 25 ≤ BMI < 30 ")
print(" Obesity: BMI ≥ 30 ")

################################################################
# Nutritional Info 

sleep_dur=float(input("how much time do you sleep:\n"))

print("\n")
print("INFORMATION ABOUT YOUR DIET \n")
print("enter the amount of the following diet you have taken (approx) ")

print("A small to medium chapati has about 80 to 120 calories, while a 6-inch chapati has around 71 calories. A")
#######################################################################
#Sleep Duration according to Age
#age =  int( input ("What Is Your Age : \n"))
#*698import pandas as pd1taset.csv")
def sleep_duration():
 if 6 <= age <= 13:
    print("You Requried 9-11 hours sleep ")
 elif 14 <= age <= 17:
    print("You Requried 8-10 hours sleep ")
    
 elif 18 <= age <= 64:
    print("You Requried 7-9 hours sleep ")
    
 else :
    print("You Requried 7-8 hours sleep ") 
sleep_duration()  
  
#######################################################################

protein = float(input("Enter the amount of protein: "))  # in grams
fats = float(input("Enter the amount of fats: "))
chapati = int(input("Enter the amount of chapatis you eat: "))             # CALORIES INTAKE
carbohydrate = chapati * 120
def calculate_calories():
    carbohydrate_calories = chapati * 120
    global x 
    x = "total_calories"
    total_calories = (carbohydrate_calories + protein * 4 + fats * 9)
    return total_calories
total_calories = calculate_calories()
print("Total calories you acquire in single day will : ", total_calories)

#####################################################################

if  total_calories <= 2500:
    print("YOU HAVE LESS CALORIES INTAKE \n ")                         # CALORIES CONDITIONS
    print("PLEASE FOLLOW FOLLOWING INSTRUCTIONS ")
        
    print("\n 1 Drink More Water ")
    print("\n 2 Eat 4-6 Small Meals Instead 2-3 Large Meals ")


          
elif  total_calories >= 3200:
    print("YOU HAVE EXTERA CALORIES INTAKE \n ")
    print("PLEASE FOLLOW FOLLOWING INSTRUCTIONS ")
            
    print("\n 1 Drink More Water ")
    print("\n 2 DO ATLEAST 2 HRS EXERCISE ")

else:
    print("YOU HAVE NORMAL CALORIES INTAKE \n ")
#####################################################################
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Carbohydrate', 'Protein', 'Fats']
values1 = [carbohydrate, protein, fats]
values2 = [1000, 70, 45]

# Number of categories
num_categories = len(categories)

# Width of each bar
bar_width = 0.35

# x-axis locations for the groups
x = np.arange(num_categories)

# Plotting the bars
plt.bar(x - bar_width/2, values1, bar_width, label='Your Intake')
plt.bar(x + bar_width/2, values2, bar_width, label='Requried Intake')

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph Diet Comparison')
plt.xticks(x, categories)
plt.legend()

# Show plot
plt.show()  
#####################################################################
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Calories']
values3 = [total_calories]
values4 = [2500]

# Number of categories
num_categories = len(categories)

# Width of each bar
bar_width = 0.35

# x-axis locations for the groups
x = np.arange(num_categories)

# Plotting the bars
plt.bar(x - bar_width/2, values3, bar_width, label='Your Intake')
plt.bar(x + bar_width/2, values4, bar_width, label='Requried Intake')

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph Diet Comparison')
plt.xticks(x, categories)
plt.legend()

# Show plot
plt.show() 

#####################################################################

print("2. HEART RATE \n")
                                                                             # HEART RATE 
print("GIVE THE BASIC DETAILS FOR FURTHUR MONITORING\n ")

heart_rate = int(input("Enter your heart rate: "))

def heart_rate1():
    if 6<= age <= 15:
        if 70 <= heart_rate <= 100:
            print("You have Normal heart rate according to your age")
        else:
            print("You heart rate in not in the range of your age group")
    elif 6 > age:
        print("SORRY!! Not Fix data ")
        
    else:
        if 60 <= heart_rate <= 100:
            print("You have Normal heart rate according to your age")
        else:
            print("You heart rate in not in the range of your age group")
heart_rate1()

#####################################################################

print("HEALTH REPORT ")
                                                                             # Health report
tup = (f"""Hello Mr/Ms {name} \n Your age is {age} years young \n                 
       Your height and weight is {height} meter and {weight} kg \n 
       Me/Ms {name} your body mass index is {BMI}\n
       Your Sleep duration is {sleep_dur} hrous\n 
       and your calories intake is {total_calories}
       and \n protein intake is {protein} and  fat intake is {fats} 
       """)
print(tup)
#improvment
print("RECOMMENDDATION!")

tup2 = (f""" {sleep_duration()}\n{heart_rate1()}
        """)
print(tup2)

#####################################################################

#Converting Users data into csv file

import csv
with open ('Users.csv',mode='w') as csvfile:
    fieldnames = ['Name','Age','Height','Weight','BMI','Sleep Duration','Calories','Heart Rate']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name":name,"Age":age,"Height":height,"Weight":weight,"BMI":BMI,"Sleep Duration":sleep_dur,"Calories":total_calories ,"Heart Rate":heart_rate})
        
#Reading csv file
import pandas as pd      
dataframe = pd.read_csv("C:/DataScience/1-Python/Users.csv")   
print(dataframe)    
    
#####################################################################

"""import matplotlib.pyplot as plt
 import pandas as pd 
 import numpy as np

 width = 0.4
 #data = {'BMI':['22-23',BMI],'Sleep Durstion':['8',sleep_dur], 'Calories':['1800-3000',total_calories],'Heart rate':['80-100',heart_rate]}
 data = ['BMI','Sleep Duration','Calories','Heart rate']
 Healthy_Person = ['22-23','8','1800-3000','80-100']
 #Users = [BMI,sleep_dur,total_calories,heart_rate]
 num = [0,1,2,3,]
 #num2 = [i+w for i num]
 num =np.arange(len(data))
 plt.bar(data,num,width,label='data')
 plt.bar(num,Healthy_Person,width,label='Healthy_Person')
 plt.xlabel('data')
 plt.title('Compare')
 plt.legend()
 plt.show()

 ###################################




 ###################################
 import tkinter as tk
 from tkinter import messagebox

 def login():
     username = username_entry.get()
     password = password_entry.get()

     # Example validation (replace with your actual validation logic)
     if username == "admin" and password == "password":
         messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
     else:
         messagebox.showerror("Login Failed", "Invalid username or password")

 # Create the main window
 root = tk.Tk()
 root.title("Health Monitoring System")

 # Create and place widgets
 tk.Label(root, text="Username:").pack()
 username_entry = tk.Entry(root)
 username_entry.pack()

 tk.Label(root, text="Password:").pack()
 password_entry = tk.Entry(root, show="*")
 password_entry.pack()

 login_button = tk.Button(root, text="Login", command=login)
 login_button.pack()


 # Start the GUI event loop
 root.mainloop()
 """   
    
#########################################
   
   
   
   
   