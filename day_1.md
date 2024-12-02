# DAY 1 #

T10 if I come back here

10.50.29.68 --linux ops station -- 192.168.65.20
10.50.23.247 -- windows -- 192.168.65.10

exploit-DB 

https://cctc.cybbh.io/students/students/latest/Day_0_Setup.html#_vta_stack_build_for_opstations

https://sec.cybbh.io/public/security/latest/index.html

https://vta.cybbh.space/project/stacks/stack/340d1ccd-8195-4311-aeaa-1cf658983e6e/

http://10.50.20.103:8000/challenges


16	DIWI-007-M	ky7GNfiXMcZSxFC	10.50.33.72   i can only run ping from this machine    https://vta.cybbh.space/project/instances/
only use ping from this box 
it is a red host box ##DO NOT USE NMAP // NC ###

host enumeration 
check the symbolic link permisions
configuriation file .conf /var/log usr/bin /sbin dont cat the binary 
file and folder permisions 
find out how to figure out what permisions you are missing
dont use banned ports 
control sockets 

mefx == red team testing 
___________________________________________________________________________________________________________________________________________________________________________________________

# 01-pentesting-overview #

find ip addresses from websites 
find services 
find exploitation processes 
gain a foothold 


Establish persistence
Escalate privileges
Cover your tracks
Exfiltrate target data

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

OPNOTES == taking notes as you are going through // think you are asking someone to take over for you 

formalized = mission report = excutive or techinical summarys 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Vulnerability and Exploitation Research #

what is now the most common method for gaining initial access?
Phishing!

Exploit Development occurs from vulnerability pairing and mission-drivens requirement
Test and verify success
Testing provides a number of benefits:
Faster time to breakout of initial foothold
Reduced risk of detection and/or tool failure
Improved recovery times
Plan
Procure Hardware and software
Assign developer
Assign a tester to develop TTPs and break it
Document testing results
Testing environment

recreate a target system in a local network to test exploits 

------------------------------------------------------------------

# Scanning and Reconnaissance #


Documentation
Why is it important?
What should we include in documentation?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ LEFT OFF HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^ https://sec.cybbh.io/-/public/-/jobs/875707/artifacts/slides/02-network-scanning-and-recon.html



nmap --script <filename>|<category>|<directory>
nmap --script-help "ftp-* and discovery"
nmap --script-args <args>
nmap --script-args-file <filename>
nmap --script-help <filename>|<category>|<directory>
nmap --script-trace


# setting up a master socket #

ssh -MS /tmp/jump student@10.50.33.72 *named jump cus it goes to the jump box* 

*I am now on the red side jumpbox i can only run ping from this machine*

# time to ping sweep

for i in {97..126}; do (ping -c 1 192.168.28.$i | grep "bytes from" &); done

-
64 bytes from 192.168.28.97: icmp_seq=1 ttl=64 time=4.14 ms

64 bytes from 192.168.28.98: icmp_seq=1 ttl=63 time=5.03 ms

64 bytes from 192.168.28.99: icmp_seq=1 ttl=63 time=4.59 ms

64 bytes from 192.168.28.100: icmp_seq=1 ttl=63 time=11.4 ms

64 bytes from 192.168.28.105: icmp_seq=1 ttl=63 time=1.67 ms

64 bytes from 192.168.28.111: icmp_seq=1 ttl=63 time=1.52 ms

64 bytes from 192.168.28.120: icmp_seq=1 ttl=63 time=1.17 ms

-

# setting up forwarding  

ssh -S /tmp/jump jump -O forward -D 9050 *no output*

# time to scan 

proxychains nmap 192.168.28.100,111
* it should be fast asf *
  
map scan report for 192.168.28.100
PORT     STATE SERVICE
80/tcp   open  http
2222/tcp open  EtherNetIP-1

Nmap scan report for 192.168.28.111
PORT     STATE SERVICE
80/tcp   open  http
2222/tcp open  EtherNetIP-1
8080/tcp open  http-proxy

Nmap scan report for 192.168.28.97
All 1000 scanned ports on 192.168.28.97 are closed

Nmap scan report for 192.168.28.98
PORT   STATE SERVICE
53/tcp open  domain

Nmap scan report for 192.168.28.99
PORT   STATE SERVICE
53/tcp open  domain

Nmap scan report for 192.168.28.105
PORT     STATE SERVICE
21/tcp   open  ftp
23/tcp   open  telnet
2222/tcp open  EtherNetIP-1

Nmap scan report for 192.168.28.120
PORT     STATE SERVICE
4242/tcp open  vrml-multi-use



# test the ports with nc #

 proxychains nc 192.168.28.100 80

 HTTP/1.1 400 

 proxychains nc 192.168.28.100 2222

SSH-2.0-OpenSSH
 
## DO NOT USE WGET ON WEB SERVERS ##


ssh -S /tmp/jump jump -O forward  -L 1111:192.168.28.100:80 -L 2222:192.168.100:2222 -L 3333:192.168.28:111 -L 5555:192.168.28.111:2222
                            ^^ opening on me to talk to port 80 ^^^^^                               ^^^
                                                                      my quad 2222 to his quad 2222   ^^^^
                                                                                                          my 3333 talking to his 80 

*skipped 4444/6666 cus it linked to metasploit*
*i can use any ports i want on my local machine*


# launch firefox from terminal / jump box #
firefox
127.0.0.1:3333 



port intergiation 
proxychains nc 192.168.28.100[111] [80,2222] ** not able to be used like this ** justwritten this way for speed **

port forward to found ports 
ssh -S /tmp/jump jump -O forward  -L 1111:192.168.28.100:80 -L 2222:192.168.100:2222 -L 3333:192.168.28:111 -L 5555:192.168.28.111:2222

auhenticate with first target 
lin-ops :: ssh -MS /tmp/t1 creds@127.0.0.1 -p 2222
                                                ^^^^ goes through the 2222 to talk to the 192.168.100

# ping sweep the new network

for i in {20..40}; do (ping -c 1 100.200.25.$i | grep "bytes from" &); done

*found 100.200.25.30 and .35*

# port forward 



ssh -S /tmp/jump jump -O cancel -9050  *to cancel tunnel change forward to cancel *

ssh -S /tmp/t1 t1 -O forward 9050 

## scan 
proxy nmap them 

got ports 

proxychains nc the ports to verify services running on the machine 

ssh -S /tmp/t1 -O forward -L2323:new ip:(port found open) -L2324:new ip:(other port found open) -L2325:(other new ip):(port open) -L2326:(other new ip):(other port found open)

ssh -MS /tmp/t2 creds@127.0.0.1 -p 2323



OPS STATION--
ssh -S /tmp/jump jump -O forward -D 9050

proxychains nmap --script=http-enum.nse 192.168.28.100

firefox 
127.0.0.1:1111/admin/login.php







