import pygame
import time

pygame.mixer.init()
pygame.init()
pygame.mixer.music.set_volume(1)
window = pygame.display.set_mode((1800, 450))
pygame.display.set_caption('Guitar -> Piano Visualizer')

#### Maybe use this later for adding text to pygame screen #####
font = pygame.font.Font('freesansbold.ttf', 30)
eText = font.render('RED : E', True, (255,0,0), (127,0,0))
eTextRect = eText.get_rect()
eTextRect.center = (150, 425)
window.blit(eText, eTextRect)

aText = font.render('ORANGE : A', True, (255,165,0), (127,84,0))
aTextRect = aText.get_rect()
aTextRect.center = (450, 425)
window.blit(aText, aTextRect)

dText = font.render('YELLOW : D', True, (255,255,0), (127,127,0))
dTextRect = dText.get_rect()
dTextRect.center = (750, 425)
window.blit(dText, dTextRect)

gText = font.render('GREEN : G', True, (0,255,0), (0,127,0))
gTextRect = gText.get_rect()
gTextRect.center = (1050, 425)
window.blit(gText, gTextRect)

bText = font.render('BLUE : B', True, (0,0,255), (0,0,127))
bTextRect = bText.get_rect()
bTextRect.center = (1350, 425)
window.blit(bText, bTextRect)

EText = font.render('PURPLE : High E', True, (255,0,255), (127,0,127))
ETextRect = EText.get_rect()
ETextRect.center = (1650, 425)
window.blit(EText, ETextRect)


#key colors
white = (255,255,255)
black = (0,0,0)

#used for calculations
scottBases = [7, 0, 5, 10, 2, 7]
willBases = [0, 5, 10, 15, 19, 24]

#active colors
red = (255,0,0)
orange = (255,165,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
purple = (255,0,255)
# used for coloring keyboard
activeColors = [red, orange, yellow, green, blue, purple]

#passive colors
red2 = (255/2,0,0)
orange2 = (255/2,165/2,0)
yellow2 = (255/2,255/2,0)
green2 = (0,255/2,0)
blue2 = (0,0,255/2)
purple2 = (255/2,0,255/2)
#used for coloring keyboard
passiveColors = [red2, orange2, yellow2, green2, blue2, purple2]

class Key:
    individualKeys = []
    def __init__(self, sharp, num, xPos, yPos, width, height, pianoSound, guitarSound):
        self.__class__.individualKeys.append(self)
        self.self = self
        self.sh = sharp
        self.n = num
        self.x = xPos
        self.y = yPos
        self.w = width
        self.h = height
        self.ps = pianoSound
        self.gs = guitarSound


    def whiten(self):
        if self.sh == 1:
            pygame.draw.rect(window, white, (self.x, self.y, self.w, self.h), 5)
        else:
            pygame.draw.rect(window, white, (self.x, self.y, self.w, self.h), 0)


    def activate(self, colornum):
        pygame.draw.rect(window, activeColors[colornum], (self.x, self.y, self.w, self.h), 0)
    
    def makePassive(self, colornum):
        pygame.draw.rect(window, passiveColors[colornum], (self.x, 0, self.w, 50), 0)
        pygame.draw.rect(window, black, (self.x, self.y, self.w, self.h), 0)
        pygame.draw.rect(window, white, (self.x, self.y, self.w, self.h), 5)
        #pygame.draw.rect(window, passiveColors[colornum], (self.x, self.y, self.w, self.h), 0)

    def displayNumber(self):
        font = pygame.font.Font('freesansbold.ttf', 15)
        numText = font.render(str(self.n), True, (255,255,255), (0,0,0))
        numTextRect = numText.get_rect()
        if self.sh == 1:
            numTextRect.center = ((self.x + 12.5), 360)
        else: 
            numTextRect.center = (self.x + 25, 375)
        window.blit(numText, numTextRect)

    def playGuitarSound(self):
        pygame.mixer.Sound(self.gs).play()
        pygame.display.update()







### SET KEYS ###

e1 = Key(0,0,0,50,50,300,'e1.mp3','Ge1.mp3')
f1 = Key(0,1,50,50,50,300,'f1.mp3','Gf1.mp3')
fsharp1 = Key(1,2,100, 0,25,300,'fsharp1.mp3','Gfsharp1.mp3')
g1 = Key(0,3,125,50,50,300,'g1.mp3','Gg1.mp3')
gsharp1 = Key(1,4,175, 0,25,300,'gsharp1.mp3','Ggsharp1.mp3')
a1 = Key(0,5,200,50,50,300,'a1.mp3','Ga1.mp3')
asharp1 = Key(1,6,250, 0,25,300,'asharp1.mp3','Gasharp1.mp3')
b1 = Key(0,7,275,50,50,300,'b1.mp3','Gb1.mp3')
c1 = Key(0,8,325,50,50,300,'c1.mp3','Gc1.mp3')
csharp1 = Key(1,9,375, 0,25,300,'csharp1.mp3','Gcsharp1.mp3')
d1 = Key(0,10,400,50,50,300,'d1.mp3','Gd1.mp3')
dsharp1 = Key(1,11,450, 0,25,300,'dsharp1.mp3','Gdsharp1.mp3')
e2 = Key(0,12,475,50,50,300,'e2.mp3','Ge2.mp3')
f2 = Key(0,13,525,50,50,300,'f2.mp3','Gf2.mp3')
fsharp2 = Key(1,14,575, 0,25,300,'fsharp2.mp3','Gfsharp2.mp3')
g2 = Key(0,15,600,50,50,300,'g2.mp3','Gg2.mp3')
gsharp2 = Key(1,16,650, 0,25,300,'gsharp2.mp3','Ggsharp2.mp3')
a2 = Key(0,17,675,50,50,300,'a2.mp3','Ga2.mp3')
asharp2 = Key(1,18,725, 0,25,300,'asharp2.mp3','Gasharp2.mp3')
b2 = Key(0,19,750,50,50,300,'b2.mp3','Gb2.mp3')
c2 = Key(0,20,800,50,50,300,'c2.mp3','Gc2.mp3')
csharp2 = Key(1,21,850, 0,25,300,'csharp2.mp3','Gcsharp2.mp3')
d2 = Key(0,22,875,50,50,300,'d2.mp3','Gd2.mp3')
dsharp2 = Key(1,23,925, 0,25,300,'dsharp2.mp3','Gdsharp2.mp3')
e3 = Key(0,24,950,50,50,300,'e3.mp3','Ge3.mp3')
f3 = Key(0,25,1000,50,50,300,'f3.mp3','Gf3.mp3')
fsharp3 = Key(1,26,1050, 0,25,300,'fsharp3.mp3','Gfsharp3.mp3')
g3 = Key(0,27,1075,50,50,300,'g3.mp3','Gg3.mp3')
gsharp3 = Key(1,28,1125, 0,25,300,'gsharp3.mp3','Ggsharp3.mp3')
a3 = Key(0,29,1150,50,50,300,'a3.mp3','Ga3.mp3')
asharp3 = Key(1,30,1200, 0,25,300,'asharp3.mp3','Gasharp3.mp3')
b3 = Key(0,31,1225,50,50,300,'b3.mp3','Gb3.mp3')
c3 = Key(0,32,1275,50,50,300,'c3.mp3','Gc3.mp3')
csharp3 = Key(1,33,1325, 0,25,300,'csharp3.mp3','Gcsharp3.mp3')
d3 = Key(0,34,1350,50,50,300,'d3.mp3','Gd3.mp3')
dsharp3 = Key(1,35,1400, 0,25,300,'dsharp3.mp3','Gdsharp3.mp3')
e4 = Key(0,36,1425,50,50,300,'e4.mp3','Ge4.mp3')
f4 = Key(0,37,1475,50,50,300,'f4.mp3','Gf4.mp3')
fsharp4 = Key(1,38,1525, 0,25,300,'fsharp4.mp3','Gfsharp4.mp3')
g4 = Key(0,39,1550,50,50,300,'g4.mp3','Gg4.mp3')
gsharp4 = Key(1,40,1600, 0,25,300,'gsharp4.mp3','Ggsharp4.mp3')
a4 = Key(0,41,1625,50,50,300,'a4.mp3','Ga4.mp3')
asharp4 = Key(1,42,1675, 0,25,300,'asharp4.mp3','Gasharp4.mp3')
b4 = Key(0,43,1700,50,50,300,'b4.mp3','Gb4.mp3')
c4 = Key(0,44,1750,50,50,300,'c4.mp3','Gc4.mp3')


scottNotes = []
willNotes = []
totalNumberOfChords = 0

### RUN THIS TO ENTER FRETS AND SEE KEYS ###

def chooseNewChord():

    print("Hello!")
    stringOfFrets = input("For each string, say which fret is played, seperated by spaces (E A D G B E): ")
    print()
    frets = stringOfFrets.split()
    fretInts = map(int, frets)
    listFretInts = list(fretInts) #int list of fret nums
    
    for i in range(6):
        scottNotes.append(scottBases[i] + listFretInts[i])

    for i in range(6):
        if listFretInts[i] >= 0:
            willNotes.append(willBases[i] + listFretInts[i])
        else:
            willNotes.append(-1) 

def displayCurrentchord():
    j = -1
    for i in range(44):
        if (Key.individualKeys[i].n in willNotes) and (Key.individualKeys[i].n >= 0):
            j += 1
            Key.individualKeys[i].activate(j)
            pygame.mixer.Sound(Key.individualKeys[i].ps).play()
            pygame.display.update()
            time.sleep(0.3)
    time.sleep(3)

    for i in range(44):
        if (Key.individualKeys[i].n in willNotes) and (Key.individualKeys[i].n >= 0):
            pygame.mixer.Sound(Key.individualKeys[i].gs).play()
            pygame.display.update()
            time.sleep(0.1)




    #### Maybe use this later for adding text to pygame screen #####
    font = pygame.font.Font('freesansbold.ttf', 30)
    eText = font.render('RED : E - ' + str(scottNotes[0]), True, (255,0,0), (127,0,0))
    eTextRect = eText.get_rect()
    eTextRect.center = (150, 425)
    window.blit(eText, eTextRect)

    aText = font.render('ORANGE : A - ' + str(scottNotes[1]), True, (255,165,0), (127,84,0))
    aTextRect = aText.get_rect()
    aTextRect.center = (450, 425)
    window.blit(aText, aTextRect)

    dText = font.render('YELLOW : D - ' + str(scottNotes[2]), True, (255,255,0), (127,127,0))
    dTextRect = dText.get_rect()
    dTextRect.center = (750, 425)
    window.blit(dText, dTextRect)

    gText = font.render('GREEN : G - ' + str(scottNotes[3]), True, (0,255,0), (0,127,0))
    gTextRect = gText.get_rect()
    gTextRect.center = (1050, 425)
    window.blit(gText, gTextRect)

    bText = font.render('BLUE : B - ' + str(scottNotes[4]), True, (0,0,255), (0,0,127))
    bTextRect = bText.get_rect()
    bTextRect.center = (1350, 425)
    window.blit(bText, bTextRect)

    EText = font.render('PURPLE : High E - ' + str(scottNotes[5]), True, (255,0,255), (127,0,127))
    ETextRect = EText.get_rect()
    ETextRect.center = (1650, 425)
    window.blit(EText, ETextRect)
    pygame.display.update()


def displayPreviousChord(listKeys):
    j = -1
    for i in range(44):
        if Key.individualKeys[i].n in listKeys:
            j += 1
            Key.individualKeys[i].makePassive(j)
    pygame.display.update()
    print('previous wills notez' , listKeys)


##########################################
#            Makes Chord Class           #
##########################################

class Chord: 
    bank = []
    def __init__(self, listKeyInts):
        self.__class__.bank.append(self)
        self.noteList = listKeyInts
        self.e = listKeyInts[0]
        self.a = listKeyInts[1]
        self.d = listKeyInts[2]
        self.g = listKeyInts[3]
        self.b = listKeyInts[4]
        self.E = listKeyInts[5]

####################################
#### Initilize the White Piano #####
####################################

for i in range(45):
    Key.individualKeys[i].whiten()
    Key.individualKeys[i].displayNumber()
pygame.display.update()

def play():
    chooseNewChord()
    displayCurrentchord()
    yayNay = input("Start fresh? press 'e' to exit: ")

    if yayNay == 'e' :
        exit()
    else :
        print("u tried!")

play()  
