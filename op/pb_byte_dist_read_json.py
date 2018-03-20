
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


    bdlist=[]
    su=0
    for i in range(1,len(data)):
        d=json.dumps(data[i], indent=4)
        #print(d)
        #print(data[i]['time_start'])
        pakpd=data[i]['byte_dist']
        #print('pakpd=',pakpd)
        if i==1:
            for i in pakpd:
     #           print(i)
                bdlist.append(i)
                su+=i
        else:
            for i in range(len(bdlist)):
                bdlist[i]=bdlist[i]+pakpd[i]
                su+=pakpd[i]
        #print('--------------------------------------------------------')
    #print(bdlist)
    bdlist=np.array(bdlist)
    bdlist=bdlist/su
    plt.bar(range(len(bdlist)),bdlist,facecolor='#ff4500',edgecolor='#696969',linewidth=0)

    plt.xlabel("Bytes_Value")
    plt.ylabel("Probability")
    plt.title(title)
    plt.grid()
    plt.xlim(-0.1,256)
    plt.ylim(0,0.03)
 #   plt.legend()
    plt.savefig(outputfile,dpi=200)
    #plt.show()

    sys.exit(0)

