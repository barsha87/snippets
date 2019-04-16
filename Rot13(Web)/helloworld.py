import os
import webapp2
import jinja2

import rot13
import signup

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

class Art(db.Model): #table
    title = db.StringProperty(required = True)
    artwork = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class MainPage(Handler):
    def get(self):
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
        self.render("ascii.html", arts=arts)

    def post(self):
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
        title = self.request.get('title')
        artbox = self.request.get('artbox')
        if title and artbox:
            a = Art(title=title, artwork=artbox)
            a.put() #put in db
            self.redirect('/')
        else:
            error="Please fill in both fields!!"
            self.render("ascii.html", getTitle=title, getArt=artbox, getError=error, arts=arts)
                

application = webapp2.WSGIApplication([('/', MainPage),
                                       ('/rot13', rot13.Rot13Page),
                                       ('/signup', signup.SignUpPage),
                                       ('/welcome', signup.WelcomePage)
                                       ],
                                      debug=True)

