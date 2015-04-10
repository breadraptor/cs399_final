#Using webapp2 framework...
#from webapp2 import RequestHandler, SWGIApplication
import webapp2
import google.appengine.ext.ndb

class MartianPizza(ndb.Model):
	# localhost:8080/datastore to see
	name = ndb.StringProperty(required=True)
	toppings = ndb.StringProperty(repeated=True)
	# Example: ["cheese", "pepperoni"]
	microbes = ndb.IntegerProperty(default=10)
	price = ndb.IntegerProperty(default=0)

class SplashPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers["Content-Type"] = 'text/plain'
		self.response.write("Hello mars!")
		pizza = MartianPizza(name="Red Rover Pizza", toppings=["cheese","red sauce"], price=500)

app = webapp2.WSGIApplication([
	('/', SplashPage),
	], debug = True)