#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

from googleapiclient.discovery import build    #for using YouTube API

from pytube import YouTube  # for downloading youtube videos

import os                   # for creating new directories

import cv2


# In[2]:


def Youtube_api(link, videoId):                              # function to generate top 2 video links based on related videoId
    F=[]
    
    
    api_key = 'AIzaSyA3MTY_9ig6svkofnp8haGvHcgbG6OUc4o'
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
    
        file_link=link+i['id']['videoId']
        F.append(file_link)                   #store all the links
        print(F)
    return F


# In[8]:


def Download_videos(D,loc):
    
    G=[]
    
    for i in D:
        video = YouTube(i)
        video.streams.filter(file_extension='mp4').first().download(loc)
        print("Video is downloaded")
        
        
        title=video.title
        title=title.replace(":","").replace("|", "").replace("?", "").replace("*", "").replace("\"", "").replace("/","").replace("\\", "")

        
        

        print(title)
        G.append(title)
        
      
    return G
       
       


# In[9]:


def save_frame(H, loc):
    os.chdir(loc)
    gap=20
    
    for k in H:
       
        os.mkdir(k)
        file_loc=loc+k+'.mp4'
        cap=cv2.VideoCapture(file_loc)

        i=0
        while(cap.isOpened()):
            
            flag, frame=cap.read()
            if flag==False:
                break
            
            elif (i==0):
                 loc1=loc+k +"/image"+str(i) +".jpg"
                 cv2.imwrite(loc1, frame)
            
            elif(i%gap==0):
                loc1=loc+k +"/image"+str(i) +".jpg"
                cv2.imwrite(loc1, frame)
                
           
            
            i+=1
    
        cap.release()
        cv2.destroyAllWindows()
        
 


# In[12]:


def scrap(file):
    data=pd.read_csv(file)
    D=[]
    
    for row in data.itertuples():
        # print(row.Youtube_links)
        
        filename=row.Youtube_links
        link, videoId=filename.split('=') #split the youtube link to get the videoId needed for Youtube_data api
        
        link=link+'='
        #print(link, videoId)
        
        
        D.extend(Youtube_api(link, videoId))  #generate all the links of related video files and store it in list D 
        
    #print(D)     
    stored_loc='C:/Users/Admin/Desktop/Project1/'  #loc folder for downloading videos and frames
    P=Download_videos(D, stored_loc)               #download videos and store all the video titles in list P
    #print(P)
        
    save_frame(P, stored_loc)                     #create frames from videos and store it in a newly created directory from vieo title.
        


# In[13]:


if __name__=='__main__':
    
    file='C:/Users/Admin/Desktop/Project1/Youtube_links.csv'
    
    scrap(file)
    
    
    


# In[ ]:




