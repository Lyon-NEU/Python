"""
A simple implemention of k-means
"""
import numpy as np
import matplotlib.pyplot as py
import os,math

class KMeans:
	'''

	'''
	def __init__(self,k,iternum,trainingdir):
		'''
		k: cluster numnbers
		iternum: iter count
		'''
		self.points=[]      #all points
		self.center=[]       #center point
		self.iternum=iternum
		self.k=k
		f=open(trainingdir) 
		for line in f.readlines():
			pass
	def euclidDistance(point_1,point_2):
		"compute distance between two point"
		distance=0.0
		for i in range(len(point_1)):
			pass
		return distance 
	def normalize():
		"generize"
		pass
	def initialize():
		"random select k seed"
		pass
	def isEqual(vec1,vec2):
		"vec1[...] == vec2[...]"
		if len(vec1) !+ len(vec2:
			return false
		for i in len(vec1):
			if vec1[i] != vec2[i]:
				return false
		return true
	def printPoint():
		pass
	def update():
		pass
	def printResult():
		pass
	if __name__ == '__main__':
		#main()