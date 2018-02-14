#!/usr/bin/python

def pattern3(noOfRows):
	for i in range (noOfRows+1):
		for j in range (noOfRows - i):
			print ' ',
		for k in range (i):
			print '*',
		print
pattern3(5)
