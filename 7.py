""" Problem 7 """ 
import time 

def is_prime(n):
	if n < 2: 
		return False
	elif n  == 2 or n == 3: 
		return True
	elif n % 2 == 0 or n % 3 == 0: 
		return False
	else: 
		for x in xrange(5, int(n**0.5)+1, 6):
		    if n % x == 0 or n % (x + 2) == 0:
		        return False
	return True

starttime, count, num, overall = time.clock(), 1, 1, 10001
while count != overall - 1:
	num += 2
	if is_prime(num):
		count += 1

print "Problem 7: ", num, " time: ", time.clock() - starttime 