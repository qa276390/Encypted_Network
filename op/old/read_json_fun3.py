
# coding: utf-8

# In[3]:


from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import json
import time
import matplotlib.pyplot as plt
import sys
import os.path


# In[4]:


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


# In[7]:


def main():

    inputfile=sys.argv[1]
    print('python input:',inputfile)
    data = read_json_fun(inputfile)
    outputfile=sys.argv[2]   
    print('python output:',outputfile)
    fn=os.path.basename(inputfile)
    title=os.path.splitext(fn)[0]
    title=title.upper()

    outputsplit=os.path.splitext(outputfile)
    
    pktin=[]
    pktout=[]
    time=[]

    for i in range(1,len(data)):
        d=json.dumps(data[i], indent=4)
        #print(d)
        packets = data[i]['packets']
        time_start = data[i]['time_start']
        for j in range(len(packets)):
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


    data_num = len(time)
    iter = int(data_num/10000)
    if iter == 0:
        plt.bar(time,pktout,facecolor='#ff4500',edgecolor='#ff4500',label="bytes_out")
        plt.bar(time,pktin,facecolor='green',edgecolor='green',label="bytes_in")
        plt.xlabel("Time(s)")
        plt.ylabel("Packet_Length(bytes)")

        plt.title(title)
        plt.grid()
        plt.legend()
        plt.savefig(outputfile,dpi=200)
    else:
        for i in range(1,iter+1):
            print(i)
            print('plot')
            plt.bar(time[(i-1)*10000:i*10000],pktout[(i-1)*10000:i*10000],facecolor='#ff4500',edgecolor='#ff4500',label="bytes_out")
            plt.bar(time[(i-1)*10000:i*10000],pktin[(i-1)*10000:i*10000],facecolor='green',edgecolor='green',label="bytes_in")
            plt.xlabel("Time(s)")
            plt.ylabel("Packet_Length(bytes)")

            plt.title(title)
            plt.grid()
            plt.legend()
            plt.savefig(outputsplit[0]+'_num_'+str(i)+'.png',dpi=200)
        plt.bar(time[iter*10000:len(time)],pktout[iter*10000:len(time)],facecolor='#ff4500',edgecolor='#ff4500',label="bytes_out")
        plt.bar(time[iter*10000:len(time)],pktin[iter*10000:len(time)],facecolor='green',edgecolor='green',label="bytes_in")
        plt.xlabel("Time(s)")
        plt.ylabel("Packet_Length(bytes)")
        plt.title(title)
        plt.grid()
        plt.legend()
        plt.savefig(outputsplit[0]+'_num_'+str(iter+1),dpi=200)
    
    '''
    plt.bar(time,pktout,facecolor='#ff4500',edgecolor='#ff4500',label="bytes_out")
    plt.bar(time,pktin,facecolor='green',edgecolor='green',label="bytes_in")
    plt.xlabel("Time(s)")
    plt.ylabel("Packet_Length(bytes)")

    plt.title(title)
    plt.grid()
    plt.legend()
    plt.savefig(outputfile,dpi=200)
    #plt.show()
    '''


# In[6]:


if __name__ == "__main__":
    main()


# In[5]:


#data=np.array(data)
#print(data)



# In[10]:





