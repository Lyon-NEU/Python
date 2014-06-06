#!/usr/bin/env python
# see git-hub Lyon-NEU
import sys
def Partition(arr,p,q):
	"part the array into two parts"
	if p<q:
		#pass
		return
	key=arr[p]
	i=0
	j=0
	i,j=p,q
	while i<j:
		while i<j and arr[j]<=key:
			j=j-1
		if i<j:
			arr[i]=arr[j]
		while i<j and arr[i]<=key:
			i=i+1
		if i<j:
			arr[j]=arr[i]
	arr[i]=key
	return i

def quicksort(arr,start,end):
	"quicksort"
	if start<end:
		#part=0
		part=Partition(arr,start,end)
		quicksort(arr,start,part-1)
		quicksort(arr,part+1,end)

if __name__ == '__main__':
	#main()
	test=[49,27,38,1,13,76,97,65]
	quicksort(test,0,len(test)-1)
	for x in test:
		#pass
		#print(x)
		sys.stdout.write("%d" % x)