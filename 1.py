""" Problem 1 """ 
import time 

starttime = time.clock()
print "Problem 1: ", sum([i for i in xrange(1000) if i % 3 == 0 or i % 5 == 0]), " time: ", time.clock() - starttime 
