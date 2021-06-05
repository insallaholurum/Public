#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# In[ ]:


df = pd.read_csv('data.csv')


# In[ ]:


labels = df.columns[1:]
width = 0.35


# In[ ]:


fig , ax = plt.subplots(figsize=(16,9))
for i in range(len(df)):
    y = np.array(df.iloc[i,1:])
    if i == 0:
        ax.bar(labels,y,width)
    else:
        bottom = np.array([0,0,0])
        for k in range(i):
            midd=np.array(df.iloc[k,1:])
            bottom = bottom+midd
        ax.bar(labels,y,width,bottom=bottom)
plt.legend(df['Area of Interest'],loc='lower right')        
plt.ylabel("Hours",fontsize=15)
plt.title("How many hours spend in daily activities?",fontsize=18)
plt.show()
fig.savefig('outcome.jpg')


# In[ ]:





# In[ ]:





# In[ ]:




