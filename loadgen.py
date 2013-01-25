import random
import time

__author__ = 'Rory'

millis = int(round(time.time() * 1000))
random.seed(millis)

while True:
	for i in range(0,9999):
		for j in range(0,9999):
			load = i + j
	length = random.randint(1,60)
	time.sleep(length)
