"""
This is going to make NYT letterbox a BREEZE
By Will Judy
Feb 18th 2025
"""

class letter_box():

    def __init__(self):
        self.all_words = self.read_dict()
        self.a, self.b, self.c, self.d = self.get_letters()
        # self.a, self.b, self.c, self.d = ['x', 'g', 'r'], ['t','s','m'],['y','i','e'],['p','h','o']
        self.all_letters = []
        self.all_letters.extend(self.a)
        self.all_letters.extend(self.b)
        self.all_letters.extend(self.c)
        self.all_letters.extend(self.d)
        self.valid_letter_words = self.prune_words_bad_letters()
        self.valid_words = self.prune_words_bad_order()
        self.valid_words = sorted(self.valid_words, key=len, reverse=True)

        self.starts_with_dict = {}
        self.ends_with_dict = {}
        self.create_dicts()

        self.paths_len_1 = []
        self.get_paths_len_1()
        self.paths_len_1 = sorted(self.paths_len_1, key = len)

        if len(self.paths_len_1) == 0:
            print("No paths found with 1 word. Trying 2 word paths...")
        else:
            print("Found 1 word solution(s): ", self.paths_len_1)
            return

        self.paths_len_2 = []
        self.get_paths_len_2()

        self.paths_len_2 = sorted(self.paths_len_2, key=lambda sublist: max((len(s) for s in sublist)))

        if len(self.paths_len_2) == 0:
            print("No paths found with 2 words. Trying 3 word paths...")
        elif len(self.paths_len_2) < 10:
            print(f"Only found {len(self.paths_len_2)} 2 word solutions: ", self.paths_len_2)
            print("Trying for some 3 word solutions as well...")
        else:
            print(f"Found {len(self.paths_len_2)} 2 word solutions: ", self.paths_len_2)
            return

        self.paths_len_3 = []
        self.get_paths_len_3()

        if len(self.paths_len_3) == 0:
            print("No paths found with 3 words. 4 words will take too long...")
        else:
            print(f"Found {len(self.paths_len_3)} 3 word solutions: ", self.paths_len_3)
            return

    def read_dict(self):
        filename = 'dictionary.txt'
        all_words = []
        with open(filename, 'r') as file:
            # Read each line in the file
            for line in file:
                # Print each line
                line = line.strip()
                if len(line) <= 2:
                    continue
                all_words.append(line)
        return all_words

    def get_letters(self):
        side1_str = input("Enter the letters along the left side, with spaces in between: ")
        side1 = [let.strip().lower() for let in side1_str.split(" ")]

        side2_str = input("Enter the letters along the top side, with spaces in between: ")
        side2 = [let.strip().lower() for let in side2_str.split(" ")]

        side3_str = input("Enter the letters along the right side, with spaces in between: ")
        side3 = [let.strip().lower() for let in side3_str.split(" ")]

        side4_str = input("Enter the letters along the left side, with spaces in between: ")
        side4 = [let.strip().lower() for let in side4_str.split(" ")]

        return side1, side2, side3, side4

    def prune_words_bad_letters(self):
        words_with_bad_letters = []
        for word in self.all_words:
            for letter in word:
                if letter not in self.all_letters:
                    words_with_bad_letters.append(word)
                    break
        return list(set(self.all_words) - set(words_with_bad_letters))

    def prune_words_bad_order(self):
        words_with_bad_order = []
        for word in self.valid_letter_words:
            for i in range(len(word) - 1):
                letter = word[i]
                next_letter = word[i + 1]
                if letter in self.a:
                    if next_letter in self.a:
                        words_with_bad_order.append(word)
                        break
                if letter in self.b:
                    if next_letter in self.b:
                        words_with_bad_order.append(word)
                        break
                if letter in self.c:
                    if next_letter in self.c:
                        words_with_bad_order.append(word)
                        break
                if letter in self.d:
                    if next_letter in self.d:
                        words_with_bad_order.append(word)
                        break
        return list(set(self.valid_letter_words) - set(words_with_bad_order))

    def create_dicts(self):
        for word in self.valid_words:
            if word[0] not in self.starts_with_dict.keys():
                self.starts_with_dict[word[0]] = [word]
            else:
                self.starts_with_dict[word[0]].append(word)

            if word[-1] not in self.ends_with_dict.keys():
                self.ends_with_dict[word[-1]] = [word]
            else:
                self.ends_with_dict[word[-1]].append(word)

    def get_valid_next_words(self, word):
        next_words = self.starts_with_dict[word[-1]]
        if word in next_words:
            next_words.remove(word)
        return next_words


    def valid_word_chain_check(self, words):
        if len(words) == 0:
            return False
        letters_used = []
        for word in words:
            for letter in word:
                letters_used.append(letter)
            if len(set(letters_used)) == 12:
                return True
        return False


    def get_paths_len_1(self):
        for word in self.valid_words:
            word_chain = [word]
            if self.valid_word_chain_check(word_chain):
                self.paths_len_1.append(word_chain)

    def get_paths_len_2(self):
        for word in self.valid_words:
            next_words = self.get_valid_next_words(word)
            if not next_words:
                continue
            for word_2 in next_words:
                word_chain = [word, word_2]
                if self.valid_word_chain_check(word_chain):
                    self.paths_len_2.append(word_chain)

    def get_paths_len_3(self):
        for word in self.valid_words:
            next_words = self.get_valid_next_words(word)
            if not next_words:
                continue
            for word_2 in next_words:
                word_chain = [word, word]
                if self.valid_word_chain_check(word_chain):
                    self.paths_len_2.append(word_chain)
                next_words_2 = self.get_valid_next_words(word_2)
                if not next_words_2:
                    continue
                for word_3 in next_words_2:
                    word_chain = [word, word_2,word_3]
                    if len(self.paths_len_3) > 499:
                        return
                    if self.valid_word_chain_check(word_chain):
                        self.paths_len_3.append(word_chain)







def main():

    box = letter_box()

if __name__ == "__main__":
    main()
