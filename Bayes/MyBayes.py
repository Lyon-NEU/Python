'''
Created on July 18,2014
@authro Lyon-NEU
'''
import numpy as np
import matplotlib as plt

def loadDataSet():
	'''
	load data set
	'''
	postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec
 def createVocabList(dataSet):
 	'''
 	create voca
 	'''
 	vocabSet=set([])
 	for document in dataSet:
 		vocabSet=vocabSet|set(document)
 	return list(vocabSet)