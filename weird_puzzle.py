class whole():
	def __init__(self):
		self.moves_on = {}
		self.moves_off = {}
		self.all = [unit(x + 1) for x in range(9)]

	def game_is_complete(self):
		for unit in self.all:
			if unit.status == 'on':
				return False
		return True

	def status_report(self):
		current = []
		for ring in self.all:
			current.append(ring.get_status())
		print(current)
		

	def update_moves(self):
		for ii in range(self.all):
			if self.all[ii].status == 'on':
				if ii == 0:
					self.moves_off[ii] = True
				if ii 
			if ii == 1:





class unit():

	def __init__(self, position):
		self.pos = position
		self.status = "on"

	def get_status(self):
		return self.status

	def change_status(self):
		if self.status == 'on':
			self.status = 'off'
		else:
			self.status = 'on'


def main():

	thePuzzle = whole()
	while not thePuzzle.game_is_complete():


if __name__ == "__main__":
	main()
