#!/usr/bin/python

import random
import time
import urllib2

__author__ = 'Rory'

# Seed our random
millis = int(round(time.time() * 1000))
random.seed(millis)

# Define some sites to visit
sites = ["http://www.google.com", "http://www.yahoo.com", "http://www.facebook.com", "http://www.twitter.com"]

# Run continuously
while True:

	# Ramp up some CPU cycles
	isize = random.randint(5000,9999)
	for i in range(0,isize):
		jsize = random.randint(5000,9999)
		for j in range(0,jsize):
			load = i + j

	# Only use network 1/2 of the time
	if random.randint(0,1) == 0:
		# Make an http request
		try:
			url = sites[random.randint(0,len(sites)-1)]
			load = urllib2.urlopen(url).read()
		except urllib2.URLError as error:
			load = "http request failed"

	# Wait a random amount of time between 4 and 8 hours
	length = random.randint(60*60*4,60*60*8)
	time.sleep(length)
