import random

fourOrLess = 0
greaterThanFour = 0

manyTrials = int(input("How many trials? "))

for i in range(manyTrials):
	bigger = 0
	a = random.randint(1,6)
	b = random.randint(1,6)
	if (a > 4) or (b > 4):
		greaterThanFour += 1
	elif (a <= 4) and (b <= 4):
		fourOrLess += 1
print()
print("1, 2, 3, 4: " + str(fourOrLess))
print("Probability: " + str((fourOrLess / manyTrials)*100) + "%")
print()
print("5 or 6: " + str(greaterThanFour))
print("Probability: " + str((greaterThanFour / manyTrials)*100) + "%")
print()