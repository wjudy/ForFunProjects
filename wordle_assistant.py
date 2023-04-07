# read in the fresh set of words, reset guess counter
def newgame():

	guesses = 0
	valid_words = open('wordle_dict.txt').read().split("\n")

	return valid_words, guesses


# take in the guess and the feedback, adjust our knowledge base accordingy
def updation(v, g, f, il, kl, kp, kap):

	print("IN UPDATION")
	print("# Valid Words remaining: " + str(len(v)))

	for i, fb in enumerate(f):
		if fb == "-":
			il.append(g[i])
		if fb == 'y':
			kap[i].append(g[i])
			kl.append(g[i])
		if fb == 'g':
			kl.append(g[i])
			kp[i] = g[i]
	v = list(set(v))
	il = list(set(il))
	kl = list(set(kl))

	for let in il:
		if let in kl:
			il.remove(let)

	print("INVALID LETTERS: " + str(il))
	print("KNOWN LETTERS: " + str(kl))
	print("KNOWN POSITIONS " + str(kp))
	print("KNOWN ANTI-POSITIONS " + str(kap))

	return trimmer(v, g, f, il, kl, kp, kap)

# uses our new knowledge base to trim down valid_words
def trimmer(v, g, f, il, kl, kp, kap):

	print("IN TRIMMER")
	print("# Valid Words remaining: " + str(len(v)))

	# First, remove words containing invalid letters
	if len(il) > 0:

		bad_words = []
		
		for word in v:
			for let in il:
				if let in word:
					bad_words.append(word)
					break
		
		for word in bad_words:
			v.remove(word)

	print("# Valid Words remaining: " + str(len(v)))


	# Second, remove words that don't have one of the known required letters
	if len(kl) > 0: 
		bad_words = []
		for word in v:
			for let in kl:
				if let not in word:
					bad_words.append(word)
					break
		
		for word in bad_words:
			v.remove(word)

	print("# Valid Words remaining: " + str(len(v)))

	# Third, remove words that have letters in bad spots
	bad_words = []
	for word in v:
		word_slots = [*word]
		for i, let in enumerate(kp):
			if let == "":
				continue
			if word_slots[i] != let:
				bad_words.append(word)

	bad_words = list(set(bad_words))

	for word in bad_words:
		v.remove(word)

	print("# Valid Words remaining: " + str(len(v)))

	# FOURTH, remove words that have letters in anti-positions
	bad_words = []
	for word in v:
		word_slots = [*word]
		for i, let in enumerate(kap):
			if len(kap[i]) == 0:
				continue
			for let in kap[i]:
				if word_slots[i] == let:
					bad_words.append(word)
	bad_words = list(set(bad_words))
	for word in bad_words:
		v.remove(word)

	print("# Valid Words remaining: " + str(len(v)))

	print("OPTIONS: \n")
	print(v)

	return v, il, kl, kp, kap


def main():

	kl = []
	il = []
	kp = ["","","","",""]
	kap = [[],[],[],[],[]]
	v, guesses = newgame()

	print("Oi! Let's get u a Wordle Win. \n")

	print("# of valid words remaining: " + str(len(v)))
	while guesses < 6:
		guess_string = input("Enter your guess: ")
		g = [*guess_string]
		print("Guess: " + str(g))

		f = input("Enter the feedback seperated by spaces: (-:blank, y:yellow, g:green) ").split(" ")
		print("Feedback: " + str(f))

		# UPDATE VALID_WORDS - FIRST GUESS
		v, il, kl, kp, kap = updation(v, g, f, il, kl, kp, kap)

	print("Ran out of tries... oof...")
	
if __name__ == "__main__":
	main()