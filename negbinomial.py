import math

def prob(n, p, r):
	return float((math.factorial(n-1)/(math.factorial(r-1)*math.factorial(n-r)))*(p**r)*((1-p)**(n-r)))

def infoMeasure(n, p, r):
	tmp = prob(n, p, r)
	if tmp==0 or tmp==1:
		return float(0)
	else:
		return float(-math.log2(tmp))

def sumProb(N, p, r):
	'''
	large N -> sumProb --> 1
	'''
	s = 0
	for i in range(r,N+1):
		s += prob(i, p, r)
	return float(s)

def approxEntropy(N, p, r):
	'''
	H(X) = sum(p(x)*I(x))
	'''
	H = 0
	for i in range(r,N+1):
		H += prob(i,p,r)*infoMeasure(i,p,r)
	return float(H)

# print (approxEntropy(10,0.5,5))