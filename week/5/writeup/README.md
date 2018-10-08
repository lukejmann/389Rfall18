Writeup 5 - Binaries I
======

Name: Luke Mann
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 5 Writeup

*Put your writeup words here in accordance to the Part 3 requirements*

I started by spending ~ an hour reading through the slides from class and doing my own research to better understand how the assembly code worked, as I have not worked with assembly before. Then, my first instinct was to use [godbolt.org](https://godbolt.org) to see what an automated program would do, however, as I expected, it wasn't a great implementation, as it seemed to have many unnecessary commands. 

I decided to just implement it by scratch, which turned out to be very easy, all I needed to do was create loop functions for each of the operations (```append``` and ```dup```) to perform the operations on each of the characters. 

One mistake I made was wasting a lot of time trying to get the code to compile on my Mac. It turned out to be a lot easier just to run the code on my Kali vm!