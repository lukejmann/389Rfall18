Writeup 3 - OSINT II, OpSec and RE
======

Name: Luke Mann
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Luke Mann

## Assignment 3 Writeup

### Part 1 (100 pts)

One of the most glaring issues was that the password to port 1337 of the admin server was extremely easy to guess or even brute force. For starters, Fred's Instagram was filled with posts of various pokemon, thus suggesting that he has a strong connection to pokemon. Anybody with a little bit of time on their hands would logically guess "pokemon" before attempting to brute force the password. Also, the password is only seven characters long, has no special characters, and is a common phrase. This means that the password is likely to appear on wordlists used for password cracking such as rockyou.txt. Mental Floss [suggests](http://mentalfloss.com/article/504786/8-tips-make-your-passwords-strong-possible0) using numbers, letters, and symbols in any given password for increased security, and Fred failed at fulfilling this obligation. Mental Floss also recommends using long passwords as well as not using passwords that are connecting to personal information, and Fred chose only to use a seven character password that is highly correlated to his demonstrated interests. In the future, I would suggest that Fred uses a password generating software to chose his passwords for him. For example, Dashlane, LastPass, and Safari can all generate highly secure passwords at the press of a button. These passwords, which are typically 16 characters long, take exponentially longer to brute force and are almost guaranteed to not appear on word lists. 




Another major issue is that Fred's server allowed unlimited (as far as I could tell) attempts at logging in. This means that an attacker can try as many different passwords as rapidly as the would like – limited only by computational and network speeds. According to RimuHosting, using 'hashlimit' in 'iptables' by adding the following to the ssh configuration is one of the most effective ways of preventing this. 
```
iptables -I INPUT -m hashlimit -m tcp -p tcp --dport 1337 --hashlimit 1/min 
--hashlimit-mode srcip --hashlimit-name ssh -m state --state NEW -j ACCEPT
```
This limits the number of connections that an IP address can have to the ssh port to only one per minute, thus dramatically increasing the time required for a brute force attack from one or multiple IP addresses.  


The third major issue was that Fred left port 1337 open for anybody to attempt to access. When Fred did not need to access the port, he should have closed the port. As [WatchPort](https://blog.watchpointdata.com/why-closing-unused-server-ports-is-critical-to-cyber-security) explains, "a hacker can easily take advantage of the system by running a simple port scan using free software like nmap to discover the open ports." Once they see that a port is open, they can perform a wide variety of attacks to access the port. The only way to (almost) guarantee that the port cannot be accessed is to close it. If the port must be open, there should at least be a software-generated password on it!



Good luck!
