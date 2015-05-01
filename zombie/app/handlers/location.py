#!/usr/bin/env python

import webapp2
from google.appengine.api import users
import app.models.models as models
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))

class LocationHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template_values = {}
        if user:
            url = users.create_logout_url('/')
            url_linktext = 'Logout'
            greeting = "Hello, " + user.nickname()

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
        template = env.get_template("new_location.html")
        self.response.out.write(template.render(template_values))
        
    def post(self):
        user = users.get_current_user()
        template_values = {}
        if user:
            # put the new challenge in the db
            lat = self.request.get('lat')
            lon = self.request.get('lon')
            sort_of_thing = self.request.get('type')
            obj = models.Point(lat= lat, lon=lon, description=sort_of_thing)
            obj.user = user
            obj.put()
            self.response.out.write("<div style='padding-top:100px; padding-left:100px;'>It's been added! Go check it out. <a href='/main'>Click here</a> to return home.</div>")
        else:
            self.response.out.write("<div style='padding-top:100px; padding-left:100px;'>You must be logged in to make a challenge.<br><br><a href='/'>Login</a></div>")
