# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:07:44 2024

@author: yash
"""
import re
def get_pattern_match(pattern,text):
    matches = re.findall(pattern,text)
    if matches :
        return matches[0]
        
get_pattern_match('order[^\d]*(\d*)', chat1)
chat1 = 'you ask lot of questions 1235678912, abc@xyz.com'
chat2 = 'here it is: (123)-567-8912, abc@xyz.com'
chat3 = 'yes, phone: 1235678912 email: abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat2)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)

##################################################
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat1)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat2)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat3)

#####################################################
text = '''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partners	
Grimes (2018–2021)[1]
Children	11[a][3]
Parents	
Errol Musk
Maye Musk

'''
get_pattern_match(r'age (\d+)', text)
get_pattern_match(r'Born(.*)\n', text).strip()
get_pattern_match(r'Born.*\n(.*)\(age', text).strip()
get_pattern_match(r'\(age.*\n(.*)', text)

####################################################
" 19 June 2024 "

def extra_personal_information (text):
    age = get_pattern_match(r'age (\d+)', text)
    full_name = get_pattern_match(r'Born(.*)\n', text).strip()
    birth_date = get_pattern_match(r'Born.*\n(.*)\(age', text).strip()
    birth_place = get_pattern_match(r'\(age.*\n(.*)', text)
    return {
        'age': int(age),
        'name': full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()       
        }

extra_personal_information (text)
####################################################
import re
text = '''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 67)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''
extra_personal_information (text)

################################################
" 20 jUNE 2024 "
import re
sentence5 = ' shatrat twitted , Wittnesing 68th republic day India from rajpath , \new Delih, Mesmorising performance by Indian army ! '
re.sub(r'([^\s\w]|_)+','',sentence5).split()

################################################

'''
re.sub(r'([^\s\w]|_)+', ', some_string)
will replace sequences 
of non-alphanumeric characters
(including punctuation but excluding whitespace)
 with a single space. This is commonly used to clean
 up te by removing punctuation and othe 
 non-word characters,making it easier to 
 process for tasks like text analysis or 
 machine Learning.
 
'''
###############################################
import re
def n_gram_extraction (input_str,n):
    tokens = re.sub(r'([^\s\w]|_)+', ' ',input_str).split()
    for i in range (len(tokens)-n+1):
        print(tokens[i:i+1])
    
n_gram_extraction("The cute little boy is playing with kitten ",2)
n_gram_extraction("The cute little boy is playing with kitten ",3)

################################################
text = '''
Follow our leader elon musk on twitter here  https://twitter.com/elonmusk
and teslas product can found at https://www.tesla.com/
https://twitter.com/trslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla

'''
pattern = " https://twitter.com/([a-zA-Z0-9_]+)"

re.findall(pattern,text)

#######################################
text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject
 us to a concentra restricted cash,
 accounts receivable, convertible note hedges,
 ar or on deposit at high credit quality
 financial institutions in th and 
 December 31, 2020, no entity represented 10% 
 or more of our ו hedges and interest rate swaps 
 is mitigated by transacting with s
Concentration of Risk: Supply Risk
We are dependent on our suppliers, 
including single source suppl products in a 
timely manner at prices, quality levels and
 volumes suppliers, could have a material 
 adverse effect on our business, 
 '''
pattern = 'Concentration of Risk : ([^\n]*)'

re.findall(pattern,text)

#################################################
text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''
pattern = 'FY(\d{4} (?: Q[1 - 4] / S * [1 - 2] )) ' 
matches = re.findall(pattern, text) # ?: match this and | a or b
matches

#################################################
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10'
matches = re.findall(pattern, text) 
matches

##################################################
text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''
pattern = 'Note \d - ([^\n]*)'

matches = re.findall(pattern, text) 
matches

###########################################
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern = 'FY\d{4} Q[1-4]'
matches = re.findall(pattern, text) 
matches

###########################################
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern = 'FY\d{4} Q[1-4]'
matches = re.findall(pattern, text, flags=re.IGNORECASE) 
matches

