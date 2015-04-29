from google.appengine.ext import ndb
from google.appengine.api import users

class ChallengesCompleted(ndb.Model):
    username = ndb.StringProperty(required=True)
    challenge = ndb.StringProperty(required=True)

class Challenge(ndb.Model):
    username = ndb.StringProperty(required=False)
    challenge = ndb.StringProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)
	
#class Point(ndb.Model):
#    description = ndb.StringProperty()
#    creator = ndb.UserProperty()
#    location = ndb.GeoPtProperty(0.0)