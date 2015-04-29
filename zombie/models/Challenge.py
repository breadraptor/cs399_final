from google.appengine.ext import ndb

class Challenge(ndb.Model):
    username = ndb.StringProperty(required=False)
    challenge = ndb.StringProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)