from googlesearch import search
import requests
import os

channels_db={
    "jordan":'https://www.jrtv.gov.jo/live-tv',
    "abc":"https://abcnews.go.com/Live",
    'jazeera':'https://www.aljazeera.com/live/',
    'bloomberg':'https://www.bloomberg.com/live/us',
    'sky':'https://www.youtube.com/watch?v=9Auq9mYxFEE&ab_channel=SkyNews',
    'facebook watch':'https://web.facebook.com/watch'
}

def get_site_google(query):
    query=query.replace(" ","+")
    netflix_site=""
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        print(j)
        netflix_site=j
    return netflix_site


def run_netflix(movie_name):
    query=("netflix "+movie_name).replace(" ","+")
    netflix_site=get_site_google(query)
    netflix_site=netflix_site.replace("title","watch")
    print(netflix_site)
    os.system('./run.sh '+netflix_site+" 1")

def run_youtube(video_name):
    query=video_name.replace(" ","+")
    youtube_site=get_site_google(query)
    print(youtube_site)
    os.system('./run.sh '+youtube_site+" 1")

def run_channel(channel_name):
    channel_link=channels_db[channel_name]
    os.system('./run.sh '+channel_link+" 1")

if __name__ =="__main__":
    run_channel("bloomberg")