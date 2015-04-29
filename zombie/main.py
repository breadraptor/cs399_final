#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
import datetime

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world!')
        
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
        
        challenges = Challenge.query().fetch(2)
        total = len(Challenge.query().fetch())
        template_values = {
          'greetings': greeting ,
          'user': user,
          'url': url,
          'url_linktext': url_linktext,
          'challenges': challenges,
          'total': total
        }
        
        self.response.out.write(template.render("index.html", template_values))
        
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


class Challenge(ndb.Model):
    username = ndb.StringProperty(required=False)
    challenge = ndb.StringProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)

