Writeup 7 - Forensics I
======

Name:  Luke Mann 
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Luke Mann

## Assignment 7 writeup

### Part 1 (40 pts)

1.  It is a JPEG File

2.  41°53' 54.87" N, 87° 37' 22.53" W —> John Hancock Center, Chicago, Illinois

3.  2018:08:22 11:33:24

4.  An iPhone 8 back camera 3.99mm f/1.8

5.  539.5 m Above Sea Level

6. CMSC389R-{look_I_f0und_a_str1ng} + CMSC389R-(abr@cadabra}

### Part 2 (55 pts)

*SUBMIT YOUR WRITEUP DETAILING YOUR APPROACH AND SOLUTION TO THIS PROBLEM HERE (>250 words). Dont forget to include the flag!*

First, I simply executed the binary which printed out  `Where is your flag?`.   My next guess was to use rabin to figure out what is being called within the binary file. Using `rabin2` showed that `fopen` was being called (along with `fwrite` and `fclose`). This told me that another file was being written to by the binary, so I used gdb to figure out that the file being written to is `/tmp/.stego`, just by setting a breakpoint and looking at read and write info of my system. I `cp`'d `.stego` into my current directory. It took me a long time to figure out that I just needed to open the file using a hex editor, I wasted a lot of time trying to convert it to different formats. Once I opened it with a hex editor I saw the magic bites were offset by a null at the very beginning. Then I used   `binwalk` to determine that it is a JPEG and renamed it `jpeg_stego.jpeg`.  However, I was getting errors opening the file so I went back to look at the bytes and saw that the closing bytes were incorrect for a JPEG (they are supposed to be `FF` `D9`).  After fixing this and opening the file, as I expected, it showed a picture of a stegosaurus! I then used `steghide` on the image and guessed the password `stegosaurus` based on the image (the same way that `pokemon` was the password in week 1). After guessing the password, I saw the flag `CMSC389R-{dropping_files_is_fun}`!