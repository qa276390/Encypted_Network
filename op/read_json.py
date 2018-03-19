
# coding: utf-8

# In[1]:


#from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import json
import time
import matplotlib.pyplot as plt
import sys
import os.path
# In[3]:


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


# In[4]:
if __name__ == "__main__":

    inputfile=sys.argv[1]
    print('python input:',inputfile)
    data = read_json_fun(inputfile)
    outputfile=sys.argv[2]   
    print('python output:',outputfile)
    fn=os.path.basename(inputfile)
    title=os.path.splitext(fn)[0]
    title=title.upper()
    # In[5]:


    #data=np.array(data)
    #print(data)


    pktin=[]
    pktout=[]
    time=[]

    for i in range(1,len(data)):
        d=json.dumps(data[i], indent=4)
        #print(d)
        #print(data[i]['time_start'])
        time.append(data[i]['time_start'])
        #print(data[i]['num_pkts_out'])
        pktout.append(data[i]['bytes_out'])
        if 'num_pkts_in' in data[i]:
            #print(data[i]['num_pkts_in'])
            pktin.append(-data[i]['bytes_in'])
        else:
            pktin.append(0)
        
        
        #print('--------------------------------------------------------')

    plt.bar(time,pktout,facecolor='#ff4500',edgecolor='#ff4500',label="bytes_out")
    plt.bar(time,pktin,facecolor='green',edgecolor='green',label="bytes_in")

    plt.xlabel("Time(s)")
    plt.ylabel("Packet_Length(bytes)")
    plt.title(title)
    plt.grid()
    #plt.ylim(-1.2,1.2)
    plt.legend()
    plt.savefig(outputfile,dpi=200)
    #plt.show()

    sys.exit(0)

