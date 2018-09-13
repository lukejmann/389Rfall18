Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Luke Mann
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 2 writeup

### Part 1 (45 pts)

1. FRED KRUEGER

2. 
* Twitter(checkusernames.com)- His Life's Trippin, associated with cornerstoneairlines.co, based in Silver Spring MD
* Has a Reddit account (checkusernames.com)
* Has instagram account with boarding pass for December 12th and lots of pokemon?

3.  Using ReconDog, the webserver is 142.93.118.186.

4. Using ReconDog, looking at robots.txt: /secret (CMSC389R-{fly_th3_sk1es_w1th_u5}). Also the TXT record: CMSC389R-{dns-txt-rec0rd-ftw} and hidden git repo: CMSC389R-{y0u_found_th3_g1t_repo}

5. The admin page links to 142.93.117.193. This is just from clicking on the link on the webpage

6. 142.93.118.186 is based in Ontario. Ontario. 142.93.117.193 is also based in Ontario.

7. 142.93.118.186 is running Apache 2.4.18. 142.93.117.193 is also running Apache 2.4.18.

8. *(BONUS)*
CMSC389R-{y0u_found_th3_g1t_repo}
CMSC389R-{dns-txt-rec0rd-ftw}
CMSC389R-{fly_th3_sk1es_w1th_u5}

### Part 2 (55 pts)
Using `nmap` (with `-p-`) I found a few different open ports on the admin server. After testing them, only 1337 prompted for login when using `nc`. I then finished up the brute force login and had it running for a _very_  long time using the username `kruegster1990`, then i tried a few others for a couple minutes and `kruegster` worked with the password `pokemon` (insta makes sense now). Then I spent a few minutes exploring the files until I found `home/flight_records` and then I just pulled up `AAC27670.txt` (based on his insta photo). `AAC27670.txt` contained the flag `CMSC389R-{c0rn3rstone-air-27670}`.