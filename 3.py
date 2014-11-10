""" Problem 3 """
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
	
starttime = time.clock()
num = 600851475143
check = int(num ** 0.5) + 1 
if check % 2 == 0:
	check -= 1 
Found = False
while check > 2 and not Found:
	check -= 2 
	if num % check == 0 and is_prime(check): 
		Found = True

print "Problem 3: ", check, " time: ", time.clock() - starttime 