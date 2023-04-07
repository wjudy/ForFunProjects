import pandas as pd
from pprint import pprint

class Element:
	def __init__(self, name, symbol, atomicNumber, atomicMass):
		self.name = name
		self.symbol = symbol
		self.atomicNumber = atomicNumber
		self.atomicMass = atomicMass

class Elements:
	def __init__(self):
		self.list = []

	def __repr__(self):
		elements = self.list

		if len(elements) == 0:
			return "No Elements"

		# # To sort the list in place...
		# elements.sort(key=lambda x: x.atomic_number)

		# To return a new list, use the sorted() built-in function...
		sorted_elements = sorted(elements, key=lambda x: x.atomicNumber)
		statement = '\n'
		for eli in sorted_elements:
			statement += 'Element: ' + eli.name + \
			' | Symbol: ' + eli.symbol + \
			' | Atomic Number: ' + str(eli.atomicNumber) + \
			' | Atomic Mass: ' + str(eli.atomicMass) + " g\n\n"

		return statement

	def add(self, element):
		self.list.append(element)

def read_data(path):
	df = pd.read_csv(path)
	#attrs = df.columns
	elements = []	
	for ii in range(df.shape[0]):
		row = df.iloc[ii]
		elements.append(Element(row['Element'], row['Symbol'], row['AtomicNumber'], row['AtomicMass']))
	return elements

def main():
	ELEMENTOS = Elements()

	tablecsv = read_data("Periodic_Table_of_Elements.csv")
	for element in tablecsv:
		ELEMENTOS.add(element)

	print(ELEMENTOS)

	# all_elements = Elements()
	# oxygen = Element('Oxygen', 'O', 8, 15.999)
	# all_elements.add(oxygen)
	# carbon = Element('Carbon', 'C', 6, 12.001)
	# all_elements.add(carbon)

	# print(all_elements)

if __name__ == "__main__":
	main()