# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:06:31 2024

@author: yashd
"""
def bycuisine():
    import pandas as pd
    print('which type of cuisine you want to taste today\n')
    cuisine=[ 'Indian,South Indian Recipes,Andhra,Udupi,Mexican,Fusion,Continental,Bengali Recipes,Punjabi,Chettinad,Tamil Nadu,Maharashtrian Recipe,North Indian recipe,Italian Recipes,Sindhi,Thai,Chinese,Kerala recipes,Gujrati Recipes,Coorg,Middle Eastern,Asian,Coastal karnataka,European,Kashmiri,Lucknowi,Rajasthani,Karanataka,Hyderabadi']
    print(cuisine)
    ch1=input('enter a cuisine: ')
    df=pd.read_csv("C:/DataScience/1-AdvancedPython/IndianFoodDatasetCSV.csv")
    cuisine1=df[(df['Cuisine']==ch1)]
    print(cuisine1[["RecipeName","Ingredients","Instructions"]])
    
def bycourse():
    import pandas as pd
    print('which type of course you want to taste today\n')
    course=['Side Dish,Main Course,South Indian Breakfast,Lunch,Snack,High Protein Vegitarian,Dinner,Appetizer,Indian Breakfast,North Indian Breakfast,Dessert']
    print(course)
    ch2=input('enter a course: ')
    df2=pd.read_csv("C:/DataScience/1-AdvancedPython/IndianFoodDatasetCSV.csv")
    course1=df2[(df2['Course']==ch2)]
    print(course1[["RecipeName","Ingredients","Instructions"]])


def bydiet():
    import pandas as pd
    print('which type of diet you want to taste today\n')
    diet=['Diabetic Friendly,Vegeterian,High Protein Vegetarian,Non Vegetarian,High Protein Non Vegetarian,Eggetarian,Vegan,No Onion No Garlic(Sattvic)']
    print(diet)
    ch3=input('enter a diet: ')
    df3=pd.read_csv("C:/DataScience/1-AdvancedPython/IndianFoodDatasetCSV.csv")
    diet1=df3[(df3['Diet']==ch3)]
    print(diet1[["RecipeName","Ingredients","Instructions"]])

def bytime():
    import pandas as pd
    print('In how much time you want to cook today\n1.0-20 mins\n2.20-45 mins\n3.greater than 45 mins\n')
    ch4=int(input("Enter your choice: "))
    df4=pd.read_csv("C:/DataScience/1-AdvancedPython/IndianFoodDatasetCSV.csv")
    def t():
        time1=df4[(df4['CookTimeInMins']>=0)&(df4['CookTimeInMins']<=20)]
        print(time1[["RecipeName","Ingredients","Instructions"]])
    def t1():
        time2=df4[(df4['CookTimeInMins']>20)&(df4['CookTimeInMins']<=45)]
        print(time2[["RecipeName","Ingredients","Instructions"]])
    def t2():
        time3=df4[(df4['CookTimeInMins']>45)]
        print(time3[["RecipeName","Ingredients","Instructions"]])

    match(ch4):
        case 1:
            t()
        case 2:  
            t1()
        case 3:
            t2()
def insert():    
    a=input("Enter recipe name: ")
    b=input("Enter ingredients name: ")
    c=input("Enter cuisine name: ")
    d=input("Enter course name: ")
    e=input("Enter instructions: ")
    df4=pd.read_csv("C:/DataScience/1-AdvancedPython/IndianFoodDatasetCSV.csv")
    df5=pd.DataFrame({"RecipeName":[a],"Ingredients":[b],"Cuisine":[c],"Course":[d],"Instructions":[e]})
    df4.append(df5)
    
    
print('welcome to our recipe recommendation system')
import pandas as pd
c=1
while c==1:
    
     print("how to choose recipe today\n1.by cuisine\n2.by course\n3.by diet\n4.by cook time\n5.insert a recipe")
     ch=int(input("enter your choice: "))
     match(ch):
         case 1:
             bycuisine()
         case 2:
             bycourse()
         case 3:
             bydiet()
         case 4:
             bytime()
         case 5:
             insert()
     c=int(input("do you want to continue (press 1 for continue)"))




















































































