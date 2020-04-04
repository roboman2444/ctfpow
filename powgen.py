#!/usr/bin/env python3
import hashlib
import random
import string
import sys


print(string.ascii_lowercase)

def powchal(diff, prec='wpictf2020pow'):
	solveurl = 'https://github.com/roboman2444/ctfpow/blob/master/powsolve.py'
	print('WPICTF proof of worky\nUse ' + solveurl + ' to solve\nChallenge:')
	prec+= ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


	sham = ''.join(random.choices(string.ascii_lowercase, k=diff))

	m = hashlib.sha3_256()
	m.update(prec.encode("utf-8"))
	m.update(sham.encode("utf-8"))
	soldo = str(m.hexdigest())
	print('./powsolve.py ' + prec + ":" + str(diff) + ":" + soldo)

	solved = input('Enter solution:').strip()
	m = hashlib.sha3_256()
	m.update(solved.encode("utf-8"))
	if str(m.hexdigest()) != soldo:
		print("Given solution is not valid, must hash to " + soldo)
		return False
	print('Correct')
	return True



if __name__ == '__main__':
	try:
		diff = int(sys.argv[1])
	except:
		diff = 5

	if not powchal(diff):
		exit(1)
