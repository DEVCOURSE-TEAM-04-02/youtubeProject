from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

# https://console.cloud.google.com/apis/credentials 여기서 API발급받아 사용
DEVELOPER_KEY='AIzaSyDfvhCHcNTn5RB30Ll9oFSjnvjW9x1ncLs' # 내 API 키값 입력
YOUTUBE_API_SERVICE_NAME='youtube'
YOUTUBE_API_VERSION='v3'

youtube=build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

search_response=youtube.search().list(
    q="지무비 : G Movie",
    order='relevance',
    part='snippet',
    maxResults=50,
    ).execute()

channel_id=search_response['items'][0]['id']['channelId']

playlists=youtube.playlists().list(
    channelId= channel_id,
    part = "snippet",
    maxResults=40
).execute()

import pandas as pd

ids=[]
titles=[]
for i in playlists['items']:
    ids.append(i['id'])
    titles.append(i['snippet']['title'])
    
df=pd.DataFrame([ids,titles]).T
df.columns=['PlayLists','Titles']

gmovie=df['PlayLists'][36]
playlist_videos=youtube.playlistItems().list(
    playlistId= gmovie,
    part = "snippet",
    maxResults=10,
)
playlistitems_list_response = playlist_videos.execute()

video_names=[]
video_ids=[]
date=[]

for v in playlistitems_list_response['items']:
    video_names.append(v['snippet']['title'])
    video_ids.append(v['snippet']['resourceId']['videoId'])
    date.append(v['snippet']['publishedAt'])
    
vdf=pd.DataFrame([date,video_names,video_ids]).T
vdf.columns=['Date','Title','IDS']

import re

category_id=[]
views=[]
likes=[]
dislikes=[]
comments=[]
mins =[]
seconds=[]
title=[]

for u in range(len(vdf)):
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=vdf['IDS'][u]
    )
    response = request.execute()
    
    if response['items']==[]:
        ids.append("-")
        category_id.append("-")
        views.append("-")
        comments.append("-")

    else:

        title.append(response['items'][0]['snippet']['title'])
        category_id.append(response['items'][0]['snippet']['categoryId'])
        views.append(response['items'][0]['statistics']['viewCount'])
        comments.append(response['items'][0]['statistics']['commentCount'])    
        
gmovie_df=pd.DataFrame([title,category_id,views,comments]).T
gmovie_df.columns=['title','category_id','views','comments']
print(gmovie_df)