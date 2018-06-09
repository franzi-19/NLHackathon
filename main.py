import watson
import quickstart
import os
import urllib.parse as urlparse
import google.oauth2.credentials
import re
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
import json


API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service(): 
    #flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    #credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, developerKey='AIzaSyD4trzorHjH564iLIXH3b-GlO4goBwU3cc')

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
service = get_authenticated_service()  

channelName = input("Please enter the name of the channel: ")

response = service.channels().list(part='snippet,contentDetails', forUsername =  str(channelName)).execute()
channel = response["items"][0]
uploads_list_id = channel['contentDetails']['relatedPlaylists']['uploads']

playlistitems_response = service.playlistItems().list(
            playlistId=uploads_list_id,
            part='snippet',
            maxResults=50,
        ).execute()

videos= []
for playlist_item in playlistitems_response['items']:
    videos.append(playlist_item)

for video in videos:
    #print(video["snippet"]["title"])
    id = video["snippet"]["resourceId"]["videoId"]
    text = quickstart.getDataOneVideo(id, service)
    watson.analyseVideo(text)

# text = quickstart.getDataOneVideo("h2cgovUFSVA", service)
# watson.analyseVideo(text)

