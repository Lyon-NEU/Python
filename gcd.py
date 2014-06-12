#!/usr/bin/env python
#see
#Tutorial code  from ..
def gcd(x,y,depth=1):
	'''
	Find the greatest commom divisor of x,y
	'''
	result=x
	if y!=0:
		indent="**"*depth
		print(("%s About to recursively call gcd (%d, %d)" % (indent,y,x%y) ) )
		result=gcd(y,x%y,depth+1)
		print(("%s result is %d" %(indent,result)))
	return result
def main():
	m=77
	n=28
	print(("Finding gcd(%d, %d)" % (m,n)))
    g = gcd(m,n)
    print(('Greatest common divisor of %d, %d = %d' % (m, n, g)))
if __name__ == '__main__':
	main()