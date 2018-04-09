
# coding: utf-8

# In[48]:


from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import json
import time
import matplotlib.pyplot as plt
import sys
import os.path


# In[49]:


def read_json_fun(file):
    data = []
    temp = []
    data_str = open(file).read()
    temp = data_str.splitlines()
    num = len(temp)
    for i in range(num):
        str = temp[i]
        data.append(json.loads(str))
    return data


# In[50]:

'''
def read_csv(file):
    return pd.read_excel(file)
'''

# In[77]:


def Generator():
    #df = pd.read_excel('Markov.xlsx')
    col = ['sa','da','sp','dp','pr','tls_scs','tls_ext_server_name','tls_c_key_length','http_content_type','http_user_agent','http_accept_language','http_server','http_code','dns_domain_name','dns_ttl','dns_num_ip','dns_domain_rank']
    for i in range(20):
        for j in range(20):
            splt_str = 'splt_' + str(i) + '_' + str(j) 
            col.append(splt_str)

    for i in range(256):
        dist_str = 'dist_' + str(i)
        col.append(dist_str)
    col.append('entropy')

    df = pd.DataFrame(columns = col)

    print(df.columns)

    #print(df)
    inputfile=sys.argv[1]
    #inputfile = 'aim_chat_3a.txt'
    print('python input:',inputfile)
    data = read_json_fun(inputfile)
    fn=os.path.basename(inputfile)
    title=os.path.splitext(fn)[0]
    print(title)
    
    pktin=[]
    pktout=[]
    time=[]
    num = 0
    for i in range(len(data)):
        d=json.dumps(data[i], indent=4)
        #print(d)
        if data[i].__contains__('packets'):
            #print(1)
            packets = data[i]['packets']
            clas = []
            count = [[0]*20 for i in range(20)]
            matrix = [[0]*20 for i in range(20)]
            #print(len(packets))
            if len(packets) > 1:
                #print(len(packets))
                for j in range(len(packets)):
                    if packets[j].__contains__('b'):
                        byte = packets[j]['b']
                        if packets[j]['dir'] == '>':
                            if byte == 1500:
                                clas.append(9)
                            elif byte < 1500:
                                clas.append(int(byte/150))
                        else:
                            if byte == 1500:
                                clas.append(19)
                            elif byte < 1500:
                                clas.append(int(byte/150)+10)
                for j in range(len(clas)-1):
                    count[clas[j+1]][clas[j]] += 1
                total = 0
                for j in range(20):
                    for k in range(20):
                        total = total + count[j][k]
                for j in range(20):
                    for k in range(20):
                        if total > 0:
                            matrix[j][k] = count[j][k]/total
                array = []
                #array.append(title + '_' + str(num))
                for j in range(20):
                    for k in range(20):
                 #       array.append(matrix[j][k])  
                        splt_str = 'splt_' + str(j) + '_' + str(k) 
                        df.loc[i,[splt_str]] = matrix[j][k]
                            
    
    out_file = 'db.csv'
    if(os.path.isfile(out_file)):
        df.to_csv(out_file, mode = 'a',header = False)
    else:
        df.to_csv(out_file, header = col)

# In[78]:


if __name__ == "__main__":
    Generator()

