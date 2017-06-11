
# coding: utf-8

# #1

# In[1]:

june_1="http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/01/20-00"
june_2="http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/02/20-00"
june_3="http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/03/20-00"
june_4="http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/04/20-00"
june_5="http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/05/20-00"
june_6="http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/06/20-00"
june_7="http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/07/20-00"
date_list=[june_1, june_2, june_3, june_4, june_5, june_6, june_7]


# In[2]:

import pandas as pd


# In[9]:

for url in date_list:
    rates=pd.read_html(url)
    rate=rates[2]
    print(rate[2:19])


# #2

# In[18]:

import re
import requests
url_snp="https://www.bloomberg.com/quote/SPX:IND"
response_snp=requests.get(url_snp)
snp_page=response_snp.text
data = re.sub(r'<|>'," ",snp_page)
output=re.findall('"price"\s*([0-9]\S*)',data)
print output


# #3

# In[12]:

import json
input='''[
    {
    "Movie":"Game of Thrones",
    "Actor":"Peter Dinklage",
    "Role":"Tyrion Lannister"    
    },
    {
    "Movie":"Vikings",
    "Actor":"Travis Fimmel",
    "Role":"Ragnar Lothbrok"  
    },
    {
    "Movie":"The last Kingdom",
    "Actor":{
            "Young Uhtred":"Tom Taylor",
            "Not that young Uhtred":"Alexander Dreymon"
            },
    "Role":"Uhtred of Bebbanburg"
    }
]'''
inpt=json.loads(input)
for x in inpt:
        print"Movie:", x['Movie']
        print "Role:", x["Role"]
        if type(x["Actor"]) == dict:
                print "Actor 1: " , x["Actor"]['Young Uhtred']
                print "Actor 2: " , x["Actor"]['Not that young Uhtred']
        else:
            print "Actor:", x["Actor"], "\n"


# #4

# In[16]:

import pandas as pd
import matplotlib.pyplot as plt
data_csv = pd.read_csv("AirPassengers.csv")
print data_csv.head(144)
plt.plot(data_csv['Passengers'])
plt.show()


# #5

# In[15]:

import re
import requests
url="http://quotes.toscrape.com/"
response=requests.get(url)
page=response.text
data = re.sub(r'"|<|>'," ",page)
output=re.findall("href=\s*(\S*)\s*next",data,re.IGNORECASE)
print "http://quotes.toscrape.com"+output[0]


# In[ ]:



