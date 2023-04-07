starting_state = [1, 1, 1, 1]

state = starting_state

def get_moves(state, index):
    if index == 0:
        if state[index] == 0:
            return "0on"
        else:
            return "0off"

    def node_is_last_on(state, index):
        if state[index] == 0:
            return False
        index -= 1
        while index >= 0:
            if state[index] == 1:
                return False
            index -= 1
        return True

    if node_is_last_on(state, index - 1):
        if state[index] == 0:
            return str(index)+"on"
        else:
            return str(index)+"off"

def unsolved(state):
	if 1 in state:
		return True
	else:
		return False

def mover(state, move):
	print(move)
	ring_key = move[0]
	ind = int(ring_key)
	move = move[1:]
	if move == 'on':
		state[ind] = 1
	else:
		state[ind] = 0
	return state

class Node:
	def __init__(self, state):
		self.state = state
		self.parent = None
		self.children = []

	def __repr__(self):
		return str(self.state)


class Tree:
	def __init__(self):
		self.root = None

	def __repr__(self):
		print_out = ""
		print_out += self.root
		return print_out


def play(state, current, discovered_states):

	while unsolved(state):
		moves = []
		for ii in range(len(state)):
			moves.append(get_moves(state, ii))

		if len(moves) == 0:
			print(discovered_states)
		
		for move in moves:
			if move == None:
				continue
			new_state = mover(state, move)
			if new_state in discovered_states:
				continue
			new_node = Node(new_state)
			current.children.append(new_node)
			new_node.parent = current
			discovered_states.append(new_state)
			play(new_state, new_node, discovered_states)

	print("solved?>?")


def setup(starting_state):
	tree_man = Tree()
	root_node = Node(starting_state)
	tree_man.root = root_node
	current = root_node
	discovered = []
	discovered.append(starting_state)
	play(starting_state, current, discovered)

	print(current)
	print(current.children)


setup(state)

