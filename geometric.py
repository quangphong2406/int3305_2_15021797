import math

def prob(n,p):
	return float((1-p)**(n-1)*p)

def infoMeasure(n, p):
	tmp = prob(n, p)
	if tmp==0 or tmp==1:
		return float(0)
	else:
		return float(-math.log2(tmp))
# print (infoMeasure(2,0.5))

def sumProb(N, p):
	'''
	with enough large N -> sumProb approach 1
	'''
	s = 0
	for i in range(1,N+1):
		s += prob(i, p)
	return float(s)

def approxEntropy(N, p):
	'''
	H(X)=sum(p(x)*I(x))
	approxEntropy(N, 0.5) ~ 2
	'''
	H = 0
	for i in range(1,N+1):
		H += prob(i,p)*infoMeasure(i, p)
	return float(H)

# print (approxEntropy(20,0.5))