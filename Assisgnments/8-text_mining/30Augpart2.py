# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:21:16 2024

@author: yashd
"""

from bs4 import BeautifulSoup as bs
import requests
link = "https://sanjivanicoe.org.in/index.php/contact "
page = requests.get(link)
page
# Response [200]
page.content
# You will get all html source code but very crowdy text
# Let us apply html parser
soup = bs(page.content,'html.praser')
soup
# Now the text is clean but not upto the exceptation 
#now let us apply prettify method 
print(soup.prettify())
# The text is not clean
list (soup.children)
#Finding all contents using tab
soup.find_all('p')
#Suppose you want to extract contents from 
#first row