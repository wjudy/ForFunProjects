from english_words import english_words_lower_alpha_set as dic

valid = {'t':['r','u','a','w','x','e','f','i','n'], 'q':['r','u','a','w','x','e','f','i','n'], 'y':['r','u','a','w','x','e','f','i','n'], 'r':['t','q','y','w','x','e','f','i','n'], 'u':['t','q','y','w','x','e','f','i','n'], 'a':['t','q','y','w','x','e','f','i','n'], 'w':['t','q','y','r','u','a','f','i','n'], 'x':['t','q','y','r','u','a','f','i','n'], 'e':['t','q','y','r','u','a','f','i','n'], 'f':['t','q','y','r','u','a','w','x','e'], 'i':['t','q','y','r','u','a','w','x','e'], 'n':['t','q','y','r','u','a','w','x','e']}

generated = []

def word_generator():
	recurseBoi('t')
	# for key in valid.keys():
	# 	recurseBoi(key)

def recurseBoi(word):
	print(word)
	if len(word) > 2 and word in dic:
		generated.append(word)
	if len(word) > 8:
		return
	next_lets = valid.get(word[-1])
	for let in next_lets:
		new = word + let
		recurseBoi(new)

word_generator()

print(generated)