#!/usr/bin/env python

import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
import datetime
import models.ChallengesCompleted as ChallengesCompletedClass
import models.Challenge as ChallengeClass

class MainHandler(webapp2.RequestHandler):
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
        challenges = ChallengeClass.Challenge.query().fetch() # pure list of challenges, one per row
        total = len(ChallengesCompletedClass.ChallengesCompleted.query().fetch()) # one row for each challenge that one person has completed
        template_values = {
          'greetings': greeting ,
          'user': user,
          'url': url,
          'url_linktext': url_linktext,
          'challenges': challenges,
          'total': total
        }
        
        self.response.out.write(template.render("index.html", template_values))
        
    def post(self):
        user = users.get_current_user()
        if user:
            # put the completed challenge in the db
            username = user.nickname()
            challenge = self.request.get('challenge')
            obj = ChallengesCompletedClass.ChallengesCompleted(username=username, challenge=challenge)
            obj.put()
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            greeting = "Hello, you."
        self.redirect('/main')
        
class Erin(webapp2.RequestHandler):

       def get(self):
        #self.response.write('Hello world!')
        
        user = users.get_current_user()
        template_values={}
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
         
        
        self.response.out.write(template.render("Erin.html", template_values))
class Jack(webapp2.RequestHandler):

       def get(self):
        #self.response.write('Hello world!')
        
        user = users.get_current_user()
        template_values={}
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
        self.response.out.write(template.render("Jack.html", template_values))

app = webapp2.WSGIApplication([
    ('/main', MainHandler),
    ('/Erin', Erin),
    ('/Jack', Jack),

], debug=True)
    
# IMPORTANT: this has some dummy Challenge data to test on, if you run populate().
class Migrate:
    def populate(self):
        obj = Challenge(username="Nancy", challenge="Climb a tree")
        obj.put()
        obj = Challenge(username="Erin", challenge="Play some L4D")
        obj.put()
        obj = Challenge(username="Jack", challenge="Run a mile")
        obj.put()
        obj = ChallengesCompleted(username="Nancy", challenge="Play some L4D") # this brings the days you survive up
        obj.put()