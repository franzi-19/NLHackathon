#!/usr/bin/python
# Sample Python code for user authorization

import os
import urllib.parse as urlparse
import google.oauth2.credentials
import re
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
import json

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
categories_as_json = {"2":"Autos & Vehicles",
"1":"Film & Animation",
"10":"Music",
"15":"Pets & Animals",
"17":"Sports",
"18":"Short Movies",
"19":"Travel & Events",
"20":"Gaming",
"21":"Videoblogging",
"22":"People & Blogs",
"23":"Comedy",
"24":"Entertainment",
"25":"News & Politics",
"26":"Howto & Style",
"27":"Education",
"28":"Science & Technology",
"29":"Nonprofits & Activism",
"30":"Movies",
"31":"Anime/Animation",
"32":"Action/Adventure",
"33":"Classics",
"34":"Comedy",
"35":"Documentary",
"36":"Drama",
"37":"Family",
"38":"Foreign",
"39":"Horror",
"40":"Sci-Fi/Fantasy",
"41":"Thriller",
"42":"Shorts",
"43":"Shows",
"44":"Trailers"}
categories_dict = json.loads(categories_as_json)

categories = {"2":"Autos & Vehicles",
"1":"Film & Animation",
"10":"Music",
"15":"Pets & Animals",
"17":"Sports",
"18":"Short Movies",
"19":"Travel & Events",
"20":"Gaming",
"21":"Videoblogging",
"22":"People & Blogs",
"23":"Comedy",
"24":"Entertainment",
"25":"News & Politics",
"26":"Howto & Style",
"27":"Education",
"28":"Science & Technology",
"29":"Nonprofits & Activism",
"30":"Movies",
"31":"Anime/Animation",
"32":"Action/Adventure",
"33":"Classics",
"34":"Comedy",
"35":"Documentary",
"36":"Drama",
"37":"Family",
"38":"Foreign",
"39":"Horror",
"40":"Sci-Fi/Fantasy",
"41":"Thriller",
"42":"Shorts",
"43":"Shows",
"44":"Trailers"}

def get_authenticated_service(): 
    #flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    #credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, developerKey="irgendeinKey")


def channels_list_by_username(service, **kwargs):
    results = service.channels().list(
        **kwargs
    ).execute()


    print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
          (results['items'][0]['id'],
           results['items'][0]['snippet']['title'],
           results['items'][0]['statistics']['viewCount']))


def commentsSearch(service, video_id):
    results = service.commentThreads().list(
    part="snippet",
    videoId=video_id,
    textFormat="plainText",
    maxResults = 100,
    order = "relevance"
    ).execute()

    watson= ""
    for item in results["items"]:
        comment = item["snippet"]["topLevelComment"] 
        author = comment["snippet"]["authorDisplayName"]
        text = comment["snippet"]["textDisplay"]
        watson += text + ". "
        #print("Comment by %s: %s" % (author, text)) 

    return watson

    # ------Kommentare eines Kommentars------
    # parent_id = results["items"][0]["id"]      
    # comments = service.comments.list( part='snippet', parentId=parent_id).execute()
    # print(comments)

def videoSearch(service, video_id):
    response = service.videos().list(id = video_id, part="snippet").execute()
    for item in response["items"]:
        title = item["snippet"]["title"]
        #decription = item["snippet"]["description"]
        cat = item["snippet"]["categoryId"]
        print ("Title: '%s' and category: '%s' \n" % (title, categroyForNumber(cat)))

    # return response["items"]


def categroyForNumber(number):
    return ""

def getData():
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()

    var = input("Please enter the link to your youtube video: ")
    

    #id = "naW9U8MiUY0" dragon
    #id= "TmYOuO68uIE" #fußball
    #id = "TFuQeK4is4U" #hundevideo
    #id="ySN5Wnu88nE"# computer
    #id="ktvTqknDobU"

    id = url_parse(var)
    
    videoSearch(service, id)

    watson = commentsSearch(service,id)

    string = ""
    for str in watson:
        pattern = '[A-Za-z., ]'
        result = re.match(pattern, str)
        if result is not None:
            string += str
    return string

def url_parse(url):
    parsed = urlparse.urlparse(url)
    return urlparse.parse_qs(parsed.query)["v"][0]


if __name__ == '__main__':
    print(getData())

