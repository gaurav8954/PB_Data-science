#!/usr/bin/env python
# coding: utf-8

# In[5]:


num = int(input('Enter no- '))
if num %2==0:
    print ("no in even-",num)


# In[3]:


a = int(input("Enter A- "))
b = int(input("Enter B - "))
c = int(input("Enter C - "))
if(a>=b & a>=c):
    print("A is big")
elif(b>=a & b>=c):
    print("B is big")
else:
    print("C is big")


# In[12]:


s = 'My name is gaurav'
s.split()


# In[14]:


Name = 'gaurav'
age = 20
Address = 'Mumbai'
print('hay {},ur age is {} and address is {}'.format(Name,age,Address))


# In[17]:


Z = 'Gaurav'
Z[3]


# In[21]:


List=[1,2,3,4,'h']
List[4]


# In[22]:


List.pop()


# In[23]:


List


# In[36]:


List1= [1,2,3,4,[3,4,5],8,9,[2.4,6]]
List1.append(7)


# In[37]:


List1


# In[ ]:


list=[]
dict={}
tuple=()
set={}


# In[38]:


set={1,2,3,'a','b','3',3}
set.add(8)
set


# In[33]:


tuple=(1,2,'p')
tuple


# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


Data = pd.DataFrame({'Name':['A','B','C'],
                    'Age':[24,45,34]})
Data


# In[3]:


Data['Age'].hist()


# In[ ]:




