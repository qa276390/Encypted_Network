
# coding: utf-8

# In[1]:


from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import json
import time
import matplotlib.pyplot as plt
import sys
import os.path

# In[2]:


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
    

# In[32]:


def main():

    inputfile=sys.argv[1]
    print('python input:',inputfile)
    data = read_json_fun(inputfile)
    outputfile=sys.argv[2]   
    print('python output:',outputfile)
    fn=os.path.basename(inputfile)
    title=os.path.splitext(fn)[0]
    title=title.upper()
    
    pktin=[]
    pktout=[]
    time=[]
    print(len(data))
    for i in range(1,len(data)):
        #print('i = ')
        #print(i)
        d=json.dumps(data[i], indent=4)
        #print(d)
        #print(data[i]['time_start'])
        #num_pkts_in = data[i]['num_pkts_in']
        
        #num_pkts_in = data[i]['num_pkts_out']
        packets = data[i]['packets']
        #print(packets)
        #pktlist = packets.split('},{')
        time_start = data[i]['time_start']
        #pktlist[0] = pktlist[0] + '}'
        #pktlist[len(pktlist)-1] = '{' + pktlist[len(pktlist)-1]
        #for j in range(2, len(pktlist)-1):
        #    pktlist[j] = '{' + pktlist[j] + '}'
        for j in range(len(packets)):
            #tmp = json.loads(packets[j])
            if j==0 :
                time.append(data[i]['time_start'])
            else:
                time.append(time[len(time)-1] + packets[j]['ipt']/1000.0)
            if packets[j]['dir'] == '>':
                pktout.append(packets[j]['b'])
                pktin.append(0)
            else:
                pktin.append(-packets[j]['b'])
                pktout.append(0)
            
            
        
        
        #print(data[i]['num_pkts_out'])
        
        #if 'num_pkts_in' in data[i]:
        #    print(data[i]['num_pkts_in'])
        #    pktin.append(-data[i]['bytes_in'])
        #else:
        #    pktin.append(0)
    
    
   # print('--------------------------------------------------------')
    #time=np.array(time)
    #print(np.shape(time))
    print(len(time))
    print('plot')
    #newdata = numpy.memmap(time, pktout)
    plt.bar(time[1:10000],pktout[1:10000],facecolor='#ff4500',edgecolor='#ff4500',label="bytes_out")
    print('plot out')
    #plt.bar(time,pktin,facecolor='green',edgecolor='green',label="bytes_in")
    print('plot in')
    plt.xlabel("Time(s)")
    plt.ylabel("Packet_Length(bytes)")

    plt.title(title)
    plt.grid()
    #plt.ylim(-1.2,1.2)
    plt.legend()
    #plt.savefig(outputfile,dpi=200)
    plt.show()


    


# In[33]:


if __name__ == "__main__":
    main()


# In[5]:


# In[10]:





