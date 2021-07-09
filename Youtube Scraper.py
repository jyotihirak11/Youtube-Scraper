#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install google-api-python-client


# In[2]:


pip install ffmpeg


# In[3]:


pip install pytube


# In[38]:


import pandas as pd

from googleapiclient.discovery import build    #for using YouTube API

from pytube import YouTube  # for downloading youtube videos

import ffmpeg               # for saving frames

import re                   # for splitting strings- youtube links

import os                   # for creating new directories


# In[2]:


#read data from csv file
data = pd.read_csv('C:/Users/Admin/Desktop/Project1/Youtube_links.csv')
data.head(5)
print(len(data))


# In[3]:


for row in data.itertuples():     
   print(row.Youtube_links)
 # random links stored in csv file


# In[27]:


D=[]   # for storing links from csv file as well as storing top 2 relevant links from Youtube api

def Youtube_api(link, videoId, D):                              # function to generate top 2 video links based on related videoId
    api_key = 'AIzaSyB6EOTenAaXlaAehlf0eO8s1AmC9WU84oY'

    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
    part = 'snippet',
    maxResults = 3,
    type = 'video',
    relatedToVideoId= videoId
    )

    response = request.execute()

    #print(response)


    for i in response['items']:
    
        #print(i['snippet']['title'])
        #print(i['id']['videoId'])
        # print(link+i['id']['videoId'])
      file_link=link+i['id']['videoId']
      D.append(file_link)                   #store all the links


# In[37]:



  for row in data.itertuples():
    filename=row.Youtube_links
    
    link, videoId=re.split(pattern=r"[=]", string=filename)    #splitting youtubelinks to videoId and link using regex
    #print(link+"\n"+ videoId)
    link = link[0:] + "="
    
    Youtube_api(link, videoId, D)                            #above function is called
    
   


# In[41]:


print(len(D))
loc='C:/Users/Admin/Desktop/Project1/'
F=[]      # for storing all the downloaded videos title + extention


def Download_videos(D,F,loc):
    for i in range(0, len(D)):
        video = YouTube(D[i])
        #video.streams.first().download(loc)
        #print("Video is downloaded")
        print("video title:" +video.title)
        filename= loc+video.title +'.mp4'
        F.append(filename)
        i=i+1
       


# In[42]:


Download_videos(D,F,loc)
print(len(F))


# In[25]:


#video = YouTube(row.Youtube_links)
#video.streams.first().download('C:/Users/Admin/Desktop/Project1/')
   # print("Video is downloaded")
print("video title:" +video.title)
for i in range(0, len(D)):
    print(D[i])
    i=i+1


# In[44]:


os.chdir(loc)
for k in range(0, len(F)):
    os.mkdir('frame-'+str(k))
    k=k+1


# In[45]:


def save_frame(filename, loc):
    for k in range(0, len(F)):
        os.mkdir('frame-'+str(k))
        ffmpeg -i loc/F[k] loc/'frame-'+str(k)/image%d.png'


# In[46]:


ffmpeg -i C://Users//Admin//Desktop//Project1//Afghanistan में Russian Army की एंट्री  Good News for India.mp4 C://Users//Admin//Desktop//Project1//image%d.jpg


# In[ ]:




