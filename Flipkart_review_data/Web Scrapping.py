#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[2]:


url="https://www.flipkart.com"


# In[3]:


r=requests.get(url)
print(r)


# In[4]:


url="https://www.flipkart.com/search?q=mobile%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


# In[5]:


p=requests.get(url)
print(p)


# In[6]:


soup=BeautifulSoup(p.text,"lxml")


# In[7]:


np=soup.find("a",class_="_1LKTO3").get("href")
print(np)


# In[8]:


cnp="https://www.flipkart.com"+np
print(cnp)


# In[9]:


for i in range(2,10):
    url="https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    p=requests.get(url)
    soup=BeautifulSoup(p.text,"lxml")
    np=soup.find("a",class_="_1LKTO3").get("href")
    cnp="https://www.flipkart.com"+np
    print(cnp)


# In[36]:


Product_Name =[]
Price=[]
Description=[]
Reviews=[]
for i in range(2,10):
    url="https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    p=requests.get(url)
    soup=BeautifulSoup(p.text,"lxml")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
    names=box.find_all("div",class_='_4rR01T')
    for i in names:
        name=i.text
        Product_Name.append(name)
    #print(len(Product_Name)
    #print(Product_Name)
    names=box.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in names:
        name=i.text
        Price.append(name)
    #print(len(Price))
    #print(Price)
    names=box.find_all("ul",class_="_1xgFaf")
    for i in names:
        name=i.text
        Description.append(name)
    #print(len(Description ))
    #print(Description)
    names=box.find_all("div",class_="_3LWZlK")
    for i in names:
        name=i.text
        Reviews.append(name)
    #print(len(Reviews))
    #print(Reviews)


# In[16]:


names=box.find_all("div",class_="_4rR01T")
for i in names:
    name=i.text
    Product_Name.append(name)
print(Product_Name)


# In[23]:


names=box.find_all("div",class_="_30jeq3 _1_WHN1")
for i in names:
    name=i.text
    Price.append(name)
print(len(Price))
print(Price)


# In[28]:


names=box.find_all("ul",class_="_1xgFaf")
for i in names:
    name=i.text
    Description.append(name)
print(len(Description ))
print(Description)


# In[27]:


names=box.find_all("div",class_="_3LWZlK")
for i in names:
    name=i.text
    Reviews.append(name)
print(len(Reviews))
print(Reviews)


# In[37]:


df=pd.DataFrame({"Product Name":Product_Name,"Product_Price":Price,"Description":Description,"Review":Reviews  })
df


# In[ ]:




