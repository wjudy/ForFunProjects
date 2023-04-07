import pygame
import random

idx_to_name = {1:'da', 2:'d2', 3:'d3',4:'d4', 5:'d5', 6:'d6', 7:'d7', 8:'d8', 9:'d9', 10:'d10', 11:'dj', 12:'dq', 13:'dk',
    14:'ca', 15:'c2', 16:'c3', 17:'c4', 18:'c5', 19:'c6', 20:'c7', 21:'c8', 22:'c9', 23:'c10', 24:'cj', 25:'cq', 26:'ak',
    27:'ha', 28:'h2', 29:'h3', 30:'h4', 31:'h5', 32:'h6', 33:'h7', 34:'h8', 35:'h9', 36:'h10', 37:'hj', 38:'hq', 39:'hk',
    40:'sa', 41:'s2', 42:'s3', 43:'s4', 44:'s5', 45:'s6', 46:'s7', 47:'s8', 48:'s9', 49:'s10', 50:'sj', 51:'sq', 52:'sk'}

winning_piles = {'d':[], 'c':[], 'h':[],'s':[]}

current_piles = {i:[] for i in range(1,8)}

def shuffle():
    cards = []
    while len(cards) < 52:
        card = random.randint(1,53)
        if card not in cards:
            cards.append(card)
    return cards

def place_cards(cards):
    for i in range(1,8):
        current_piles[i].append(cards[:i])
        cards = cards[i:]

def get_visible_cards():
    we_can_see = []
    for i in range(1,8):
        idx = current_piles[i][0][-1]
        we_can_see.append(idx_to_name[idx])
    return we_can_see


def display():
    print(get_visible_cards())

def card_is_black(str):
    if 's' in str or 'c' in str:
        return True
    else:
        return False
    
# def get_moves():
    

def main():

    deck = shuffle()
    # print(deck)
    # print(current_piles)
    place_cards(deck)
    print(current_piles)
    display()
    

    # screen = pygame.display.set_mode((1000, 500))
    # pygame.display.set_caption('Solitaire for Sluts')
    # screen.fill((235, 163, 240))
    # pygame.display.flip()

    # # deck = shuffle()
    # # print(deck)
    # # print(current_piles)
    # # place_cards(deck)
    # # print(current_piles)

    # surface1 = pygame.Surface((100,100))
    # # surface2 = pygame.Surface((100, 100), flags=0, depth=2, masks=None)


    # pygame.draw.rect(surface1, (100,100,100,100))   

    # running = True
    # while running:
        
    # # for loop through the event queue  
    #     for event in pygame.event.get():
        
    #         # Check for QUIT event      
    #         if event.type == pygame.QUIT:
    #             running = False

if __name__ == "__main__":
    main()