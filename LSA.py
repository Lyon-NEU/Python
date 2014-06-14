#!/usr/bin/env python
#see
from numpy import zeros
from scipy.linalg import svd

titles=
[
"The Neatest Little Guide to Stock MarketInvesting",
"Investing For Dummies, 4thEdition",
"The Little Book of Common SenseInvesting: The Only Way to Guarantee Your Fair Share of StockMarket Returns",
"The Little Book of ValueInvesting",
"Value Investing: From Graham to Buffettand Beyond",
"Rich Dad's Guide toInvesting: What the Rich Invest in, That the Poor and the MiddleClass Do Not!",
"Investing in Real Estate, 5thEdition",
"Stock Investing ForDummies",
"Rich Dad's Advisors: The ABC's of RealEstate Investing: The Secrets of Finding Hidden Profits MostInvestors Miss"
]
stopwords=['and','edition','for','in','little','of','the','to']
ignorechars=''''',:'!'''
class LSA(object):
	def __init__(self,stopwords,ignorechars):
		self.stopwords=stopwords
		self.ignorechars=ignorechars
		self.wdict={}
		self.dcount=0