# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:40:45 2024

@author: yashd
"""

#Write a python program to draw a line with suitable lable in the
import matplotlib.pyplot as plt
X = range(1,50)
Y = [value * 3 for value in X]
print("values of X: ")
print(*range(1,50))

""" This is equivalent to 
i innn range (1,50 ): 
    print(i, end = ' ') """

print("Values of Y (thrice of X): ")
print(Y)

#plot lines and/or markers to the Axes.
plt.plot(X,Y)

#set the x axis label of the current axis 
plt.xlabel('x - axis')

#set the y axis label of the curret axis 
plt.ylabel('y - axis')

#set a title
plt.title('Draw a line.')

#display the figure 
plt.show()

#####################################
#Write a python program to draw a line
#using given axis values
#label in the x axis, x-axis and title
import matplotlib.pyplot as plt
# x axis values
x = [1,2,3]

# y axis values
y = [2,4,1]

# Plot lines and / or markers to the axis 
plt.plot(x,y)

#set the x axis label of the crrent axis
plt.xlabel('x - axis')

#set the y axis label of the curret axis 
plt.ylabel('y - axis')

#set a title
plt.title('Sample graph.')

#display the figure 
plt.show()

#####################################
#Write a pythn program to plot two or more lines
#on the same plot with suitable legends of each 

import matplotlib.pyplot as plt
#line 1 points
x1 = [10,20,30]
y1 = [20,30,10]

#line 2 points 
x2 = [10,20,30]
y2 = [40,10,30]

#ploting the line 1 points
plt.plot(x1,y1,label = "line 1")

#ploting the line 2 points
plt.plot(x2,y2,label = "line 2")
plt.xlabel('x - axis')

#set the y axis label of the curret axis 
plt.ylabel('y - axis')

#set a title
plt.title('Two or more lins on same plot with suitable labels.')

#show legends on the plot 
plt.legend()

#display the figure 
plt.show()

#####################################
#Write a pythn program to plot two or more lines
#on the same plot with suitable legends of each 

import matplotlib.pyplot as plt
#line 1 points
x1 = [10,20,30]
y1 = [20,30,10]

#line 2 points 
x2 = [10,20,30]
y2 = [40,10,30]

#ploting the line 1 points
plt.plot(x1,y1,label = "line 1")

#ploting the line 2 points
plt.plot(x2,y2,label = "line 2")
plt.xlabel('x - axis')

#set the y axis label of the curret axis 
plt.ylabel('y - axis')

#set a title
plt.title('Two or more lins on same plot with suitable labels.')

#Display the figure 
plt.plot(x1,y1, color = 'blue',linewidth = 3, label = 'line1-width-3')
plt.plot(x2,y2, color = 'red',linewidth = 5, label = 'line2-width-5')

#show legends on the plot 
plt.legend()

#display the figure 
plt.show()

#####################################
#Write a pythn program to plot two or more lines
#on the same plot with suitable legends of each 

import matplotlib.pyplot as plt
#line 1 points
x1 = [10,20,30]
y1 = [20,30,10]

#line 2 points 
x2 = [10,20,30]
y2 = [40,10,30]

#ploting the line 1 points
plt.plot(x1,y1,label = "line 1")

#ploting the line 2 points
plt.plot(x2,y2,label = "line 2")
plt.xlabel('x - axis')

#set the y axis label of the curret axis 
plt.ylabel('y - axis')

#set a title
plt.title('Two or more lins on same plot with suitable labels.')

#Display the figure 
plt.plot(x1,y1, color = 'blue',linewidth = 3, label = 'line1-dotted',linestyle='dotted')
plt.plot(x2,y2, color = 'red',linewidth = 5, label = 'line2-dotted',linestyle='dotted')

#show legends on the plot 
plt.legend()

#display the figure 
plt.show()













