import json
from tkinter import W
import requests
import json

myHook = "replace with hook url"

def send_discord(msg, url: str):
    if not url:
        return
    data = {"content": f"{msg} "}
    requests.post(url, json=data)

def retrieve_message(channelid):
    headers = {
        'authorization': 'replace with authorization'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages?limit=3', headers = headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        discordMessage = value['content']
        discordName = value['author']['username']
        if discordName == 'whatevername':
            send_discord(discordName+"Said "+discordMessage, myHook)
        else:
            print("this message was sent by: "+discordName)
            
        

retrieve_message('replace with channel id')
