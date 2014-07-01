import os,codecs,math
class BayesText (object):
	"""docstring for BayesText This class implements a naive approach to text classification"""
	def __init__(self, trainingdir,stopwordlist):
		#super(BayesText , self).__init__()
		#self.arg = arg
		self.vocabulary={}
		self.prob={}
		self.totals={}
		self.stopwords={}
		f=open(stopwordlist)
		for line in f:
			self.stopwords[line.strip()]=1
		f.close()
		categories=os.listdir(trainingdir)
		#filter out files that are not directory
		self.categories=[filename for filename in categories if os.path.isdir(trainingdir+filename)]
		print("Counting......")
		for category in self.categories:
			print(' '+category)
			(self.prob[category],self.totals[category])=self.train(trainingdir,category)
		#I am going to eliminate any word in the vocabulary tha dosen't occure at least 3 times
		toDelete=[]
		for word in self.vocabulary:
			if self.vocabulary[word]<3:
				#mark word for delete
				toDelete.append(word)
		#now delte
		for word in toDelete:
			del self.vocabulary[word]
		vocabLength=len(self.vocabulary)
		print("Computing Probabilities:")
		for category in self.categories:
			print(' '+category)
			denominator=self.totals[category]+vocabLength
			for word in self.vocabulary:
				if word in slef.prob[category]:
					count=self.prob[category][word]
				else:
					count=0
			self.prob[category][word]=(count+1.0)/denominator

	def train(self,trainingdir,category)：
		"""count word occurrence for a paticulary category"""
		currentdir=trainingdir+category
		files=os.listdir(currentdir)
		counts={}
		total=0
		for file in files:
			f=codecs.open(currentdir+'/'+file,'r','iso8859-1')
			for line in f:		
				tokens=line.split()
				for token in tokens:
					#get rid of punctuaction and lowercase word
					token=token.strip('\'".,?:-')
					token=token.lower()
					if token != '' or not in self.stopwords:
						self.vocabulary.setdefault(token,0)
						self.vocabulary[token]+=1
						counts.setdefault(token,0)
						counts[token] += 1
						total += 1
			f.close()
		return(counts,total)

	def classify(self, filename):
		results={}
		for category in self.categories:
			results[category] = 0
		f=codecs.open(filename,'r','ios8859-1')
		for line in f:
			tokens=line.split()
			for token in tokens:
				token=token.strip('\'".,?:-').lower()
				if token in self.vocabulary:
					for category in self.categories:
						results[category]+=math.log(self.prob[category][token])
			f.close()
		results=list(results.item())
		results.sort(key=lambda tuple:tuple[1],reverse=True)
		return results[0][0]
	def testCategory(self,directory,category):
		files=os.listdir(directory)
		total=0
		correct=0
		for file in files:
			total+=1
			result=self.classify(directory+file)
			if result == category:
				correct+=1
		return (correct,total)
	def test(self,testdir):
		"""
		Test all fiels in the test direcotru 
		"""
		categories=os.listdir(testdir)
		categories=[filename for filename in categories if os.path.isdir(testdir+filename)]
		correct=0.0
		total=0.0
		for category in categories:
			(catCorrect,catTotal)=self.testCategory(testdir+category+'/',category)
			correct+=catCorrect
			total+=catTotal
		print("Accuracy is %f%% (%i test instances)" %((correct / total)*100,total)

if __name__ == '__main__':
	#main()