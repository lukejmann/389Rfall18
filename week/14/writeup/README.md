Writeup 10 - Crypto II
=====

Name: Luke Mann
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Luke Mann

## Assignment 10 Writeup

### Part 1 (70 Pts)
I first visited `cornerstoneairlines.co:8080` and played around with the site, and clicking on a few of the links. I noticed that all of the listed items had the structure of `http://cornerstoneairlines.co:8080/item?id=NUM`. I tried adding some other numbers for the id first (-1,0,3, etc.), hoping to find an unlisted item, but that did not work out. Then, I noticed that the README for this week hints at __SQL__, so I figured it had to be an SQL injection that was needed. I tried adding the `' OR '1'='1` (from the presentation). This lead to the listing with id 1 (Cybersecurity Training Seminar) appearing, so I figured I had done something wrong with the injection. I tried playing around with some different SQL syntax and eventually found that just making the `OR` lowercase so that the URL was 
`cornerstoneairlines.co:8080/item?id=' or '1'='1` led to a new page with the `FLAG` of `CMSC38R-{y0U-are_the_5ql_n1nja}`!

### Part 2 (30 Pts)
1. My first thought was to insert JS code that would trigger the alert into the textbox in the center of the screen. I tried simply `alert('yo')` but this didn't do anything. I then tried wrapping it in `<script>` tags, and the alert appeared and I passed the challenge!

2. I tried inserting the same `<script>alert('yo')</script>` again, but nothing seemed to happen, so I tried it without the tags and the post was sent, telling me that the post is not valid if it has the `<script>` tags. I played around with a few different ways to get around this, including wrapping it in `<html>` tags. I eventually figured out that adding a `<input>` wrapper tag created an input box, which I needed to autofocus to use. I then set it so that it executed the JS code `alert('yo')` when it was automatically focused. The final script was `<input type="text" onfocus="alert('yo')" autofocus="" />`. 

3. I played around with the page a little bit, but I didn't see anything that stood out to me, so I looked at the code and saw that the html in the URL was being loaded via `$('#tabContent').html(html);`. I added the `<script>` tag with the alert code inside to the URL to get the final URL of `xss-game.appspot.com/level3/frame#'/><script>alert('yo')</script>`

4. After trying `<script>alert('yo')</script>`, I looked at the code. The code shows that upon the page loading the code `startTimer('{{ timer }}');` is being executed, where `{{timer}}` is the text input box. By manipulating the closing parenthesis and sending `10000');alert('yo` into the box, an alert appears. 

5. After looking through the code and playing with a few different URL combinations, I found that adding `javascript:` to the end of the sign-up URL successfully executed the JS following the statement. I then used the URL `xss-game.appspot.com/level5/frame/signup?next=javascript:alert('yo!')`, pressed the `Next >>` and passed the challenge!

6. The site automatically executes any JS file attached to the end of the URL (instead of `/static/gadget.js`). I knew that I needed to add a statement that would make it execute `alert('yo')`. I tried adding `javascript: `, as with challenge 5, but that didn't work. I then made a GitHub gist that executed an alert and just put the raw file in the URL. 
https://xss-game.appspot.com/level6/frame#Https://gist.githubusercontent.com/lukejmann/626c84f9da9c16934a0059cd2fa4d65f/raw/f53bff24da9935932e766ae28bcae2e4b746df41/yo.js. This did not work  (not sure why) so I experimented with trying different callbacks to get around any URL checks in the code. I eventually used Google's JS alert callback (`Https://www.google.com/jsapi?callback=alert`), for the complete URL of `https://xss-game.appspot.com/level6/frame#Https://www.google.com/jsapi?callback=alert`, which worked! I capitalized the `H` to get around the code's explicit check for `http`.