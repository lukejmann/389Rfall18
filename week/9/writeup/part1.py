#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
hash_list=open("../hashes",'r').readlines()

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for password in wordlist:
    password=password.strip()
    for salt in salts:
        salted_word=hashlib.sha512(salt+password).hexdigest()
        for hash in hash_list:
                hash=hash.rstrip()
                if salted_word==hash:
                     print("Matched password is {} with salt {}!".format(password,salt))
