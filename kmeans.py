"""
A simple implemention of k-means
"""
import numpy as np
import matplotlib.pyplot as plt
import os,math
import random
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
		self.inCenter={}    # which cluster point belong to
		self.iternum=iternum
		self.k=k
		self.pointCount=0     # record how many points
		f=open(trainingdir) 
		for line in f.readlines():
			pts=line.strip().split(' ')
			points.append(pts)
			self.pointCount++
		f.close()
	def euclidDistance(self,point_1,point_2):
		"compute distance between two point"
		distance=0.0
		c=[x-y for x,y in zip(point_1,point_2)]
		d=lambda x:x*x
		d(c)
		distance=sqrt(sum(d))
		return distance 
	def normalize():
		"generize"
		pass
	def initialize(self):
		"random select k seed"
		for i in range(self.k):           #random seletct  k points as center 
			self.center.append(self.points[random.randint(0,self.pointCount)])
		print('---------####first k center####------------\n')
		print(self.center)
	def isEqual(vec1,vec2):
		"vec1[...] == vec2[...]"
		if len(vec1) !+ len(vec2:
			return false
		for i in range(len(vec1):
			if vec1[i] != vec2[i]:
				return false
		return true
	def printPoint():
		plt.title("k-means")
		plt.xlabel(u'dimension1')
		plt.ylabel(u'dimension2')
		plt.plot()
		plt.show()
	def update(self):
		'''
		iter until center not change or when iter iternum times
		'''
		toChange=true  #record if center points is change
		iterCount=1      #iter time
		while toChange and iterCount<=self.iternum:
			print('\nre-compute\n')
			#compute every point's center
			for i in range(self.pointCount):
				oldDistance=MAX
				for j in range(self.k):  #compute distance from the point to every center pooints
					newDistance=euclidDistance(pooints[i],center[j])
					if newDistance<oldDistance:
						oldDistance=newDistance
						self.inCenter[j].append(i)
			#re-compute center point of each cluster
			for i in range(k):
				c=self.inCenter[i] #list: saved points belongs this cluster
				#将每个维度的数据分别相加
				#分别除以点的个数，计算平均数
	def printResult():
		pass
	if __name__ == '__main__':
		#main()