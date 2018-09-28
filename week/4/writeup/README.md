Writeup 3 - Pentesting I
======

Name: Luke Mann
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Luke Mann

## Assignment 4 Writeup

### Part 1 (45 pts)
I started with just running `nc cornerstoneairlines.co 45` to see what I should expect. I wanted to try a few things with the `Network Administration Panel  --  Uptime Monitor`, and I ended up just trying entering random ip addresses for kicks. Thinking that the prompt may be vulnerable like the shell shock attack we saw in class, I decided to try adding a semicolon to execute the second command. Running `;ls` printed a list of directories! I then went straight to `home` and ran `cat flag.txt`, as the `shellimg.png` image showed that to be the location of the flag (`;cd home;cat flag.txt`). 

Flag: `CMSC389R-{p1ng_as_a_$erv1c3`

I decided to use the semicolon approach because adding `;` to a bash command allows a second command to executed from the same line. This approach was taught in class and has been used extensively for [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) of both the frontend and the backend of applications. 

In order to find out what allowed this vulnerability, I decided to try to find the script making the `Uptime Monitor` prompt. I went about exploring the various directories and eventually found `/opt/container_startup.sh`. This script showed that the prompt would result in `echo "[$(date)] INPUT: $input" cmd="ping -w 5 -c 2 $input" output=$(eval $cmd)` being run.

Basically, `eval $cmd` is the security flaw that ought to be corrected,  this executes any second command that the user attaches, because the semicolon and command are added to the `cmd` string. 

This could be fixed by creating a script that would only execute the `eval` command if `$cmd` does not contain any semicolons, or even better if the $input was only a single IP address. This could be done using a check of the regex, such as patterns [on this site](https://www.regular-expressions.info/ip.html). A few different implementations are possible depending on the overall application/ use case. 



### Part 2 (55 pts)

My program (`stub.py`, Python3)  executes commands using the exploit in part one. Using the socket libary, a connection is made to `cornerstoneairlines.co` at port 45 and the commands are sent as in part one.

In order to maintain the state of what directory the user is in (necessary because a new remote shell is started everytime the bytes are sent), a single string of the path is stored as `base`. From here, `cd` commands are simply executed by adding to the base, and when a `cd ../` or similar command is run, the `base` variable is updated to appropriately show the change in directory. 

The pull method simply uses `cat` to essentially copy the data to a local file as provided. Although this may not be able to handle directories or function, it gets the job done for practical applications such as downloading `container_startup.sh`. The error handling is also rather rudimentary, just a generic try, catch statement. In future implementations, the can be extended to explicitly tell users about common errors.

This script also proves useful for revisiting part one. Instead of manually starting a new shell for each command, this script allows us to execute the commands in quick succession and thus find flags quickly. 