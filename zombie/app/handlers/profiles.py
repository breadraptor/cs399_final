#!/usr/bin/env python

import webapp2
from google.appengine.api import users
from app.models.models import *
import app.models.models as models
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))

        
class Erin(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        template_values={}
        challenges = len(models.ChallengesCompleted.query(models.ChallengesCompleted.username=='Erin').fetch())
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
          'url_linktext': url_linktext,
          'challenges_completed': challenges
        }
        template = env.get_template("Erin.html")
        self.response.out.write(template.render(template_values))

class Jack(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        template_values={}
        challenges = len(models.ChallengesCompleted.query(models.ChallengesCompleted.username=='Jack').fetch())
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
          'url_linktext': url_linktext,
		  'challenges_completed': challenges
        }
        template = env.get_template("Jack.html")
        self.response.out.write(template.render(template_values))