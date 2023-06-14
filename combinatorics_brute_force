import random

def create_combo():
    rests = ["A","A","A","B","B","B","C","C","C","D","D","D"]
    order = [""]*12
    while len(rests) > 0:
        r = rests.pop(0)
        while r != '':
            index = random.randint(0,11)
            if order[index] == "":
                order[index] = r
                r = ''
    return order



def main():
    all_the_combos = []
    fails_in_a_row = 0
    while fails_in_a_row < 100:
        new_order = create_combo()
        if new_order in all_the_combos:
            fails_in_a_row += 1
        else:
            all_the_combos.append(new_order)
            fails_in_a_row = 0
            print(len(all_the_combos))

if __name__ == "__main__":
    main()
