import math
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def getZ(x, mu, sig, n=1):
	return (x - mu) / (sig / n**(1/2))

def normalDist(x, mu, sig):
	leftSide = 1 / (math.sqrt(sig*math.pi*(sig**2)))
	rightSide = math.exp(-(((x-mu)**2)/(2*(sig**2))))
	return leftSide * rightSide

def probZLessThanX(z):
	leftSide = 1 / math.sqrt(2*math.pi)
	def integrand(x):
		return math.exp(-((x**2)/2))
	integral = integrate.quad(integrand, -100, z)
	rightSide = integral[0]
	return leftSide * rightSide 

def getXVals(mu, sigma):
	lowEnd = mu - 4*sigma
	highEnd = mu + 4*sigma
	dif = highEnd - lowEnd
	interval = dif / 1000
	vals = [lowEnd + interval * i for i in range(1001)]
	return vals

mu = float(input("Enter the mean: "))
sigma = float(input("Enter the standard deviation: "))
Xvalue = float(input("Enter the value of the X in question: "))
N = int(input("Enter the Sample Size, n: ")) 
leftRight = input("Probability on left or right of X? (enter 'l' or 'r'): ")

Xvals = getXVals(mu, sigma)
plotDict = {}
for Xval in Xvals:
	plotDict[Xval] = normalDist(Xval, mu, sigma)
while leftRight != 'l' and leftRight != 'r':
	leftRight = input("Invalid, please choose 'l' or 'r': ")

Zvalue = getZ(Xvalue, mu, sigma, N)

goodPlotDict = {}
for Xval in Xvals:
	if leftRight == 'l':
		if Xval < Xvalue:
			goodPlotDict[Xval] = normalDist(Xval, mu, sigma)
	else:
		if Xval > Xvalue:
			goodPlotDict[Xval] = normalDist(Xval, mu, sigma)

probZ = probZLessThanX(Zvalue)
if leftRight == 'r':
	probZ = 1 - probZ

print("X VALUE: " + str(Xvalue))
print("Calculated Z value: " + str(Zvalue))
print("Predicted probability: " + str(probZ))

plt.bar(plotDict.keys(), plotDict.values())
plt.bar(goodPlotDict.keys(), goodPlotDict.values(), color='red')
plt.show()

