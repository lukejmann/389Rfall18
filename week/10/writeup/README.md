Writeup 10 - Crypto II
=====

Name: Luke Mann
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgment of honor pledge: Luke Mann

## Assignment 10 Writeup

### Part 1 (70 Pts)
For this assignment, I first set up the connection to the given IP address and navigated through the menu until getting the legit hash and extracting it using regex.  Next, I created a fake hash to send using the stub code, but the hard part was figuring out the right padding to put between the message and the malicious hash. At first, I tried following the instructions for calculating the exact padding I needed, but I found this to be slightly tiresome and I couldn't get it to work properly. I ended up running a loop with a few different messages to find the right number of `\x00`s to add, and eventually I figured out that for the 3-letter message the correct number is 42. Then, following the stub code, I added the message and malicious message to the padding and sent the payload!

my legit hash was `3671e5b6a9a35e49d39663c5cba4242f` and my crafted hash was `960ca98a91bf3b0b6993bc27ee95d3fd`. My payload was `ljm\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00baddie`

### Part 2 (30 Pts)
To create my own key I ran `gpg --gen-key` and added my email with the UID of `Luke Mann`. Then, to import the given key, I ran `--import pgpassignment.key`. I then saw that this imported a key for  UMD Cybersecurity Club with the email "president@csec.umiacs.umd.edu". Finally, I ran `gpg -e -u "Luke Mann" -r "UMD Cybersecurity Club" message.txt`, which encodes the message.txt file(contains `yo`) with the imported "UMD Cybersecurity Club" as the recipient and Luke Mann as the signing user.  


