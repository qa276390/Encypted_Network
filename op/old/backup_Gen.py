
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



def Generator():
    #df = pd.read_excel('Markov.xlsx')
    col = ['type','sa','da','sp','dp','pr','tls_scs','tls_ext_server_name','tls_c_key_length','http_content_type','http_user_agent','http_accept_language','http_server','http_code','dns_domain_name','dns_ttl','dns_num_ip','dns_domain_rank']
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
    print('file = ',title)
    Type = Catgo(title)
    print('type = ',Type)
    time=[]
    num = 0
    for i in range(len(data)):
        
    #---------------------KL-------------------------#
        Basic_Info(data, i, df, Type)
        Marcov(data, i, df)
    
    out_file = 'db.csv'
    if(os.path.isfile(out_file)):
        df.to_csv(out_file, mode = 'a',header = False)
    else:
        df.to_csv(out_file, header = col)

def Basic_Info(data, i, df, Type):

    if data[i].__contains__('sa'):
        df.loc[i,'sa'] = data[i]['sa']
    else:    
        df.loc[i,'sa'] = 'NULL'

    if data[i].__contains__('da'):
        df.loc[i,'da'] = data[i]['da']
    else:    
        df.loc[i,'da'] = 'NULL'
    
    if data[i].__contains__('sp'):
        df.loc[i,'sp'] = data[i]['sp']
    else:    
        df.loc[i,'sp'] = 'NULL'
    
    if data[i].__contains__('dp'):
        df.loc[i,'dp'] = data[i]['dp']
    else:    
        df.loc[i,'dp'] = 'NULL'
    
    if data[i].__contains__('pr'):
        df.loc[i,'pr'] = data[i]['pr']
    else:    
        df.loc[i,'pr'] = 'NULL'
    
    df.loc[i,'type'] = Type

def Catgo(t):
    t = t.lower()

    if (t.find('email') !=  -1):
        return 'email'
    elif(t.find('chat') !=  -1):
        return 'chat'
    elif(t.find('youtube')!=-1 or t.find('vimeo')!=-1 or t.find('video')!=-1 or t.find('netflix')!=-1 or t.find('spotify')!=-1 ):
        return 'stream'
    elif(t.find('ftp')!=-1 or t.find('scp')!=-1 or t.find('file')!=-1):
        return 'file_trans'
    elif(t.find('audio')!=-1 or t.find('voip')!=-1):
        return 'voip'
    elif(t.find('torrent')):
        return 'trap2p'
    else:
        print('browsing?')
        return 'browsing'


def Marcov(data, i, df):

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

if __name__ == "__main__":
    Generator()

