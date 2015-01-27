#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
val1 = form.getvalue('name')
val2 = form.getvalue('family')
print "Content-type:text/html"
print
print "The name is: <br/>"
print val1
print "<br/>"
print "The family is: <br/>"
print val2
print """<form method="post" action="page1.py">

<textarea name="birthday" cols="40" rows="5">
Enter birthday here ...
</textarea>
<br/>
<textarea name="hobby" cols="40" rows="5">
Enter hobby here ...
</textarea>
<br/>
<input type="submit" value="Submit">
</form>"""

