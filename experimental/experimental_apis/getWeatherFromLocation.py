#!/usr/bin/env python
# encoding: utf-8

### IMPORTS

import yweather
import sys

from weather import Weather

### CLIENTS

client = yweather.Client()
weather = Weather()


### FUNCTIONS

def getWoeidFromLocation(location):
	return client.fetch_woeid(location)

def getConditionFromCity(city):
	location = weather.lookup_by_location(city)
	return location.condition()



