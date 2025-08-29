# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:53:36 2024

@author: yashd
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(open("C:/8-text_mining/sample_doc.html"))
print(soup)
# It is going to show all the html contents extracted 
soup.text
# It will show only text 
soup.contents
#It is going to show all the html contents extracted 
soup.find('address')
soup.find_all('address')
soup.find_all('q')
soup.find_all('b')                   
table=soup.find_all('table')
table
for row in table.find_all('tr'):
    columns=row.find_all('td')
    print(columns)  

    
# It will show all the rows except first row 
# Now we want to display M.tech which is located in third row 
# I need to give [3][2]
table.find_all('tr')[3].find_all('td')[2]    
    
    
    
    
