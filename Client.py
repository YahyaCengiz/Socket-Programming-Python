from email import message
from http import client
import socket

port = 4141
host = socket.gethostbyname(socket.gethostname())
addres = (host,port)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addres)

def send(msg):
    message = msg.encode('utf-8')
    msg_length = len(msg)
    send_length = str(msg_length).encode('utf-8')
    send_length += b' ' * (64 - len(send_length))
    client.send(send_length)
    client.send(message)

user = input()
while user != "!" :
    send(user)
    user = input()
