import os
import webapp2
import jinja2
import re
import hmac

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Users(db.Model): #table
    username = db.StringProperty(required = True)
    password = db.StringProperty(required = True)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
MAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(pwd):
    return PASS_RE.match(pwd)

def valid_email(mail):
    return MAIL_RE.match(mail)


class SignUpPage(Handler):

    def get(self):
        self.render("signup.html")
        
    def post(self):
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
        user=''
        pw=''
        mail=''
        t1=''
        t4=''
        if not u or not p or not e:
            if not u:
                user = "That's not a valid username"
            if not p:
                pw = "That wasn't a valid password"
            if not e:
                mail = "That's not a valid email"
            t1 = username
            t4 = email
            self.render("signup.html", user=user, pw=pw, mail= mail, t1=t1, t4=t4)
        elif not password==verify:
            match = "The passwords don't match"
            t1 = username
            t4 = email
            self.render("signup.html", t1=t1, t4=t4)
        else:
            q = db.GqlQuery("SELECT * FROM Users WHERE username = :1", username)
            list(q)
            j=0
            for i in q:
               j+=1 
            if j>0:
                u = "Username already exists"
                self.render('signup.html', user=u)
            else:
                user = Users(username=username, password=password)
                user.put()
                h=hmac.new("nbv_12345", username).hexdigest()
                self.response.headers.add_header('Set-Cookie', 'user=%s' %str(username)+'|'+str(h))
                self.redirect('/welcome')

class WelcomePage(Handler):

    def get(self):
        username=self.request.cookies.get('user',None)
        if username:
            pos=username.find('|')
            user=username[:pos]
            h=username[pos+1:]
            hash2=hmac.new("nbv_12345", user).hexdigest()
            if h==hash2:
                self.write("<br><h1>Welcome, %s!</h1>" % user)
            else:
                self.redirect('/signup') 
        else:
            self.redirect('/signup')

"""class LoginPage(Handler):

    def get(self):
        username=self.request.cookies.get('user',None)
        if username:
            pos=username.find('|')
            user=username[:pos]
            h=username[pos+1:]
            hash2=hmac.new("nbv_12345", user).hexdigest()
            if h==hash2:
                self.write("<br><h1>Welcome, %s!</h1>" % user)
            else:
                self.redirect('/signup') 
        else:
            self.redirect('/signup')
    
    

"""
