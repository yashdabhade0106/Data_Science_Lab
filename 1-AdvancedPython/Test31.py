# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:05:43 2024

@author: yashd
"""

import pandas as pd 
result=pd.Series=[['red','green','white'],['red','black'],['yellow']]
print(result)
result1 = pd.series ([item in sublist for result for item in sublist  ])
print(result1)

########################################
text = ''' 
Joe waited for the train. The train was late.  
Mary and Samantha took the bus.  
I looked for Mary and Samantha at the bus station. 
''' 
text1 = text.split()
print(text1)


########################################

import pandas as pd 
import numpy as np
arrayOne = np.array([[5, 6, 9], [21 ,18, 27]]) 
print(arrayOne)
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])
print(arrayTwo)

Resutarray = arrayOne + arrayTwo
print(Resutarray)

Resutarray1 = np.square(Resutarray)
print(Resutarray1)

#######################################
DataFrame: ({ 
'tweets': ['@Obama says goodbye','Retweets for @cash','A political endorsement in 
@Indonesia', '1 dog = many #retweets', 'Just a simple #egg'] 
})









