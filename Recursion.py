def factorial(n):
	"""
	:type n: int
	:rtype: int
	"""
	if (n == 1 or n == 0):
		return 1
	elif (n > 1):
		return n * factorial(n-1)



def sum(n):
	"""
	:type n: int
	:rtype: int
	"""
	#Fill out,  Use recursion
	if n==1:
		return 1
	return sum(n-1)+n

def fibonacci(n):
	""":
	:type n: int
	:rtype: int
	"""
# Fill out,  Use recursion
	if n==0:
		return 0
	elif n==1:
		return 1
	else :
		return fibonacci(n-1)+fibonacci(n-2)

	
def combination(n, r):
	""":
	:type n: int
	:type r: int
	:rtype: int
	"""
# Fill out,  Use recursion
	if n==r or r==0: return 1
	return combination(n-1,r-1)+combination(n-1,r)

def TestRecursionFunction():
	print factorial(10)
	print sum(100)
	print combination(10,3)
	print fibonacci(10)

TestRecursionFunction()
