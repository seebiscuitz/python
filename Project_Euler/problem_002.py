#     - projecteuler.net -
#
# Problem 2:
#	Even Fibonacci Numbers
#
# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
#	1, 2, 3, 5, 8, 13, 21, 34, 55, 89
#
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

# Created on: 	26/12/2016
# Last Updated:	26/12/2016

#imports
import sys
import math

#splash
print	""
print	"				-dx4-			"
print	""
#\splash 

#program begins
flag = 1;
total = 2;
i1 = 1;
i2 = 2;
tsum = 0;
fib = 0;
total = 0;


#while begins
while flag:
	if fib >= 4000000:
		flag = 0;
	else:
		fib = i1 + i2;
		if (fib%2==0):
			total = total + fib;
		i1 = i2;
		i2 = fib;
#while ends

print "The sum total is ", total + 2
print 