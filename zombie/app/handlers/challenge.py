#!/usr/bin/env python

import webapp2
from google.appengine.api import users
import app.models.models as models
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))

class ChallengeHandler(webapp2.RequestHandler):
    def get(self):    
        user = users.get_current_user()
        template_values = {}
        if user:
            url = users.create_logout_url('/')
            url_linktext = 'Logout'
            greeting = "Hello, "

        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            greeting = "Hello, you."
       
        template_values = {
          'greetings': greeting ,
          'user': user,
          'url': url,
          'url_linktext': url_linktext
        }
        template = env.get_template("new.html")
        self.response.out.write(template.render(template_values))
        
    def post(self):
        user = users.get_current_user()
        template_values = {}
        if user:
            # put the new challenge in the db
            username = user.nickname()
            challenge = self.request.get('challenge')
            obj = models.Challenge(username=username, challenge=challenge)
            obj.put()
            self.response.out.write("<div style='padding-top:100px; padding-left:100px;'>Your challenge has been added! <a href='/main'>Click here</a> to return home.</div>")
        else:
            self.response.out.write("<div style='padding-top:100px; padding-left:100px;'>You must be logged in to make a challenge.<br><br><a href='/'>Login</a></div>")
