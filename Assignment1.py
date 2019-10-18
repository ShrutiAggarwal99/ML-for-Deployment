#!/usr/bin/env python
# coding: utf-8

# # ML for deployment Assignment 1 

# # TASK 1

# In[1]:


for i in range(2000,3200):
    if i%5!=0 and i%7==0:
        print(i,",",end='')


# In[2]:


f_name = input("tell me your first name : ")
l_name = input("tell me your last name : ")
print(f_name[::-1]+" "+l_name[::-1])


# In[3]:


import numpy as np
r = 6
vol = (4*np.pi*(r**3))/3
print(vol)


# # TASK 2

# In[4]:


values = input("Input some comma separated numbers : ")
values = values.split(",")
print(values)


# In[5]:


for i in range(1,10):
    if i<=5:
        for j in range(0,i):
            print("*",end='')
        print()
    else:
        for j in range(10-i,0,-1):
            print("*",end='')
        print()


# In[6]:


word = input("tell me a word: ")
word = word[::-1]
print(word)


# In[7]:


str1 = "WE, THE PEOPLE OF INDIA,"
str2 = "having solemnly resolved to constitute India into a SOVEREIGN,"
str3 = "SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC "
str4 = "and to secure to all its citizens"

print(str1,"\n\t",str2,"!\n\t\t",str3,"\n\t\t ",str4)

