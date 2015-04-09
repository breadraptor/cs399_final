#Using webapp2 framework...
#from webapp2 import RequestHandler, SWGIApplication
import webapp2

class SplashPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers["Content-Type"] = 'text/plain'
		self.response.write("Hello mars!")

app = webapp2.WSGIApplication([
	('/', SplashPage),
	], debug = True)