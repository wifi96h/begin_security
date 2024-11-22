## Objectives

1>) Familiarization with SQL queries
  commands 
    union 
    select 
    select union select (puts them together to requests)

Is INFORMATION_SCHEMA Database available?

GET Request versus POST Request HTTP methods


SELECT :: Extracts data from a database

UNION ::Used to COMBINE the result-set of TWO OR MORE SELECT STATEMENTS


2>) Perform SQL injections

Unsanitized: input fields can be found using a Single Quote ⇒ '
SELECT id FROM users WHERE name=‘$name’ AND pass=‘$pass’;

User enters TOM' OR 1='1 in the username 
User enters TOM' OR 1='1 in the password fields

this is a post request ^^^^
 
if this is suceseful --

 go back -- you need to have these steps done before  submiting the above sql  
 
-- right click : INSPECT ACCESIBILITY PROPERTIES 

in the menu that opens at the bottom :: go to network tab 

submit credentials / login 

click the POST input feild in the menu on the bottom 

that opens a new menu hit the REQUEST tab that opens in the new menu 

switch to RAW its a toggle icon 

copy the entire feild 

go to the URL paste it after a question mark 

1 (the original) http://10.50.33.78/login.php

2 (add the question mark) http://10.50.33.78/login.php?

3 (final) http://10.50.33.78/login.php?username=TOM%27+OR+1%3D%271&passwd=TOM%27+OR+1%3D%271

test the new credentials 

3>) Identify unsanitized input fields

throw shit at the wall
