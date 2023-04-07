
import matplotlib.pyplot as plt


def placeInStacks(placeDict):
	l = []
	c = []
	r = []
	for i in placeDict.keys():
		if i % 3 == 1:
			l.append(placeDict.get(i))
		elif i % 3 == 2:
			c.append(placeDict.get(i))
		else:
			r.append(placeDict.get(i))
	return l, c, r

def playTheGame(theNum, placeDict):
	previousLoc = ''
	positions = []
	
	while 'cc' not in previousLoc:
		l, c, r = placeInStacks(placeDict)
		newOrder = []
		valList = list(placeDict.values())
		if theNum in l:
			previousLoc = 'l'
			positions.append(valList.index(theNum) + 1)
			newOrder = c + l + r
		elif theNum in c:
			if previousLoc == 'c':
				previousLoc = 'cc'
			else:
				previousLoc = 'c'
			positions.append(valList.index(theNum) + 1)
			newOrder = l + c + r
		else:
			previousLoc = 'r'
			positions.append(valList.index(theNum) + 1)
			newOrder = l + r + c

		for i in range(1,22):
			placeDict[i] = newOrder[i-1]
	print(positions)
	return positions


# while True:

# 	cards = list(range(1,22))
# 	placeDict = {}

# 	# set up initial order
# 	for i in range(1,22):
# 		placeDict[i] = cards[i-1]

# 	theNum = int(input("Choose starting position (1 thru 21): "))
# 	playTheGame(theNum, placeDict)

stepsDict = {}
for num in range(1,22):
	cards = list(range(1,22))
	placeDict = {}

	for i in range(1,22):
		placeDict[i] = cards[i-1]
	stepsDict[num] = len(playTheGame(num, placeDict))

plt.bar(list(stepsDict.keys()), list(stepsDict.values()))
plt.show()

