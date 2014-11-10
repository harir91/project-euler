""" Problem 9 """ 
import time

def pytho_trip(n):
	for a in xrange(1, int(n/2)):
		for b in xrange(1, n-a):
			c = 1000 - a - b 
			if ((a ** 2) + (b ** 2)) == (c ** 2):
				return a * b * c

starttime = time.clock()
print "Problem 9: ",  pytho_trip(1000), " time: ", time.clock() - starttime 
