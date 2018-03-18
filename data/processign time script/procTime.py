
# coding: utf-8

# In[1]:


import sys
import pandas as pd


# In[40]:


def main():

    print("Enter:")
    print("experiment number, exp1 or exp2")
    print("experiment sub type: base,p4,nfv")
    print("number of main experiments: l1,l2,l3.")
    print("number of sub experiments: 1,2,3,4...10")
    print("file type: csv,txt")

    _exp_main_type = 1
    _exp_sub_type = "p4"
    _num_of_main_exp = 1
    _num_of_sub_exp = 1
    _file_format = "csv"
    _file_path="/Users/sparta/Google Drive/courses-projects/Student Assist/Labs/P4/data/processign time script/"

    for i in range(1,_num_of_main_exp+1):
        for j in range(1,_num_of_sub_exp+1):
            _tx_file = "exp"+str(_exp_main_type)+"_"+_exp_sub_type+"_"+"tx"+"_"+"l"+str(i)+"_"+str(j)+"."+_file_format
            _rx_file = "exp"+str(_exp_main_type)+"_"+_exp_sub_type+"_"+"rx"+"_"+"l"+str(i)+"_"+str(j)+"."+_file_format
            print(_tx_file)
            print(_rx_file)
            data = pd.read_csv(_file_path+_tx_file, sep=' ,\s+',engine='python')
            
            print(data.head())
            
            
        



# In[41]:



if __name__ == "__main__":
    main()

