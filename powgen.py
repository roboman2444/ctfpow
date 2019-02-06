#!/usr/bin/env python3.7
import hashlib
import random
import string
import sys

try:
	diff = int(sys.argv[1])
except:
	diff = 5
prec = 'wpictf2019pow'

solveurl = 'https://github.com/roboman2444/ctfpow/blob/master/powsolve.py'
print('WPICTF proof of worky\nUse ' + solveurl + ' to solve\nChallenge:')
prec+= ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


sham = ''.join(random.choices(string.ascii_lowercase, k=diff))

m = hashlib.sha3_256()
m.update(prec.encode("utf-8"))
m.update(sham.encode("utf-8"))
soldo = str(m.hexdigest())
print('./powsolve.py ' + prec + ":" + str(diff) + ":" + soldo)




#shammy = prec + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))



solved = input('Enter solution:').strip()
#if not solved.startswith(prec):
#	print("Given solution does not start with " + prec)
#	return 1
#prec = solved[

m = hashlib.sha3_256()
m.update(solved.encode("utf-8"))
if str(m.hexdigest()) != soldo:
	print("Given solution is not valid, must hash to " + soldo)
	exit(1)

print('Correct')
exit(0)
