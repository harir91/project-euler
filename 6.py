""" Problem 6 """ 
import time 

starttime, start, end = time.clock(), 1, 100
print "Problem 6: ", sum(x for x in range(start, end+1))**2 - sum(x**2 for x in range(start, end+1)), " time: ", time.clock() - starttime 
