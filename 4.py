""" Problem 4 """
import time 

def isPalindrome(n):
	return str(n)[::-1] == str(n)

starttime = time.clock()

highest = 1
for first in xrange(999, 900, -1):
	for second in xrange(900, 999-(999-first), 1):
		total = first * second 
		if total > highest: 
			if isPalindrome(total): 
				highest = total

print "Problem 4: ", highest, " time: ", time.clock() - starttime 