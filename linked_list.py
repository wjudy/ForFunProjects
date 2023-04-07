import pygame
import sys

class Node:
    def __init__(self, data):
        self.data = str(data)
        self.status = 1
        self.behind = None
        self.before = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        node = self.tail
        nodes = []
        stati = []

        while node is not None:
            nodes.append(str(node.data))
            stati.append(str(node.status))
            node = node.before

        line_one = " <-> ".join(nodes)
        line_two = " <-> ".join(stati)

        return "\n" + line_one + " \n" + line_two + " \n"

    def finished(self):
        node = self.head
        while node is not None:
            if node.status == 1:
                return False
            node = node.behind
        return True

def check_move(node):
    if node.data == "1":
        if node.status == 0:
            return "on"
        else:
            return "off"

    if node_is_last_on(node.before):
        if node.status == 0:
            return "on"
        else:
            return "off"
    else:
        return "no"


def node_is_last_on(node):
        if node.status == 0:
            return False
        nxt = node.before
        while nxt is not None:
            if nxt.status == 1:
                return False
            nxt = nxt.before
        return True
            
def Starting_Position():

    first_node = Node(1)
    second_node = Node(2)
    first_node.behind = second_node
    second_node.before = first_node

    third_node = Node(3)
    second_node.behind = third_node
    third_node.before = second_node

    fourth_node = Node(4)
    third_node.behind = fourth_node
    fourth_node.before = third_node

    fifth_node = Node(5)
    fourth_node.behind = fifth_node
    fifth_node.before = fourth_node

    sixth_node = Node(6)
    fifth_node.behind = sixth_node
    sixth_node.before = fifth_node

    seventh_node = Node(7)
    sixth_node.behind = seventh_node
    seventh_node. before = sixth_node

    eighth_node = Node(8)
    seventh_node.behind = eighth_node
    eighth_node.before = seventh_node

    ninth_node = Node(9)
    eighth_node.behind = ninth_node
    ninth_node.before = eighth_node

    return first_node

def main():


    ######### Initial Setup ##########
    
    llist = LinkedList()

    # create all rings and set to "on" position 
    llist.head = Starting_Position()

    # get tail too...
    node = llist.head
    while node.behind is not None:
        node = node.behind

    llist.tail = node
    print(llist)

    ######### Graphics Setup #########

    def move(link):
        # initializing the constructor
        pygame.init()
          
        # screen resolution
        res = (1100,500)
          
        # opens up a window
        screen = pygame.display.set_mode(res)

        # define colors
        color = (255,255,255)
        color_light = (170,170,170)
        color_dark = (100,100,100)
          
        # defining a font
        smallfont = pygame.font.SysFont('Corbel',35)

        # Set up variables
        positions = [900, 800, 700, 600, 500, 400, 300, 200, 100]
        
        texts = [smallfont.render('Ring ' + str(ii), True , color) for ii in range(1,10)]
    
        move_texts = [smallfont.render(status, True, color) for status in ['ON', 'OFF', 'Stuck']]

        # get possible moves
        moves = []
        node = link.head
        while node is not None:
            moves.append(check_move(node))
            node = node.behind
        print(moves)

        # color the screen green

        screen.fill((20,100,60))

        # establist first node,  "ring 1"
        node = link.head
        ii = 0
        positions_move_box_list = []
        numbers_move_box_list = []
        
        # DRAW EVERYTHING
        while node is not None:

            # RING LABEL
            screen.blit(texts[ii], (positions[ii], 400))

            # 'MOVE' BOX
            pygame.draw.rect(screen, color_dark, (positions[ii] + 5, 325, 90, 50))

            # 'MOVE' BOX MESSAGE
            if moves[ii] == 'off':
                screen.blit(move_texts[1], (positions[ii] + 25, 337.5))
                positions_move_box_list.append((positions[ii] + 5, 325, 90, 50))
                numbers_move_box_list.append(int(str(node)))
            elif moves[ii] == 'on':
                screen.blit(move_texts[0], (positions[ii] + 25, 337.5))
                positions_move_box_list.append((positions[ii] + 5, 325, 90, 50))
                numbers_move_box_list.append(int(str(node)))
            else:
                screen.blit(move_texts[2], (positions[ii] + 12.5, 337.5))

            #  RING
            if node.status == 1:
                pygame.draw.ellipse(screen, color_light, (positions[ii], 100 , 40, 100), 8)
            else:
                pygame.draw.ellipse(screen, color_dark, (positions[ii], 200 , 40, 100), 8)

            # ITERATE
            ii += 1
            node = node.behind
        
        # updates the frames of the game
        pygame.display.update()


        # GET USER INTERACTION
        chosen_ring = 0
        chosen_move = ""

        while chosen_ring == 0:
            
            ev = pygame.event.get()

            for event in ev:

                if event.type == pygame.QUIT:
                        pygame.quit()
                      
                #checks if a mouse is clicked
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        
                    mouse = pygame.mouse.get_pos()

                    for ii in range(len(positions_move_box_list)):
                        print("ii "+ str(ii))
                        quad = positions_move_box_list[ii]

                        if quad[0] <= mouse[0] <= quad[0] + quad[2] and quad[1] <= mouse[1] <= quad[1] + quad[3]:
                            print("Ring " + str(numbers_move_box_list[ii]) + ", move " + str(moves[numbers_move_box_list[ii] - 1]))
                            chosen_ring = numbers_move_box_list[ii]
                            print("Chosen_ring: " + str(chosen_ring))

                            print("Moves: " + str(moves))
                            chosen_move = str(moves[numbers_move_box_list[ii] - 1])
                            print("Chosen_move: " + str(chosen_move)
                                )

                    if chosen_ring != 0:
                        node = link.head
                        while chosen_ring > 1:
                            node = node.behind
                            chosen_ring -= 1

                        print(node)
                        if chosen_move == "off":
                            node.status = 0
                        else:
                            node.status = 1

                    if link.finished():
                        print("FINISHED?!")
                        return True
                    else:
                        return move(link)
        print(link)
        return move(link)


    YEAH_BABY = move(llist)

    
if __name__ == "__main__":
    main()