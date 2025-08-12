# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:00:51 2024

@author: yashd
"""

def distance(a,b ):
  from geopy.geocoders import Nominatim
  from geopy import distance

  geocoder=Nominatim(user_agent="i am yuvraj")
  #a=input("enter your location:  ")
  #b=input("enter your destination:  ")
  coordinates1=geocoder.geocode(a)
  coordinates2=geocoder.geocode(b)
  lat1,long1=(coordinates1.latitude),(coordinates1.longitude)
  lat2,long2=(coordinates2.latitude),(coordinates2.longitude)
  place1=(lat1,long1) 
  place2=(lat2,long2)
  global dist
  dist=distance.distance(place1,place2).km
  print(dist,"km")
  



import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
if hour>0 and hour<12:
 print("Good morning")
elif hour>=12 and hour<=16:
 print("Good afternoon")
elif hour>16 and hour<=19:
 print("Good evening")
else:
  print ("Good night")

print("Welcome! to sanjivani travel planner\nMaking your plans better\n ")
#print("Instructions:\n1.for bus and railway source put the cities name in capital\n2.for flight source put only first letter in capital")    
a=input("Enter your location: ")
b=input("Enter your destination: ")
trep=0
location=["Kopargaon,Shirdi"]
destination=["Pune jn.,Mumbai,Aurangabad,Paithan,Shirdi"]
i=1
while i==1:
 ch=int(input(f"1.distance between {a} and {b} \n2.source to travel from {a} to {b}\n3.Hotels in {b} \n4.Places near to visit in {b} \n5.total expense\n"))
 match ch:
  case 1:
   distance(a,b)
  case 2:
   distance(a,b)
   fy=int(input("1.by bus\n2.by railway\n3.by plane\n4.by car\nenter your choice: "))
   match fy:
    case 1:
      if a=="Kopargaon" and b=="Pune jn.":

        from tabulate import tabulate
        mydata=[["Pune via Ahmednagar","05:00"],["Pune jn. via loni","05:30"],["Pune jn. via sangamner(shivshahi)","06:15,09:00,11:30"],
        ["Pune jn. via Ahmednagar","07:15,08:00,14:00,14:30"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))
      elif a=="Kopargaon" and b=="Mumbai":

        from tabulate import tabulate
        mydata=[["Mumbai","07:00"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))

      elif a=="Kopargaon" and b=="Aurangabad":

        from tabulate import tabulate
        mydata=[["Aurangabad via vaijapur","06:45,08:30,09:30"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))

      elif a=="Kopargaon" and b=="Paithan":

        from tabulate import tabulate
        mydata=[["Paithan via bableshwar","06:45"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))


      elif a=="Kopargaon" and b=="Shirdi":

        from tabulate import tabulate
        mydata=[["Shirdi via sai corner","08:00,11:30,15:00"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))

      elif a=="Shirdi" and b=="Pune jn.":

        from tabulate import tabulate
        mydata=[["Pune via Ahmednagar","0:30,10:00,11:45,12:00,13:00,14:00,15:00,16:00,17:30,19:00,21:30,23:00"],["Pune jn. via sangamner","05:45,06:45,08:00,08:30,09:00,09:30,10:15,11:30,12:30,14:30,15:00,15:30,16:50,17:30,"],["Pune jn. via sangamner(shivshahi)","06:15,09:00,11:30"],
        ["Pune jn. via shevgaon","08:00,09:00,14:00,14:30"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))

      elif a=="Shirdi" and b=="Mumbai":

        from tabulate import tabulate
        mydata=[["Mumbai","07:00,09:00,14:00,17:00,20:00,21:00"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))


      elif a=="Shirdi" and b=="Aurangabad":

        from tabulate import tabulate
        mydata=[["Aurangabad via shrirampur","05:00,05:30,06:00,07:00,07:30,08:00,08:30,09:00,"],["Aurangabad via vaijapur","15:30,17:30"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))

      elif a=="Shirdi" and b=="Paithan":

        from tabulate import tabulate
        mydata=[["Paithan ","07:15"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))

      elif a=="Ahmednagar" and b=="Pune jn.":

        '''from tabulate import tabulate
        mydata=[["Mumbai","07:00"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))'''
        print("no data found")

      elif a=="Ahmednagar" and b=="Mumbai":

        from tabulate import tabulate
        mydata=[["Mumbai","08:00,09:30,22:45,23:15"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))


      elif a=="Ahmednagar" and b=="Aurangabad":

        '''from tabulate import tabulate
        mydata=[["Mumbai","07:00"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))'''
        print("no data found")

      elif a=="Ahmednagar" and b=="Paithan":

        '''from tabulate import tabulate
        mydata=[["Mumbai","07:00"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))'''
        print("no data found")


      elif a=="Ahmednagar" and b=="Shirdi":

        from tabulate import tabulate
        mydata=[["Shirdi ","02:15,04:15,08:00,09:45,10:30,10:45,11:00,15:15,15:30,15:45,16:30,17:00,17:30,17:45,19:00,19:15,20:30"]]
        head = ["VIA\ROUTE","TIME"]
        print(tabulate(mydata,headers=head,tablefmt="grid"))

      else:
        print("data is uploading")
      if fy==1:
       trep=dist*2
       print(f"total expense for bus is {trep} rupees")
  #elif fy==2:
    #trep=dist*1.6
   # print(f"total expense for railway is {trep} rupees")
   #elif fy==3:
   # trep=dist*4
    #print(f"total expense for plane is {trep} rupees")
    
    case 2: 
      import pandas as pd
      c=(a.upper())#location store in c
      d=(b.upper())#destination store in d
      
      df=pd.read_csv('Train_details_22122017.csv')
      if c and d in df.values:
          new_df=df[(df['Station Name']==c)&(df['Destination Station Name']==d)]
          print(new_df)
          trep=dist*1.6
          print(f"total expense for railway is {trep} rupees")
      else:
          print("sorry,we didnt found any train for your destination")
      
    case 3: 
      import pandas as pd

      df2=pd.read_csv('Flight_Schedule.csv')
      if a and b in df2.values:
          new_df=df2[(df2['origin']==a)&(df2['destination']==b)]
          print(new_df)
          trep=dist*4
          print(f"total expense for plane is {trep} rupees")
      else:
          print("sorry,we didnt found any flight for your destination/ndata is uploading")
          
    case 4:
        mil=int(input("enter milage of your car: "))
        diesel=dist/mil
        trep=diesel*93
        print(f"you need {diesel}litres of diesel\nyour travel expense will be {trep}")
  case 3:
      import pandas as pd
      if b=="Pune jn." :
         b="Pune"
      df3=pd.read_csv('goibibo_com-travel_sample.csv')
      new_df9=df3[(df3['city']==b)]
      if b in df3.values:
          print(new_df9)
          star=int(input("enter the type of hotels\n1.5 star \n2.4 star \n3.3 star: "))
          nod=int(input("enter the number of days: "))
          members=int(input("enter number of members: "))
          if star==1: 
            new_df2=df3[(df3['hotel_star_rating']==5)&(df3['city']==b)]
            hotelexpense=4000*nod*members
            print(new_df2)
            print("hotel expense is ",hotelexpense)
            #print(new_df2)
          elif star==2:
            new_df2=df3[(df3['hotel_star_rating']==4)&(df3['city']==b)]
            hotelexpense=2500*nod*members
            print(new_df2)
            print("hotel expense is ",hotelexpense)
            #print(new_df2)
          elif star==3:
            new_df2=df3[(df3['hotel_star_rating']==3)&(df3['city']==b)]
            print(new_df2)
            hotelexpense=800*nod*members
            print(hotelexpense)
          else:
            new_df2=df3[(df3['hotel_star_rating']==2,1,0)&(df3['city']==b)]
            print(new_df2)
            hotelexpense=500*nod
            print(hotelexpense)
          ch2=int(input("feeling hungry(1-yes)"))
          fd=pd.read_csv("D:/New folder/IndianFoodDatasetCSV.csv")
          if ch2==1:
              ch3=int(input("1.breakfast\n2.lunch\n3.dinner\n4.snack\nwhat do you wanna eat: "))
              match(ch3):
                  case 1:
                      print("Here are some breakfast dishes to you")
                      
                      fd1=fd[(fd['Course']=='Indian Breakfast')and(fd['Course']=='South Indian Breakfast')and(fd['Course']=='North Indian Breakfast')]
                      print(fd1)
                      foodexpse=100
                  case 2:
                      print("Here are some lunch dishes to you\nany dish for rs.250 only")
                      
                      fd2=fd[(fd['Course']=='Lunch')]
                      print(fd2)
                      foodexpse=250
                  case 3:
                      print("Here are some dinner dishes to you\nany dish for rs.250 only")
                      
                      fd2=fd[(fd['Course']=='Dinner')]
                      print(fd2)
                      foodexpse=250
                  case 4:
                      print("Here are some snack dishes to you\nany dish for rs.100 only")
                      
                      fd2=fd[(fd['Course']=='Dinner')]
                      print(fd2)
                      foodexpse=100
                      
                      
      else:
          print("\nSorry, we didnt find any hotels in your destination/ndata is uploading")
      
  
  case 4:
    df4=pd.read_csv('Places to visit.csv')
    advplcs={'Pune':'Pawna Lake Camping, Adlbs Imagica, Diamond Waterpark, Mulshi Lake and Dam, Rajamchi Fort Trek, Lohagad Camping and Trekking, Malsej Ghat Camping, Wai Camping, Camping beside Bhandardara Lake, Lonavala, Panchgani, Khandala, Kamshet, Appu Ghar Amusement Park, Peacock Bay.',
             'Mumbai':' Abseiling Near Mumbai,Gorakhgad Night Trek,Mumbai Flying tour in a fixed-wing Aircraft,Paintball Near Powai, Mumbai - 50 Balls,Paragliding at Kamshet Near Mumbai,Rappelling Near Khandala Dukes Nose 300 Feet,Sailing Yacht Cruise from Mumbai on Fareast ,Sarasgad Night Trekking.',
             'Nashik':'Sula Vineyards, Dudhsagar Falls, Saptashrungi, Trimbakeshwar Temple, Pandavleni Caves, Sita Gumpha, Anjaneri Hills, Gangapur Dam, Dugarwadi Waterfall, Kalaram Temple, Vallonne Vineyards, Harihar Fort, Coin Museum, Muktidham, Vihigaon Waterfall, Tringalwadi Fort',
             'Aurangabad':'Ellora Caves. UNESCO World Heritage Site,Ajanta Caves. Rock-cut Buddhist Cave Temples,Bibi Ka Maqbara Aurangabad. Taj of the Deccan,Bhadra Maruti Temple. Popular Temple Dedicated to Hanuman,Valley of the Sufi Saints. Famous Sufi Site,Grishneshwar Temple Jyotirlinga, Aurangabad,Aurangabad Caves,Khuldabad Aurangabad.'}
    shopping={}
    if b=="Pune jn." :
      b="Pune"
    if b in df4.values:
        new_df4=df4[(df4['DISTRICT']==b)]
        print(new_df4)
    else:
        print("sorry,we didnt find any place near to visit /ndata is uploading")
    che=int(input("hows your mood now\nlets go for\n1.adventurous place\n2.shopping mall\n3.theatre"))
    if b=='Pune'or b=='Mumbai'or b=='Nashik' or b=='Aurangabad':
      if che==1:
        y=advplcs[b]
        print("here are some adventurous place to visit")
      elif che==2:
          print(" ")
      
  case 5:
    print('Total expenses are :')
    from tabulate import tabulate
    mydata=[["travel expenses",trep],["Hotel expenses",hotelexpense],["Food Expenses",foodexpse],["Total expenses",trep+hotelexpense+foodexpse]]
    head = ["Type","Amount"]
    print(tabulate(mydata,headers=head,tablefmt="grid"))

 i=0       
 i=int(input("do you want to continue\n1.yes\n2.no  \n"))