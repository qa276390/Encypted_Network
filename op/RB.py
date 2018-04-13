
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

#--------------------RB------------------
def http(i,data,df):
    http_col = ['http_content_type','http_user_agent','http_accept_language','http_server','http_code']
    if data.__contains__("http"):
        http = data['http'][0]
        if http.__contains__('in'):
            code = False
            server = False
            content = False
            for element in http['in']:
                if element.__contains__("code"):
                    df.loc[i,'http_code'] = element['code']
                    code = True
                if element.__contains__("Server"):
                    df.loc[i,'http_server'] = element["Server"]
                    server = True
                if element.__contains__("Content-Type"):
                    df.loc[i,'http_content_type'] = element['Content-Type']
                    content = True
            if not code:
                df.loc[i,'http_code'] = 'NULL'
            if not server:
                df.loc[i,'http_server'] = 'NULL'
            if not content:
                df.loc[i,'http_content_type'] = 'NULL'

        else:
            in_col = ['http_content_type','http_server','http_code']
            df.loc[i,in_col] = 'NULL'
        if http.__contains__('out'):
            agent = False
            lang = False
            for element in http['out']:
                if element.__contains__("User-Agent"):
                    df.loc[i,'http_user_agent'] = element["User-Agent"]
                    agent = True
                if element.__contains__("Accept-Language"):
                    df.loc[i,'http_accept_language'] = element["Accept-Language"]
                    lang = True
            if not agent:
                df.loc[i,'http_user_agent'] = 'NULL'
            if not lang:
                df.loc[i,'http_accept_language'] = 'NULL'
        else:
            out_col = ['http_user_agent','http_accept_language']
            df.loc[i,out_col] = 'NULL'
    else:
        df.loc[i,http_col] = 'NULL'
    return 

def dns(i,data,df):
    dns_col = ['dns_domain_name','dns_ttl','dns_num_ip','dns_domain_rank']
    if data.__contains__("linked_dns"):
        dns = data['linked_dns']
        num_ip = 0

        if dns.__contains__('dns'):
            if dns['dns'][0].__contains__('rn'):
                df.loc[i,'dns_domain_name'] = dns['dns'][0]['rn']
            else:
                df.loc[i,'dns_domain_name'] = 'NULL'
            if dns['dns'][0].__contains__('rr'):
                lis = dns['dns'][0]['rr']
                ttl = -1
                for element in lis:
                    if ttl == -1 and element.__contains__('cname'):
                        ttl = element['ttl']
                    if element.__contains__('a'):
                        num_ip+=1
                if ttl == -1:
                    df.loc[i,'dns_ttl'] = 'NULL'
                else:
                    df.loc[i,'dns_ttl'] = ttl
                    
                df.loc[i,'dns_num_ip'] = num_ip
                df.loc[i,'dns_domain_rank'] = 'NULL'
            else:
                dns_col = ['dns_ttl','dns_num_ip','dns_domain_rank']
                df.loc[i,dns_col] = 'NULL'
        else:
            df.loc[i,dns_col] = 'NULL'
    else:
        df.loc[i,dns_col] = 'NULL'
    return 
    #--------------------RB------------------
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
    for i in range(1,len(data)):
        #--------------------KL------------------
        d=json.dumps(data[i], indent=4)
        #print(d)
        if data[i].__contains__('packets'):
            '''
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

            '''
        http(i,data[i],df)
        dns(i,data[i],df)
    
    out_file = 'db.csv'
    if(os.path.isfile(out_file)):
        df.to_csv(out_file, mode = 'a',header = False)
    else:
        df.to_csv(out_file, header = col)

# In[78]:


if __name__ == "__main__":
    Generator()

