
# coding: utf-8

# In[1]:


import sys
from pathlib import Path
import re


# In[2]:


def read_file(file_path):
    content=[]
    my_file = Path(file_path)
    if not my_file.is_file():
        return False
    else:
        with open(my_file) as f:
            content = f.readlines()
    return content        


# In[3]:


def write_file(contents, file_path):
    my_file = Path(file_path)
    if my_file.is_file():
        with open(my_file, "w") as f:
            for line in contents:
                f.write(line)


# In[4]:


def remove_from_file(file_path, chars):
    content = read_file(file_path)   

    for char in chars:
        content = [x.replace(char, "") for x in content]
    write_file(content,file_path)    

    return True;


# In[5]:


def remove_line_from_file(file_path, matches, contains_flag):
    content = read_file(file_path)
    result =[]
    for line in content:
        if contains_flag and any(i in line for i in matches) :           
            result.append(line)
        if not contains_flag and not any(i in line for i in matches) :           
            result.append(line)

    write_file(result, file_path)
    return True
    


# In[6]:


#remove_line_from_file("/Users/sparta/Google Drive/courses-projects/Student Assist/Labs/processign time script/data/base/exp1_base_rx_l1_1.csv",["request"],True)

