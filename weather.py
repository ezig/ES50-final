APIKEY = "83215ca074d35d0adc3c85fcd2062946"

import json
import urllib2

def toFahrenheit(temp):
	"""Converts from kelvin to fahrenheit"""

	return (float(temp) - 273.15) * 1.8 + 32

class Weather:

	def __init__(self):
		"""Gets location based on IP address (may be problematic on Harvard network)"""

		f = urllib2.urlopen('http://freegeoip.net/json/')
		geoJSON = f.read()
		f.close()
		geo = json.loads(geoJSON)
		self.location = geo['city'] + ',' + geo['region_code']
		
		#If something went wrong with the location fetching,
		# assume we're in Cambridge (our fair city)
		if self.location == ',':
			self.location = "Cambridge,MA"

	def getWeather(self):
		address = 'http://api.openweathermap.org/data/2.5/weather?q=' + self.location + '&APPID=' + APIKEY
		f = urllib2.urlopen(address)
		weatherJSON = f.read()
		f.close()
		weather = json.loads(weatherJSON)
		return round(toFahrenheit(weather['main']['temp']),1)
	
