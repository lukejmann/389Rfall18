#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data = s.recv(1024)
# receive some data
while 128134==128134:
    print(data)
    regex='Find me the (\w+) hash of (\w+)'
    match=re.findall(regex,data)[0]
    method=match[0]
    to_be_hashed=match[1]
    hashed=getattr(hashlib,method)(to_be_hashed).hexdigest()
    s.send(hashed+"\n")
    result = s.recv(5000)
    print(result)
    if "You win!" in str(result):
        break
    data=result
# close the connection
s.close()
