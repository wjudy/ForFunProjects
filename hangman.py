from random_word import RandomWords
random_words = RandomWords()
the_word = random_words.get_random_word()
# Eventually the user won't see this printout
print(the_word)
print("WELCOME TO HANGMAN!!!!!!")
print("Your word has " + str(len(the_word)) + " letters.")
print("\n")
guessed_word = False
guessed_letters = []
while not guessed_word:
	guessed_word = True
	print_line = ""
	for let in the_word:
		if let in guessed_letters:
			print_line += let
		else:
			print_line += "_"
			guessed_word = False
	print("Your word:")
	print(print_line)
	print("\n")
	print("Already guessed: " + str(guessed_letters))
	guess = input("Choose a letter! ")
	guessed_letters.append(guess)