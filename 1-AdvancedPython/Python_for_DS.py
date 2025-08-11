# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:40:13 2024

@author: yash
"""

# A SERIES IS USED TO MODEL ONE DIMENSIONAL DATA
# SIMILAR TO A LIST IN PYTHON
#The Series object also has a few more bits 
# of data includind #index and a name 

import pandas as pd
songs2= pd.Series([145,142,38,13],name='counts')
# it is easy to inspect the index of a series 
songs2.index 
# The index can be string based as well,
#in which case pandas indicates 
# that the datatype for the index is object (not string)

songs3= pd.Series([145,142,38,13],name='counts')
index=(['paul','John','George','Ringo'])
songs3.index
songs3

#The NaN value

#Numeric colum will become NaN.
import pandas as pd 
f1 = pd.read_csv("C:/DataScience/1-AdvancedPython/age.csv.xls")
f1

#None, NaN,nan and null are synonyms
#the Series object behaves similarly to 
# a Numpy array

df = pd.read_excel("C:/DataScience/1-AdvancedPython/Bahaman.xlsx")
import numpy as np
numpy_ser = np.array([145,142,38,13])
#142
songs3[1]
numpy_ser[1]
#They both have methods in common
songs3.mean()
numpy_ser.mean()

#THE PANDAS SERIES DATA STRUCTURE PROVIDES 
#SUPPORT FOR THE BASIC CRUD
#operations-create, read, update, and delete.
#Creation

george = pd.Series([10,7,1,22],
index=['1968','1969','1970','1970'],name='George_Songs')
george

#Reading 
#To read or select the data from a series
george['1968']

george['1970']
#We can iterate over data in a series 
#as well. when iterating over a series 
for item in george:
    print(item)

#################################
#Updating
#updating value in a series can be a 
#little tricky as well
#to update a value 
#for a given index label,
#the standard index assingment opderation Works
george['1969']=68
george['1969']
george

""" 3 April 2024 """

#######################################
#03/04/2024
import pandas as pd
s=pd.Series([2,3,4],index=[1,2,3])
s
###############################################
#if we want to update the value orn delete the value 
george=pd.Series([10,7,8,22],index=['1968','1969','1970','1978'],
name='George')
#for update 
george['1969']=68
george['1969']
george

#deletion
s=pd.Series([2,3,4],index=[1,2,3])
del s[1]
s

###############################3
#now to convert the datatypes
#string use.astype(str)
#numeric use pd.to_numeric
#integer use .astype(int)


songs_66=pd.Series([3.0,None,11.0,9.0],
                   index=["george","ringo","john","paul"],
                   name="counts")
songs_66.dtypes
#dtype("float")
pd.to_numeric(songs_66.apply(str))
#there will bw error
pd.to_numeric(songs_66.astype(str),errors='coerce')
'''
songs_66["ringo"]=5.0
songs_66["ringo"]
songs_66
pd.to_numeric(songs_66.apply(str))
pd.to_numeric(songs_66.astype(str))
'''
#dealing with none
#the .fillna method will replace them with a given value
songs_66=pd.Series([3,None,11,9],
                   index=["george","ringo","john","paul"],
                   name="counts")
songs_66.dtypes
songs_66=songs_66.fillna(7)
#pd.to_numeric(songs_66.apply(str))
songs_66=songs_66.astype(int)
songs_66.dtypes
songs_66

###
#NaN values can be droped
#the serires using .dropna
songs_65=pd.Series([3.0,None,11.0,9.0],
                   index=["george","ringo","john","paul"],
                   name="counts")
songs_65
songs_65=songs_65.dropna()
songs_65

############################################
#append,combining and joining two series
songs_77=pd.Series([7,8,4,5],index=["prasad","hardik","yash","yuvraj"]
                   ,name="counts")
#to concatenate the series
songs=pd.concat([songs_66,songs_77])
songs

########################################
'''matplotlib is a module and pyplot is package inside it
so thatswhy we are calling it like matplotlib.pyplot'''
#plotting series
import matplotlib.pyplot as plt
fig=plt.figure()
songs.plot()
plt.legend()
####################################
fig=plt.figure()
songs_77.plot(kind='bar')
songs_66.plot(kind='bar',color='y')
plt.legend()

#################################
import numpy as np
data=pd.Series(np.random.randn(500),name='500 random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()

""" 4 April 2024 """
#To check version of pandas

import pandas as pd 
pd.__version__

##############################

#conda install pandas ==2.2.1

#Create using constructor
#Create pandas DataFrame froom list 

import pandas as pd
technologies = [["Spark",20000,"30Days"],["pandas",20000,"40Days"]]

df=pd.DataFrame(technologies)
print(df)

###################################
#Since we have not given labels to column and 
#index, DataFrame by default assigns


column_names = ["Courses","Fee","Duration"]
row_label = ["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print (df)

###############################
df.dtypes

###########################
#you can also assign custom
#data types to columns.
#set custom type as DataFrame

import pandas as pd
technologies={"Course":["Spark","PySpark","Hadoop","Python","Pandas","Orcale","Java"],
              "Fee":[20000,25000,26000,22000,24000,21000,22000],
              "Duration":["30Days","40Days","35Days","40Days","60Days","50Days","55Days"],
              "Discount":[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
df = pd.DataFrame(technologies)
print(df.dtypes)
print(df)
#Convert all types to best possible types 
df2 = df.convert_dtypes()
print(df2.dtypes)

#Change all columns to same data type 
df = df.astype(str)
print(df.dtypes)

###################

#Change type for one or multiple columns
df=df.astype({"Fee":int,"Discount":float})
print(df.dtypes)

##########################

#Convert Data Type for all colums in list
df = pd.DataFrame(technologies)
df.dtypes
cols = ["Fee","Discount"]
df[cols] = df[cols].astype("float")
df.dtypes

#Ignores error
df = df.astype({"Course":int},errors = "ignore")
df.dtypes

#Generates error 
df = df.astype({"Course":int},errors = "raise")
df.dtypes

#Convert feed column to numeric type
df = df.astype(str)
print(df.dtypes)
df["Discount"] = pd.to_numeric(df["Discount"])
df.dtypes

import pandas as pd
technologies={"Course":["Spark","PySpark","Hadoop","Python","Pandas","Orcale","Java"],
              "Fee":[20000,25000,26000,22000,24000,21000,22000],
              "Duration":["30Days","40Days","35Days","40Days","60Days","50Days","55Days"],
              "Discount":[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
df = pd.DataFrame(technologies)
df
#################################
#conert DataFrame to csv
df.to_csv("data_file.csv")

#Crerate DataFrame from CSV file 
df2 = pd.read_csv("data_file.csv")
print(df2)
################################

#Pandas DataFrame - Basic Operations
#Create DataFrame with None/Null to work with examples 

import pandas as pd
import numpy as np

technologies= ({"Course":["Spark","PySpark","Hadoop","Python","Pandas",None,"Orcale","Java"],
              "Fee":[20000,25000,26000,22000,24000,np.nan,21000,22000],
              "Duration":["30Days","40Days","35Days","","40Days","60Days","50Days","55Days"],
              "Discount":[11.8,23.7,13.4,15.7,12.5,25.4,18.4,11.6]
              })

row_labels = ["r0","r1","r2","r3","r4","r5","r6","r7"]
df = pd.DataFrame(technologies, index= row_labels)
print(df)

""" 5 April 2024 """

#DataFrame properties
df.shape
#8,4
df.size
#32
df.columns
df.columns.values
df.index
df.dtypes
df.info

#############################
#Accessing one column content 
df["Fee"]
#Accessing two columns contents 
cols = ["Fee","Duration"]
df[cols]

#Another way
df[['Fee','Duration']]

#Select certain rows and assign it to another DataFrame
df2 = df[6:]
df2

df2 = df[:6]
df2

#df2 = df[6:8]
#df2 SAME RESULT

############################
#Accessing certain cell from column 'duration'

df['Duration'][3]
df['Duration'][4]

#Subtrating specific value from a column
df['Fee'] = df['Fee'] - 500
df['Fee']
#Pandas to manipulate DataFrame
#Describe DataFrame 
#Describe DataFrame foe all numeric columns 

df.describe()
#It will show 5 number summary
#####################################

#rename() -Rename pandas DataFrame columns
df = pd.DataFrame(technologies, index = row_labels)

#Assign new header by setting new column names.

df.columns = ['A','B','C','D']
df
########################################
#Rename Column Names Using rename() method
df = pd.DataFrame(technologies, index = row_labels)
df.columns = ['A','B','C','D']
df2 = df.rename({'A':'c1','B':'c2'},axis=1)
df2 = df.rename({'C':'c3','D':'c4'},axis='columns')
df2 = df.rename(columns={'A':'c1','B':'c2'})
################################
#Drop DataFrame Rows abd Columns
df = pd.DataFrame(technologies, index = row_labels)

#Drop rows by labels
df1 = df.drop(['r1','r2'])
df1

#Delet rows by position/index
df1 = df.drop(df.index[1])
df1

df1 = df.drop(df.index[[1,3]])
df1

#Delete Rows by Index Range
df1 = df.drop(df.index[2:])
df1

#When you have default indexes for rows 
df = pd.DataFrame(technologies)
df1 = df.drop(0)
df1

df = pd.DataFrame(technologies)
df1 = df.drop([0,3],axis=0)#It will delete row0 and row3
df1


df1 = df.drop(range(0,2))#It will delete 0 and 1
df1

######################################

""" 16 April 2024 """

# Pandas Shuffle Dataframe Rows
import pandas as pd 
technologies={'courses':["spark","Pyspark","Hadoop","Python","pandas","oracle","Java"],
              'Fee':[20000,25000,26000,22000,21000,22000,28000],
              'Duration':['30days','40days','35days','40days','60days','50days','55days'],
              'Discount':[1000,2300,1500,1200,2500,2100,2000]}
df=pd.DataFrame(technologies)
print(df)
#########################################
#pandas shuffle DataFrame Rows
#shuffle the DataFrame rows And retun all columns 

df1=df.sample(frac=1)
print(df1)
##############################+
#create a new index starting from zero
df1=df.sample(frac=1).reset_index()
print(df1)
###################

import pandas as pd 
technologies={'courses':["spark","Pyspark","Python","pandas"],
              'Fee':[20000,25000,22000,30000],
              'Duration':['30days','40days','35days','50days'],}
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)

technologies2={ 'courses':['spark','java','python','go'],
               'Discount':[2000,2300,1200,2000]}
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index_labels2)

### pandas join 

df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)
##########################################

### pandas inner join DataFrames 
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='inner')
print(df3)
########################

# pandas left join DataFrames
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='left')
print(df3)
################################

# pandas right join DataFrames 
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='right')
print(df3)
####################################

# Pandas Merge DataFrames
import pandas as pd 
technologies={'courses':["spark","Pyspark","Python","pandas"],
              'Fee':[20000,25000,22000,30000],
              'Duration':['30days','40days','35days','50days'],}
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)

technologies2={ 'courses':['spark','java','python','go'],
               'Discount':[2000,2300,1200,2000]}
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index_labels2)

## using pandas.merge()
df3=pd.merge(df1,df2)

## using DatFrame.merge()
df3=df1.merge(df2)
#########################################3

# use pandas.concat() to concat to DataFrames
import pandas as pd
df=pd.DataFrame({'courses':["spark","Pyspark","Python","pandas"],
                 'Fee':[20000,25000,22000,30000]})
df1=pd.DataFrame({'courses':["pandas","hadoop","hyperion","java"],
                 'Fee':[25000,25200,24500,24900]})
                 
## using pandas.concat() to conect two DataFrames
data=[df,df1]
df2=pd.concat(data)
df2
########################################
## concatenate Multiple DataFrames Using pandas.concat()

import pandas as pd 
df=pd.DataFrame({'courses':["spark","Pyspark","Python","pandas"],
                 'Fee':['20000','25000','22000','30000']})
df1=pd.DataFrame({'courses':["pandas","hadoop","hyperion","java"],
                 'Fee':['25000','25200','24500','24900']})
df2=pd.DataFrame({'Duration':['30days','40days','35days','60days','55days'],
                  'Discount':[1000,2300,2500,2000,3000]})

## Appending multiple DataFrame 
df3=pd.concat([df,df1,df2])
print(df3)
#########################

""" 18 April 2024 """

#Read Excel file
import pandas as pd 
df = pd.read_excel('C:/DataScience/1-AdvancedPython/data_file.csv')
print(df)

##############################
df.to_excel('C:/DataScience/1-AdvancedPython/data_file.csv')
print(df)

#Using Series.values.tolist()
col_list = df.courses.values
print(col_list)
col_list = df.courses.values.tolist()
print(col_list)

#Using Series.values.tolist()
col_list = df["courses"].values.tolist()
print(col_list)

#Using list() function 
col_list = list(df["courses"])
print(col_list)

#Convert to numpy array
col_list = df["courses"].to_numpy()
print(col_list)






















