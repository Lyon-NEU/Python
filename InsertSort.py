#!/usr/bin/env python
#see git-hub Lyon-NEU
import sys
def insertSort(arr):
	"""
	insert sort: arr the array to be sorted
	"""
	if len(arr)<=1:
		return
	for j in range(len(arr)-1):
		key=arr[j+1]
		i=j
		while i>=0 and arr[i]>key :
			arr[i+1]=arr[i]
			i--
		arr[i+1]=arr[i]
def InsertionSort(A):
	for j in range(1,len(A)):
		key=A[j]
		i=j-1
		while (i>=0) and (A[i]>key):
			A[i+1]=A[i]
			i=i-1
		A[i+1]=key	
def main():
	"""
	test
	"""
	test=[50,10,20,100,90,30,70,40,80,60]
	for x in test:
		print(x)
	print('\n')
	insertSort(test)
	for y in test:
		print(y)
if __name__ == '__main__':
	main()