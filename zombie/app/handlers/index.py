#!/usr/bin/env python

import webapp2
from google.appengine.api import users
import app.models.models as models
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))

def make_map_url(map_points):
  map_url = "http://maps.googleapis.com/maps/api/staticmap?scale=false&size=500x300&maptype=satellite&format=png&visual_refresh=true&"
  #markers=size:mid%7Ccolor:0x0000ff%7Clabel:0%7C35.2028+N,+111.6644+W&
  #markers=size:mid%7Ccolor:0x804040%7Clabel:1%7CNorthern+Arizona+University"
  point_counter = 0
  for point in map_points:
    map_url += "markers=size:mid%7Ccolor:0x"
    if point.description == "water":
      map_url += "0000ff"
    elif point.description == "food":
      map_url += "21D131"
    elif point.description == "weapons":
      map_url += "FF0A23"
    elif point.description == "shelter":
      map_url += "5C4E17"
    else:
      map_url += "804040"
    map_url += "%7Clabel:"
    map_url += "%7C"
    point_counter += 1
    map_url += point.lat + ","
    map_url += point.lon + "&"
  return map_url

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
        map_items = models.Point.query()
        map_url = make_map_url(map_items)

        template_values = {
          'greetings': greeting ,
          'user': user,
          'url': url,
          'url_linktext': url_linktext,
          'challenges': challenges,
          'total': total,
          'map_url': map_url
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