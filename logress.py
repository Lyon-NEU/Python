'''
'''
from numpy import *

def loadDataset():
	dataMat=[]
	labelMat=[]
	fr=open('testSet.txt')
	for line in fr.readlines():
		lineArr=line.strip().split()
		#x0,x1
		dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat,labelMat
def sigmoid(inX):
	return 1.0/(1+extp(-inX))
def gradAscent(dataMat,classLabels):
	dataMatrix=mat(dataMat)
	labelMat=mat(classLabels).transpose()  #convert
	m,n=shape(dataMatrix)
	alpha=0.001
	maxCycles=500
	weights=ones((n,1))
	for k in range(maxCycles):
		h=sigmoid(dataMatrix*weights)
		error=(labelMat-h)
		weights=weights+alpha*dataMatrix.transpose()*error
	return weights
def  plotBestFit(weights):
	import matplotlib.pyplot as plt
	dataMat,labelMat=loadDataset()
	dataArr==array(dataMat)
	n=shape(dataArr)[0]
	xcord1=[]
	ycord1=[]
	xcord2=[]
	ycord2=[]
	for i in range(n):
		if int(labelMat[i] == 1:
			xcord1.append(dataArr[i,1])
			ycord1.append(dataArr[i,2])
		else:
			xcord2.append(dataArr[i,1])
			ycord2.append(dataArr[i,2])
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
	ax.scatter(xcord2,ycord2,s=30,c='green')
	x=arange(-3.0,3.0,0.1)
	y=(-weights[0]-weights[1]*x)/weights[2]
	ax.plot(x,y)
	plt.xlabel('X1')
	plt.ylabel('X2')
	plt.show()