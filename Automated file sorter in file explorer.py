#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os,shutil


# In[12]:


path = r"C:/Users/H Vamshi/Downloads/python tutorials/"


# In[17]:


file_name = os.listdir(path)


# In[27]:


folder_names = ['image files','text files']

for loop in range(0,2):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])
for file in file_name:
    if".png" in file and not os.path.exists(path + "image files/"+ file):
        shutil.move(path + file , path+ "image files/"+  file )
    elif".txt" in file and not os.path.exists(path + "text files/"+ file):
        shutil.move(path + file , path+ "text files/"+   file )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




