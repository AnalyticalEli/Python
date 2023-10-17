#!/usr/bin/env python
# coding: utf-8

# In[1]:


#First we import os shutil

import os, shutil


# In[2]:


#Next we set the path variable equal to the path of the raw data

path = r'C:\Users\hands\OneDrive\Documents\Python Project #33/'


# In[3]:


#Next we set the file_name equal to the path

file_name = os.listdir(path)


# In[4]:


#Next we create a loop that will create files for respective folders in folder_name

folder_names = ['csv files', 'image files', 'text files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
    os.makedirs(path + folder_names[loop])


# In[5]:


#Next we create code that will move files:

for file in file_name:
    if ".xlsx" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    else:
        print("There were files in this path that were not moved!")
    

