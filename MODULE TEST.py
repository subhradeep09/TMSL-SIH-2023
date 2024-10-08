from test import YTStats
from pytube import *
import requests
import json


API_KEY = 'AIzaSyAMtysCv1YSFqck6UOtdpZWYuZ1qzGGNWY'

channel_id = 'UCbXgNpp0jedKWcQiULLbDTA'


def get_video_ids(URL_PLAYLIST):

    # Retrieve URLs of videos from playlist
    playlist = Playlist(URL_PLAYLIST) 

    urls = []
    vid_ids = []
    for url in playlist:
        urls.append(url)

    for i in urls:
        vId = extract.video_id(i)
        vid_ids.append(vId)
    
    return (vid_ids,urls)

yt = YTStats(API_KEY, channel_id)

#print((get_video_ids("https://youtube.com/playlist?list=PLU6SqdYcYsfJV8Lfq4KFA0U8kGeJ2NGWV&si=zq8VtON19aU-aL6g"))[1])

count = 0
for x in (get_video_ids("https://youtube.com/playlist?list=PLU6SqdYcYsfJV8Lfq4KFA0U8kGeJ2NGWV&si=zq8VtON19aU-aL6g")[0]):

    json_url = requests.get(yt.get_video_stats(x))

    data = json.loads(json_url.text)
 
    
    
    #collecting all datas
    
    video_url =  get_video_ids("https://youtube.com/playlist?list=PLU6SqdYcYsfJV8Lfq4KFA0U8kGeJ2NGWV&si=zq8VtON19aU-aL6g")[1][count]

    video_id = data["items"][0]["id"]  #id of the video

    title_of_video = data["items"][0]["snippet"]["title"]

    tags_of_video = (data["items"][0]["snippet"]["tags"])

    channel_title = data["items"][0]["snippet"]["channelTitle"]

    video_thumbnail = data["items"][0]["snippet"]["thumbnails"]["medium"]["url"]
    
    duration_of_video = int(data["items"][0]["contentDetails"]["duration"][2:].split('M')[0])

    video_views = data["items"][0]["statistics"]["viewCount"]

    video_likes = data["items"][0]["statistics"]["likeCount"]

    video_comments_count = data["items"][0]["statistics"]["commentCount"]

    count+=1

    print(video_thumbnail,duration_of_video)

    
    
# ids = get_video_ids("https://youtube.com/playlist?list=PLU6SqdYcYsfJV8Lfq4KFA0U8kGeJ2NGWV&si=zq8VtON19aU-aL6g")
# json_url = requests.get(yt.get_video_stats(ids[0][0]))
# data = json.loads(json_url.text)





# print(video_views,video_likes,video_comments_count)
        
# url = get_video_ids("https://youtube.com/playlist?list=PLU6SqdYcYsfJV8Lfq4KFA0U8kGeJ2NGWV&si=zq8VtON19aU-aL6g")[0]
