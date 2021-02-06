#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import json
import pickle
from matplotlib import pyplot as plt


# In[ ]:


def read_file(filename):
    loc= '/home/bansal/Downloads/' + filename + ".txt"
    print (loc)
    txtfile= open(loc, 'r')
    lines= txtfile.read().split(' ')
    array= []
    for num in lines:
        if(len(num)> 0):
            array.append(float(num))
    return array



# In[14]:


def read_pkl(filename):
    loc= '/media/data_dump_1/Rajat/Topics_CFscore/' + filename + ".pkl"
    print (loc)
    f= open(loc, 'rb')
    array= pickle.load(f)
    return array


# In[3]:


def read_json(filename):
    loc= '/home/bansal/Downloads/' + filename + '.json'
    print (loc)
    scores= []
    count= 0
    for comment in open(loc, 'r'):
        scores.append(abs(int(json.loads(comment)['ups'])))#nice
    return scores


# In[4]:


def get_mean(array):
    count= 0
    for num in array:
        if(num!= 0.0):
            count+= 1
    print (count)
    return np.sum(array)/count


# In[5]:


def get_median(array):
    array2= []
    for i in array:
        if(i!= 0.0):
            array2.append(i)
    return np.median(array2)


# In[ ]:


def create_discourse(filename):
    loc= '/home/bansal/Downloads/' + filename + '.json'
    actualdiscourse= []
    obsdiscourse= read_file('elaborationdiscourse')
    print (len(obsdiscourse))
    count= 0
    df= pd.read_csv('/home/bansal/Downloads/subreddits_basic.csv')
    for post in open(loc, 'r'):
        text= json.loads(post)
        subreddit= text['subreddit']
        subs= df.loc[df['reddit']== subreddit, 'subs'].values
        for subpost in text['posts']:
            if('majority_type' in subpost and subpost['majority_type']== 'elaboration'):
                if(len(subs)> 0 and subs[0]!= 'None' and int(subs[0])!= 0):
                    actualdiscourse.append(1)
                else:
                    actualdiscourse.append(0)
    print (len(actualdiscourse))
    return actualdiscourse
    


# In[6]:


def get_correlation(virality, formality):
    return np.corrcoef(virality, formality)



# In[18]:


vir= read_pkl('worldnewscfv') 
scores= read_pkl('worldnewscf')
print (len(vir))
print (len(scores), np.mean(scores))
print ("For Worldnews: " + str(get_correlation(scores, vir)))
fig, axs = plt.subplots(2, 2)
axs[0,0].scatter(scores, vir, c= 'blue', alpha= 0.3)
axs[0,0].set_title('Worldnews Scatter Plot')
vir= read_pkl('sciencecfv')
scores= read_pkl("sciencecf")
print (len(vir))
print (len(scores), np.mean(scores))
print ("For Science: " + str(get_correlation(scores, vir)))
axs[0,1].scatter(scores, vir, c= 'yellow', alpha= 0.3)
axs[0,1].set_title('Science Scatter Plot')
vir= read_pkl('moviescfv')
scores= read_pkl('moviescf')
print (len(vir))
print (len(scores), np.mean(scores))
print ("For Movies: " + str(get_correlation(scores, vir)))
axs[1,0].scatter(scores, vir, c= 'red', alpha= 0.3)
axs[1,0].set_title('Movies Scatter Plot')
vir= read_pkl('showerthoughtscfv')
scores= read_pkl('showerthoughtscf')
print (len(vir))
print (len(scores), np.mean(scores))
print ("For Showerthoughts: " + str(get_correlation(scores, vir)))
axs[1,1].scatter(scores, vir, c= 'green', alpha= 0.3)
axs[1,1].set_title('Showerthoughts Scatter Plot')


for ax in axs.flat:
    ax.set(xlabel='Formality Scores', ylabel='Virality Scores')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.savefig('/media/data_dump_1/Rajat/Topics_CFscore/topicscf.png')


# In[ ]:




