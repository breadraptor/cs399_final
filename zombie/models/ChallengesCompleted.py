from google.appengine.ext import ndb

class ChallengesCompleted(ndb.Model):
    username = ndb.StringProperty(required=True)
    challenge = ndb.StringProperty(required=True)
