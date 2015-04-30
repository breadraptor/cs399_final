#!/usr/bin/env python

import webapp2
from google.appengine.api import users
import app.models.models as models
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):      
        user = users.get_current_user()
        template_values = {}
        if user:
            url = users.create_logout_url('/')
            url_linktext = 'Logout'
            greeting = "Hello, "+user.nickname()

        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            greeting = "Hello, you."
        challenges = models.Challenge.query().order(-models.Challenge.date).fetch(8) # pure list of challenges, one per row
        total = len(models.ChallengesCompleted.query().fetch()) # one row for each challenge that one person has completed
        template_values = {
          'greetings': greeting ,
          'user': user,
          'url': url,
          'url_linktext': url_linktext,
          'challenges': challenges,
          'total': total
        }
        template = env.get_template("index.html")
        self.response.out.write(template.render(template_values))
        
    def post(self):
        user = users.get_current_user()
        if user:
            # put the completed challenge in the db
            username = user.nickname()
            challenge = self.request.get('challenge')
            obj = models.ChallengesCompleted(username=username, challenge=challenge)
            obj.put()
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            greeting = "Hello, you."
        self.redirect('/main')