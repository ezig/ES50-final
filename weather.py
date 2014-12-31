import json
import urllib2

def toFahrenheit(temp):
	"""Converts from kelvin to fahrenheit"""

	return (float(temp) - 273.15) * 1.8 + 32

class Weather:

	def __init__(self):
		"""Gets location based on IP address (will be problematic if the IP address is private)"""

		try:
			f = urllib2.urlopen('http://freegeoip.net/json/')
			geoJSON = f.read()
			f.close()
			geo = json.loads(geoJSON)
			self.location = geo['city'] + ',' + geo['region_code']
		
		except:
			#If something went wrong with the location fetching,
			# assume we're in Cambridge (our fair city)
			self.location = "Cambridge,MA"

	def getWeather(self):
		"""Gets the temperature in Kelvin from openweathermap"""

		address = 'http://api.openweathermap.org/data/2.5/weather?q=' + self.location
		f = urllib2.urlopen(address)
		weatherJSON = f.read()
		f.close()
		weather = json.loads(weatherJSON)
		return int(toFahrenheit(weather['main']['temp']))
	
