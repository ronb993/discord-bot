import socket
import sys

myHook = '' # place discord hook url here
myAuthorization = '' # place authorization here
channelID = '' # place discord channel ID here
userName = '' # replace with discord username

def sendAndReceiveChatScript(msgToSend, server='127.0.0.1', port=1024, timeout=10):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((server, port))
        s.sendall(msgToSend)
        msg = ''
        while True:
            chunk = s.recv(1024)
            if chunk == b'':
                break
            msg = msg + chunk.decode("utf-8")
        s.close()
        return msg
    except:
        return None

server = 127.0.0.1
port = 1024
botname = "harry"
user="bob"
