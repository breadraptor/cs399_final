#!/usr/bin/env python

import os, sys, webapp2

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

from app.handlers import index, profiles, splash, challenge

app = webapp2.WSGIApplication([
    ('/main', index.MainHandler),
    ('/Erin', profiles.Erin),
    ('/Jack', profiles.Jack),
    ('/Nancy', profiles.Nancy),
    ('/Sarah', profiles.Sarah),
    ('/David', profiles.David),
	('/splash', splash.SplashHandler),
	('/new', challenge.ChallengeHandler),
	('/', splash.SplashHandler)

], debug=True)

def main():
    app.run()
	
if __name__ == "__main__":
    main()