import webapp2
import cgi
html="""
<!DOCTYPE html>
<html>
    <head>
        <title>ROT13</title>
    </head>
    <body>
    <br><br>
    <h1>Enter some text to ROT13:</h1>
    <br>
        <form method="post">
            <textarea name=text rows=6 cols=50>%s</textarea>
            <br>
            <input type=submit>
        </form>
    </body>
    </html>
"""

def get13(text=""):
    s=''
    for i in text:
        n=ord(i)
        if n in range(ord('a'),ord('n')) or n in range(ord('A'),ord('N')):
            s+=(chr((n)+13))
        elif n in range (ord('n'),ord('z')+1) or n in range (ord('N'),ord('Z')+1):
            s+=(chr((n)-13))
        else:
            s+=i
    return s

class Rot13Page(webapp2.RequestHandler):

    def writeform(self,stuff=""):
        self.response.write(html % stuff)

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write(html)
        self.writeform()
        
    def post(self):
        text=self.request.get('text')
        stuff=get13(text)
        stuff=cgi.escape(stuff, quote=True)
        self.writeform(stuff)

application = webapp2.WSGIApplication([('/rot13', Rot13Page),
                                       ],
                                      debug=True)


"""@import './ascii_design.css'"""
