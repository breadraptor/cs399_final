import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users

class SplashHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world!')
        
        user = users.get_current_user()
        template_values = {}
        if user:
            url = users.create_logout_url('/')
            url_linktext = 'Logout'
            greeting = "Goodbye, "
        else:
            url = users.create_login_url('/main')
            url_linktext = 'Login'
            greeting = "Hello, you."

        template_values = {
          'greetings': greeting ,
          'user': user,
          'url': url,
          'url_linktext': url_linktext
        }
         
        
        self.response.out.write(template.render("splash.html", template_values))
    
app = webapp2.WSGIApplication([
    ('/', SplashHandler)
], debug=True)