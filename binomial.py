import math

def prob(n, p, N):
	return float((math.factorial(N)/(math.factorial(n)*math.factorial(N-n)))*(p**n)*((1-p)**(N-n)))

def infoMeasure(n, p, N):
	tmp = prob(n, p, N)
	if tmp==0 or tmp==1:
		return float(0)
	else:
		return float(-math.log2(tmp))

def sumProb(N, p):
	'''
	large N -> sumProb == 1
	'''
	s = 0
	for i in range(1,N+1):
		s += prob(i,p,N)
	return float(s)

def approxEntropy(N, p):
	'''
	H(X) = sum(p(x)*I(x))
	'''
	H = 0
	for i in range(1,N+1):
		H += prob(i,p,N)*infoMeasure(i,p,N)
	return float(H)