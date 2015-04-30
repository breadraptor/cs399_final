import webapp2
from google.appengine.api import users
from app.models.models import *
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))

class SplashHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template_values = {}
        if user:
            url = users.create_logout_url('/')
            url_linktext = 'Logout'
            greeting = "Goodbye, " + user.nickname()
            self.redirect('/main')
        else:
            url = users.create_login_url('/main')
            url_linktext = 'Login'
            greeting = "Hello, you."

        template_values = {
          'greetings': greeting,
          'user': user,
          'url': url,
          'url_linktext': url_linktext
        }
        template = env.get_template("splash.html")
        self.response.out.write(template.render(template_values))