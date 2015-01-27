#!/usr/bin/env python
import cgi

form = cgi.FieldStorage()
val1 = form.getvalue('birthday')
val2 = form.getvalue('hobby')
print """Content-type:text/html

<form method="post" action="page2.py">
<textarea name="name" cols="40" rows="5">
Enter name here ...
</textarea>
<br/>
<textarea name="family" cols="40" rows="5">
Enter family here ...
</textarea>
<br/>
<input type="submit" value="Submit">
</form>
The birthday is: <br/> %s <br/>
The hobby is: <br/> %s
""" %(val1, val2)


