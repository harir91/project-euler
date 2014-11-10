""" Problem 2 """ 
import time 

starttime, a, b, total =  time.clock(), 0, 1, 0 
while b < 4000000:
	a, b = b, a + b
	if b % 2 == 0: 
		total += b

print "Problem 2: ", total, " time: ", time.clock() - starttime 
  