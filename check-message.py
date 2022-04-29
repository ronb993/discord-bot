import time
import json
import requests
from chatscript_client import *

myHook = "replace with hook url"
lastTime = ""

def sendDiscord(msg, url: str):
    if not url:
        return
    data = {"content": f"{msg} "}
    requests.post(url, json=data)

def retrieveData(channelid):
    headers = {
        'authorization': 'replace with authorization'
    }
    try:
        r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages?limit=3', headers = headers)
        r.raise_for_status()
        jsonn = json.loads(r.text)
        for value in jsonn:
            currentTime = value['timestamp']
            discordMessage = value['content']
            discordName = value['author']['username']
        return currentTime, discordMessage, discordName
    except:
        import sys
        sys.exit('unable to request time') 


while True:
    retrieveTime, sendM, sendN = retrieveData()
    if retrieveTime != lastTime:
        lastTime = retrieveTime
        print("new message retrieved")
        if sendN == 'replace with username':
            msg = u'%s\u0000%s\u0000%s\u0000' % (user, botname, sendM)
            msg = str.encode(msg)
            resp = sendAndReceiveChatScript(msg, server=server, port=port)
            sendDiscord(" "+resp, myHook)
        else:
            print("This is not the person")
    time.sleep(3) # you may want sleep to not overload the network