#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import re

host = "142.93.118.186"   # IP address or URL
port = 1234     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

data = s.recv(1024)
s.send("1\n")
data = s.recv(1024)

#####################################
### STEP 1: Calculate forged hash ###
#####################################

message = 'ljm'    # original message here
legit = ''      # a legit hash of secret + message goes here, obtained from signing a message

s.send('{}\n'.format(message))

data = s.recv(1024)

matched=re.compile(r"Your hash: ([a-z0-9]+)").search(data).group(1)
legit=matched
print("legit hash: {}".format(legit))

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'baddie'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print("crafted hash: {}".format(fake_hash))


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits
# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash
data = s.recv(1024)
padding = "\x80" + "\x00"*42 + chr(104) +'\x00\x00\x00\x00\x00\x00\x00'
payload = message + padding + malicious
print("Payload: {}".format(payload))
s.send("2\n")
data = s.recv(1024)
s.send(fake_hash+"\n")
data = s.recv(1024)
s.send(payload + "\n")
data = s.recv(1024)
data = s.recv(1024)
print(data)
s.close()