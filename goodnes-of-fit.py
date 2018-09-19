x = [0,1,2,3] #classification of repetition
O = [32,15,9,4] #observed frequency
N = len(x)
sO = sum(O)
#######################################################################################
### Needed functions
def addtill5(l):
	lst = []
	#avoids changing the original list
	for i in l:
		lst.append(i)
	for i in range(len(l)):
		# print('\nOG list %s' %i)
		# print('+++++++++++++++++++++')
		for i in range(len(lst)):
			# print('new list %s' %i)
			# print('list value is %s' %lst[i])
			if (lst[i] < 5.) and (i == 0):
				lst[i] += lst[i+1]
				lst.pop(i+1)
				# print("%s" %lst)
				break
			elif (lst[i] < 5.) and (i < len(lst)-1) and (i != 0):
				#won't work if the adjacent values are identical
				#it seems to sum the former instead of the latter when both are equal.
				lst[i] += min(lst[i+1],lst[i-1])
				lst.pop(lst.index(min(lst[i+1],lst[i-1]))) 
				# print("%s" %lst)
				break
			elif (lst[i] < 5.) and (i == len(lst)-1):
				lst[i] += lst[i-1]
				lst.pop(i-1)
				# print("%s" %lst)
				# break
			# else:
			# 	print("%s" %lst)
		# 	print('-------------------')
		# print('+++++++++++++++++++++')
	return lst

def nCr(n,r):
	from math import factorial
	return factorial(n) // factorial(r) // factorial(n-r)
#I think its broken
def gamma(integer):
	#integer must be greater than 1
	from math import factorial
	return factorial(int(integer)-1)
#######################################################################################
### List of Probabilities
def poisson(x,O):
	from math import factorial
	from math import exp
	N = len(x)
	sO = sum(O)
	Xm = 0
	P = []
	for i in range(N):
		Xm += x[i] * O[i] / sO
	# print(Xm)
	for i in range(N-1):
		P.append(exp(-Xm)*Xm**i /factorial(i)) #this is the Poisson equation
	P.append(1-sum(P))
	return P

def binomial(x,n,p): #not verified
	#later verify all the definitions of n are correct with the theory
	P = []
	for i in range(N):
		P.append(nCr(n,x[i]) * (p**x[i]) * (1-p)**(n-x[i]))
	return P
#Unfinished
def normal(x,mu,s):
	from math import exp
	from math import sqrt
	from math import pi
	return exp(-1/2 * (((x-mu)/s))^2) / (s * sqrt(2 *pi))
#######################################################################################
switch = 'binomial'

if switch == 'poisson':
	P = poisson(x,O)
	p = 1
elif switch == 'binomial':
	P = binomial(x,N,0.5)
	p = 2
print('P %s' %P)
E = []
for i in range(N):
	E.append(P[i] *sO)
print('E %s' %E)


Efix = addtill5(E)
print("expected frequency combined %s" %Efix)


k = len(Efix)
v = k -p -1
if v < 1:
	v = 1

X2 = 0
for i in range(k):
	X2 += (O[i] - Efix[i])**2 /Efix[i]
print(X2) 


#TODO - dont know what x is or if this distribution is the correct one
def chisqrd(x,v):
	from math import exp
	if x > 0:
		return (x**(v/2 - 1) * exp(-x/2)) / (2**(v/2) * gamma(v/2))
	else:
		return 0
print(chisqrd(0.05,8))