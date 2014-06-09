#!/usr/bin/env python
#see git-hub Lyon-NEU
import sys

def bubbleSort(arr):
	"Bubble sort"
	for i in range(len(arr)):
		exchange=False
		for j in range(len(arr)-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
				exchange=True
		if exchange == False:
			return
def main():
	"test"
	test=[50,10,20,100,90,30,70,40,80,60]
	for x in test:
		print (x)
	print('\n')
	bubbleSort(test)
	for y in test:
		#pass
		print(y)
	print("\n")
if __name__ == '__main__':
	main()