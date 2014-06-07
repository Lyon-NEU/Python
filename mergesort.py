#!/usr/bin/evn python 
# see
import sys

def merge(arr,left,mid,right):
	"merge left...mid and mid+1...right"
	#copy left and right
	L=arr[left:mid+1]
	R=arr[mid+1:right+1]
	#L.extend(arr[left:mid+1])
	#R.extend(arr[mid+1:right+1])
	L.append(1000)
	R.append(1000)
	i=0
	j=0
	k=left
	while k<=right:
		#pass
		if L[i]<=R[j]:
			arr[k]=L[i]
			i+=1
		else:
			arr[k]=R[j]
			j+=1
		k+=1
	del L
	del R

def mergesort(arr,left,right):
	"recursive solve"
	if left<right:
		#pass
		mid=int((left+right)/2)
		mergesort(arr,left,mid)
		mergesort(arr,mid+1,right)
		merge(arr,left,mid,right)

def main():
	#pass
	test=[50,10,20,100,90,30,70,40,80,60]
	for x in test:
		print (x)
	print('\n')
	mergesort(test,0,9)
	for y in test:
		#pass
		print(y)
	print("\n")
if __name__ == '__main__':
	main()