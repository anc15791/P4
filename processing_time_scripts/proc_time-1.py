
# coding: utf-8

# In[13]:


import sys
import pandas as pd
from util import *
from datetime import datetime
import numpy as nm
import statistics


# In[14]:


def map_times(data_rx, data_tx):

    
    for index, row in data_tx.iterrows():
        tx = data_tx[['seq', 'time']]
        
    
    tx_time = tx.values.tolist()
    rx_time = []
    for match in tx_time:
        rx_time.append((data_rx.loc[data_rx['seq'] == match[0]])[['seq', 'time']].values.tolist())    
    process_time_data = []  
    process_times=[]
    
    #print(rx_time)
    #print(tx_time)
    
    for i in range(0,len(tx_time)):
        
        if tx_time[i][0] == rx_time[i][0][0]:
            lst = [tx_time[i][0], tx_time[i][1], rx_time[i][0][1]]
            FMT = '%H:%M:%S.%f'
            timediff = (datetime.strptime(lst[1], FMT) - datetime.strptime(lst[2], FMT)).microseconds
            if timediff >= 0 :
                lst.append(timediff)
                process_times.append(timediff)
            process_time_data.append(lst)
    
    return process_time_data,process_times


# In[15]:


def main():

    print("Enter:")
    print("experiment number, exp1 or exp2")
    print("experiment sub type: base,p4,nfv")
    print("number of main experiments: l1,l2,l3.")
    print("number of sub experiments: 1,2,3,4...10")
    print("file type: csv,txt")

    _exp_main_type = 1
    _exp_sub_type = "nfv"
    _num_of_main_exp = 5
    _num_of_sub_exp = 1
    _file_format = "csv"
    _file_path="/Users/sparta/Google Drive/courses-projects/Student Assist/Labs/processign time script/data/nfv/"
    print(_file_path)
    for i in range(1,_num_of_main_exp+1):
        
        exp_result=["exp"+str(_exp_main_type)+"_"+_exp_sub_type+"_"+"l"+str(i),0.0,0.0,0.0,0.0]
        
        for j in range(1,_num_of_sub_exp+1):
            _tx_file = "exp"+str(_exp_main_type)+"_"+_exp_sub_type+"_"+"tx"+"_"+"l"+str(i)+"_"+str(j)+"."+_file_format
            _rx_file = "exp"+str(_exp_main_type)+"_"+_exp_sub_type+"_"+"rx"+"_"+"l"+str(i)+"_"+str(j)+"."+_file_format
            #print(""+ _file_path + _tx_file)
            #print("" + _file_path + _rx_file)
            rem_char_match = [",","->"]
            rem_line_if_not_match = ["ICMP","Echo"]
            rem_line_if_match = ["reply"]
            if not remove_from_file(_file_path+_tx_file,rem_char_match) or not remove_from_file(_file_path+_rx_file,rem_char_match):
                  print("files could not be cleaned, error in remove_from_file")
                  sys.exit()
             
            if not remove_line_from_file(_file_path+_tx_file,rem_line_if_not_match,True) or not remove_line_from_file(_file_path+_rx_file,rem_line_if_not_match,True):
                  print("files could not be cleaned, error in remove_line_from_file:true")
                  sys.exit()
            
            if not remove_line_from_file(_file_path+_tx_file,rem_line_if_match,False) or not remove_line_from_file(_file_path+_rx_file,rem_line_if_match,False):
                  print("files could not be cleaned, error in remove_line_from_file:false")
                  sys.exit()
            
            col_names=['sr.no','date','time','srcip','dstip','protocol','ptype1','ptype2','ptype3','id','seq','ttl','srcmac','dstamc']
            data_tx = pd.read_csv(_file_path+_tx_file, delim_whitespace=True, names=col_names, header=None,index_col=0, engine='python')
            data_tx=data_tx.dropna(axis=1,how='all') 
            #data_tx=data_tx.drop(columns=['->', '-->'])
            
            data_rx = pd.read_csv(_file_path+_rx_file, delim_whitespace=True, names=col_names, header=None,index_col=0, engine='python')
            data_rx=data_rx.dropna(axis=1,how='all')
            #data_rx=data_rx.drop(columns=['->', '-->'])
            
            
            
            #with pd.option_context('display.max_rows', None, 'display.max_columns', 25):
            #    display(data_tx)
            #    display(data_rx)
            
            _tx_rx_data, timediffs  = map_times(data_rx, data_tx)
   
            avg = nm.mean(timediffs)
            median = statistics.median(timediffs)
            maximum = max(timediffs)
            minimum = min(timediffs)
            lst = ["exp"+str(_exp_main_type)+"_"+_exp_sub_type+"_"+"l"+str(i)+"_"+str(j),avg,median,maximum,minimum]
            print(lst)
            
            exp_result[1] = exp_result[1]+avg
            exp_result[2] = exp_result[2]+median
            exp_result[3] = exp_result[3]+maximum
            exp_result[4] = exp_result[4]+minimum
           
        
        exp_result[1] = exp_result[1]/_num_of_sub_exp
        exp_result[2] = exp_result[2]/_num_of_sub_exp
        exp_result[3] = exp_result[3]/_num_of_sub_exp
        exp_result[4] = exp_result[4]/_num_of_sub_exp
        
        print(exp_result)
            
            
        



# In[16]:



if __name__ == "__main__":
    main()

