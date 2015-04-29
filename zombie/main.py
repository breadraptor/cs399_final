#!/usr/bin/env python

import os, sys, webapp2

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

from app.handlers import index, profiles, splash

app = webapp2.WSGIApplication([
    ('/main', index.MainHandler),
    ('/Erin', profiles.Erin),
    ('/Jack', profiles.Jack),
	('/splash', splash.SplashHandler),
	('/', splash.SplashHandler)

], debug=True)

def main():
    app.run()
	
if __name__ == "__main__":
    main()