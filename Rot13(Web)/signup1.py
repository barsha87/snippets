import webapp2
import cgi
import re

html="""
<!DOCTYPE html>
<html>
	<head>
		<title>Sign up page</title>
	</head>
	
	<body>
	   <br>
	   <h2>Signup</h2>
	   <br>
	   <form method=post>
		<label>
			Username&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
			<input name=username type=text value='%(t1)s'>
		</label>
		<label style=color:red>%(user)s</label>
		<br>
		<label>
			Password&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
			<input name=password type=password value=''>
		</label>
		<label style=color:red>%(pass)s</label>
		<br>
		<label>
			Verify Password
			<input name=verify type=password value=''>
		</label>
		<label style=color:red>%(match)s</label>
		<br>
		<label>
			Email (optional)&nbsp;&nbsp;
			<input name=email type=text value=%(t4)s>
		</label>
		<label style=color:red>%(mail)s</label>
		<br>
		<input type=submit>
	   </form>
	</body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
MAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(pwd):
    return PASS_RE.match(pwd)

def valid_email(mail):
    return MAIL_RE.match(mail)

d={'user':'', 'pass':'', 'match':'', 'mail':'', 't1':'', 't4':''}
class SignUpPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(html %d)
        
    def post(self):
        d={'user':'', 'pass':'', 'match':'', 'mail':'', 't1':'', 't4':''}
        username=self.request.get('username')
        password=self.request.get('password')
        verify=self.request.get('verify')
        email=self.request.get('email')
        u= valid_username(username)
        p= valid_password(password)
        if email=='':
            e=True
        else:
            e = valid_email(email)
            
        if not u or not p or not e:
            if not u:
                d['user'] = "That's not a valid username"
            if not p:
                d['pass'] = "That wasn't a valid password"
            if not e:
                d['mail'] = "That's not a valid email"
            d['t1'] = cgi.escape(username, quote=True)
            d['t4'] = cgi.escape(email, quote=True)
            self.response.write(html %d)
        elif not password==verify:
            d['match'] = "The passwords don't match"
            d['t1'] = cgi.escape(username, quote=True)
            d['t4'] = cgi.escape(email, quote=True)
            self.response.write(html %d)
        else:
            username=cgi.escape(username, quote=True)
            self.redirect('/welcome?username=%s' %username)

class WelcomePage(webapp2.RequestHandler):

    def get(self):
        username=self.request.get('username')
        self.response.write("<br><h1>Welcome, %s!</h1>" %username)

