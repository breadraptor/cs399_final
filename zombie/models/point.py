import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users

class Point(ndb.Model):
    description = ndb.StringProperty()
    creator = ndb.UserProperty()
    location = ndb.GeoPtProperty(0.0)