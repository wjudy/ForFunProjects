import pygame
import time


pygame.mixer.init()
pygame.init()
pygame.mixer.music.set_volume(0.7)
window = pygame.display.set_mode((1000, 600))

#All sounds first octave
c1Sound = pygame.mixer.Sound('loC.mp3')
c1sharpSound = pygame.mixer.Sound('loCsharp.mp3')
d1Sound = pygame.mixer.Sound('loD.mp3')
d1sharpSound = pygame.mixer.Sound('loDsharp.mp3')
e1Sound = pygame.mixer.Sound('loE.mp3')
f1Sound = pygame.mixer.Sound('loF.mp3')
f1sharpSound = pygame.mixer.Sound('loFsharp.mp3')
g1Sound = pygame.mixer.Sound('loG.mp3')
g1sharpSound = pygame.mixer.Sound('loGsharp.mp3')
a1Sound = pygame.mixer.Sound('loA.mp3')
a1sharpSound = pygame.mixer.Sound('loAsharp.mp3')
b1Sound = pygame.mixer.Sound('loB.mp3')

#second ocatave and high c
midcSound = pygame.mixer.Sound('C.mp3')
csharpSound = pygame.mixer.Sound('Csharp.mp3')
dSound = pygame.mixer.Sound('D.mp3')
dsharpSound = pygame.mixer.Sound('Dsharp.mp3')
eSound = pygame.mixer.Sound('E.mp3')
fSound = pygame.mixer.Sound('F.mp3')
fsharpSound = pygame.mixer.Sound('Fsharp.mp3')
gSound = pygame.mixer.Sound('G.mp3')
gsharpSound = pygame.mixer.Sound('Gsharp.mp3')
aSound = pygame.mixer.Sound('A.mp3')
asharpSound = pygame.mixer.Sound('Asharp.mp3')
bSound = pygame.mixer.Sound('B.mp3')
c3Sound = pygame.mixer.Sound('hiC.mp3')

#key colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

#low octave
c1minx = 0
c1miny = 300
c1maxx = 25
c1maxy = 600

c1sharpminx = 25
c1sharpminy = 200
c1sharpmaxx = 75/2
c1sharpmaxy = 500

d1minx = 75/2
d1miny = 300
d1maxx = 125/2
d1maxy = 600

d1sharpminx = 125/2
d1sharpminy = 200
d1sharpmaxx = 150/2
d1sharpmaxy = 500

e1minx = 150/2
e1miny = 300
e1maxx = 200/2
e1maxy = 600

f1minx = 200/2
f1miny = 300
f1maxx = 250/2
f1maxy = 600

f1sharpminx = 250/2
f1sharpminy = 200
f1sharpmaxx = 275/2
f1sharpmaxy = 500

g1minx = 275/2
g1miny = 300
g1maxx = 325/2
g1maxy = 600

g1sharpminx = 325/2
g1sharpminy = 200
g1sharpmaxx = 350/2
g1sharpmaxy = 500

a1minx = 350/2
a1miny = 300
a1maxx = 400/2
a1maxy = 600

a1sharpminx = 400/2
a1sharpminy = 200
a1sharpmaxx = 425/2
a1sharpmaxy = 500

b1minx = 425/2
b1miny = 300
b1maxx = 475/2
b1maxy = 600

#mid C
midcminx = 475/2
midcminy = 300
midcmaxx = 525/2
midcmaxy = 600

csharpminx = 525/2
csharpminy = 200
csharpmaxx = 550/2
csharpmaxy = 500

dminx = 550/2
dminy = 300
dmaxx = 600/2
dmaxy = 600

dsharpminx = 600/2
dsharpminy = 200
dsharpmaxx = 625/2
dsharpmaxy = 500

eminx = 625/2
eminy = 300
emaxx = 675/2
emaxy = 600

fminx = 675/2
fminy = 300
fmaxx = 725/2
fmaxy = 600

fsharpminx = 725/2
fsharpminy = 200
fsharpmaxx = 750/2
fsharpmaxy = 500

gminx = 750/2
gminy = 300
gmaxx = 800/2
gmaxy = 600

gsharpminx = 800/2
gsharpminy = 200
gsharpmaxx = 825/2
gsharpmaxy = 500

aminx = 825/2
aminy = 300
amaxx = 875/2
amaxy = 600

asharpminx = 875/2
asharpminy = 200
asharpmaxx = 900/2
asharpmaxy = 500

bminx = 900/2
bminy = 300
bmaxx = 950/2
bmaxy = 600

#high C
c3minx = 950/2
c3miny = 300
c3maxx = 1000/2
c3maxy = 600
#DRAWING ALL THE NOTES

#draw c1, key name, press name
pygame.draw.rect(window, white, (0,300,50/2,300),5)
    #draw c
pygame.draw.line(window, white, (10,525), (40,525),2)
pygame.draw.line(window, white, (10,525), (10,550),2)
pygame.draw.line(window, white, (10,550), (40,550),2)
    #draw z
pygame.draw.line(window, red, (10,520), (40,520),2)
pygame.draw.line(window, red, (10,520), (40,495),2)
pygame.draw.line(window, red, (10,495), (40,495),2)
#draw d1
pygame.draw.rect(window, white, (75,300,50,300),5)
    #draw d
pygame.draw.line(window, white, (85,525), (115,537.5),2)
pygame.draw.line(window, white, (85,525), (85,550),2)
pygame.draw.line(window, white, (85,550), (115,537.5),2)
    #draw x
pygame.draw.line(window, red, (85,495), (115,520),2)
pygame.draw.line(window, red, (85,520), (115,495),2)
pygame.draw.line(window, red, (10,495), (40,495),2)
#draw e1
pygame.draw.rect(window, white, (150,300,50,300),5)
    #draw e
pygame.draw.line(window, white, (160,550), (190,550),2)
pygame.draw.line(window, white, (160,525), (160,550),2)
pygame.draw.line(window, white, (160,525), (190,525),2)
pygame.draw.line(window, white, (160,537.5), (175,537.5),2)
    #draw C
pygame.draw.line(window, red, (160,520), (190,520),2)
pygame.draw.line(window, red, (160,495), (160,520),2)
pygame.draw.line(window, red, (160,495), (190,495),2)
#draw f1
pygame.draw.rect(window, white, (200,300,50,300),5)
    #draw f
pygame.draw.line(window, white, (210,525), (240,525),2)
pygame.draw.line(window, white, (210,525), (210,550),2)
pygame.draw.line(window, white, (210,537.5), (225,537.5),2)
    #draw v
pygame.draw.line(window, red, (210,495), (225,520),2)
pygame.draw.line(window, red, (225,520), (240,495),2)
#draw g1
pygame.draw.rect(window, white, (275,300,50,300),5)
    #draw g
pygame.draw.line(window, white, (285,525), (315,525),2)
pygame.draw.line(window, white, (285,550), (315,550),2)
pygame.draw.line(window, white, (285,525), (285,550),2)
pygame.draw.line(window, white, (315,537.5), (315,550),2)
    #draw b
pygame.draw.line(window, red, (285,520), (315,520),2)
pygame.draw.line(window, red, (285,495), (285,520),2)
pygame.draw.line(window, red, (315,520), (315,507.5),2)
pygame.draw.line(window, red, (285,507.5), (315,507.5),2)
#draw a1
pygame.draw.rect(window, white, (350,300,50,300),5)
    #draw a
pygame.draw.line(window, white, (375,525), (355,550),2)
pygame.draw.line(window, white, (375,525), (395,550),2)
pygame.draw.line(window, white, (370,537.5), (380,537.5),2)
    #draw n
pygame.draw.line(window, red, (360,495), (360,520),2)
pygame.draw.line(window, red, (360,495), (390,520),2)
pygame.draw.line(window, red, (390,520), (390,495),2)
#draw b1
pygame.draw.rect(window, white, (425,300,50,300),5)
    #draw b
pygame.draw.line(window, white, (435,550), (465,550),2)
pygame.draw.line(window, white, (435,550), (435,525),2)
pygame.draw.line(window, white, (435,537.5), (465,537.5),2)
pygame.draw.line(window, white, (465,550), (465,537.5),2)
    #draw m
pygame.draw.line(window, red, (435,495), (435,520),2)
pygame.draw.line(window, red, (435,495), (450,520),2)
pygame.draw.line(window, red, (450,520), (465,495),2)
pygame.draw.line(window, red, (465,495), (465,520),2)
#draw c1 sharp
pygame.draw.rect(window, blue, (50,200,25,300),5)
    #draw s
pygame.draw.line(window, red, (50,125), (75,125),2)
pygame.draw.line(window, red, (50,125), (50,150),2)
pygame.draw.line(window, red, (50,150), (75,150),2)
pygame.draw.line(window, red, (75,150), (75,175),2)
pygame.draw.line(window, red, (75,175), (50,175),2)
#draw d1 sharp
pygame.draw.rect(window, blue, (125,200,25,300),5)
    #draw D
pygame.draw.line(window, red, (125,125), (150,150),2)
pygame.draw.line(window, red, (125,175), (150,150),2)
pygame.draw.line(window, red, (125,125), (125,175),2)
#draw f1 sharp
pygame.draw.rect(window, blue, (250,200,25,300),5)
    #draw g
pygame.draw.line(window, red, (250,125), (275,125),2)
pygame.draw.line(window, red, (250,175), (250,125),2)
pygame.draw.line(window, red, (250,175), (275,175),2)
pygame.draw.line(window, red, (275,150), (275,175),2)
#draw g1 sharp
pygame.draw.rect(window, blue, (325,200,25,300),5)
    #draw h
pygame.draw.line(window, red, (325,125), (325,175),2)
pygame.draw.line(window, red, (325,150), (350,150),2)
pygame.draw.line(window, red, (350,125), (350,175),2)
#draw a1 sharp
pygame.draw.rect(window, blue, (400,200,25,300),5)
    #draw J
pygame.draw.line(window, red, (425,125), (425,175),2)
pygame.draw.line(window, red, (425,175), (400,175),2)
pygame.draw.line(window, red, (400,175), (400,155),2)
    #draw mid c
pygame.draw.line(window, white, (485,530), (515,530),2)
pygame.draw.line(window, white, (485,530), (485,555),2)
pygame.draw.line(window, white, (485,555), (515,555),2)
    #draw w
pygame.draw.line(window, red, (480,495), (490,520),2)
pygame.draw.line(window, red, (490,520), (498,505),2)
pygame.draw.line(window, red, (498,505), (508,520),2)
pygame.draw.line(window, red, (508,520), (514,495),2)
    #draw 3
pygame.draw.line(window, red, (520,125), (540,125),2)
pygame.draw.line(window, red, (540,125), (540,175),2)
pygame.draw.line(window, red, (525,150), (540,150),2)
pygame.draw.line(window, red, (520,175), (540,175),2)
    #draw d
pygame.draw.line(window, white, (560,530), (585,545),2)
pygame.draw.line(window, white, (585,545), (560,560),2)
pygame.draw.line(window, white, (560,560), (560,530),2)
    #draw e
pygame.draw.line(window, red, (560,495), (585,495),2)
pygame.draw.line(window, red, (560,525), (560,495),2)
pygame.draw.line(window, red, (560,510), (575,510),2)
pygame.draw.line(window, red, (560,525), (585,525),2)
    #draw 4
pygame.draw.line(window, red, (600,125), (600,150),2)
pygame.draw.line(window, red, (600,150), (625,150),2)
pygame.draw.line(window, red, (625,125), (625,175),2)
    # draw e
pygame.draw.line(window, white, (635,535), (660,535),2)
pygame.draw.line(window, white, (635,535), (635,560),2)
pygame.draw.line(window, white, (635,548.5), (650,548.5),2)
pygame.draw.line(window, white, (635,560), (660,560),2)
    #draw r
pygame.draw.line(window, red, (635,500), (635,525),2)
pygame.draw.line(window, red, (635,500), (655,500),2)
pygame.draw.line(window, red, (655,500), (655,510),2)
pygame.draw.line(window, red, (655,510), (635,510),2)
pygame.draw.line(window, red, (635,510), (655,525),2)
    #draw f
pygame.draw.line(window, white, (690,535), (715,535),2)
pygame.draw.line(window, white, (690,535), (690,565),2)
pygame.draw.line(window, white, (690,548.5), (705,548.5),2)
    #draw t
pygame.draw.line(window, red, (698.566,500), (698.5,525),2)
pygame.draw.line(window, red, (685,510), (710,510),2)
    #draw 6
pygame.draw.line(window, red, (725,125), (725,175),2)
pygame.draw.line(window, red, (725,175), (750,175),2)
pygame.draw.line(window, red, (750,175), (750,150),2)
pygame.draw.line(window, red, (750,150), (725,150),2)
    #draw g
pygame.draw.line(window, white, (760,535), (785,535),2)
pygame.draw.line(window, white, (760,535), (760,565),2)
pygame.draw.line(window, white, (760,565), (785,565),2)
pygame.draw.line(window, white, (785,555), (785,565),2)
pygame.draw.line(window, white, (785,555), (770,555),2)
    #draw y
pygame.draw.line(window, red, (775,510), (775,530),2)
pygame.draw.line(window, red, (760,500), (775,510),2)
pygame.draw.line(window, red, (785,500), (775,510),2)
    #draw 7
pygame.draw.line(window, red, (800,125), (825,125),2)
pygame.draw.line(window, red, (825,125), (800,175),2)
pygame.draw.line(window, red, (805,150), (820,150),2)
    #draw a
pygame.draw.line(window, white, (830,565), (850,535),2)
pygame.draw.line(window, white, (850,535), (870,565),2)
pygame.draw.line(window, white, (842,550), (857,550),2)
    #draw u
pygame.draw.line(window, red, (835,530), (860,530),2)
pygame.draw.line(window, red, (835,530), (835,500),2)
pygame.draw.line(window, red, (860,530), (860,500),2)
    #draw 8
pygame.draw.line(window, red, (880,125), (900,125),2)
pygame.draw.line(window, red, (880,125), (880,140),2)
pygame.draw.line(window, red, (880,140), (900,140),2)
pygame.draw.line(window, red, (900,140), (900,125),2)
pygame.draw.line(window, red, (890,140), (890,150),2)
pygame.draw.line(window, red, (880,150), (900,150),2)
pygame.draw.line(window, red, (880,150), (880,165),2)
pygame.draw.line(window, red, (880,165), (900,165),2)
pygame.draw.line(window, red, (900,165), (900,150),2)
    #draw b
pygame.draw.line(window, white, (915,535), (915,565),2)
pygame.draw.line(window, white, (915,565), (940,565),2)
pygame.draw.line(window, white, (940,565), (940,550),2)
pygame.draw.line(window, white, (940,550), (915,550),2)
    #draw i
pygame.draw.line(window, red, (925,505), (925,530),2)
pygame.draw.line(window, red, (925,495), (925,500),2)
    #draw c3
pygame.draw.line(window, white, (955,538), (970,538),2)
pygame.draw.line(window, white, (955,538), (955,562),2)
pygame.draw.line(window, white, (955,562), (970,562),2)
    #draw 3
pygame.draw.line(window, white, (980,535), (995,535),2)
pygame.draw.line(window, white, (995,535), (995,565),2)
pygame.draw.line(window, white, (995,565), (980,565),2)
pygame.draw.line(window, white, (980,550), (995,550),2)
    #draw o
pygame.draw.line(window, red, (965,505), (990,505),2)
pygame.draw.line(window, red, (965,505), (965,528),2)
pygame.draw.line(window, red, (965,528), (990,528),2)
pygame.draw.line(window, red, (990,528), (990,505),2)



#draw middle c
pygame.draw.rect(window, white, (475,300,50,300),5)
#draw d
pygame.draw.rect(window, white, (550,300,50,300),5)
#draw e
pygame.draw.rect(window, white, (625,300,50,300),5)
#draw f
pygame.draw.rect(window, white, (675,300,50,300),5)
#draw g
pygame.draw.rect(window, white, (750,300,50,300),5)
#draw a
pygame.draw.rect(window, white, (825,300,50,300),5)
#draw b
pygame.draw.rect(window, white, (900,300,50,300),5)
#draw c sharp
pygame.draw.rect(window, blue, (525,200,25,300),5)
#draw d sharp
pygame.draw.rect(window, blue, (600,200,25,300),5)
#draw f sharp
pygame.draw.rect(window, blue, (725,200,25,300),5)
#draw g sharp
pygame.draw.rect(window, blue, (800,200,25,300),5)
#draw a sharp
pygame.draw.rect(window, blue, (875,200,25,300),5)
#high c3
pygame.draw.rect(window, white, (950,300,50,300),5)

pygame.display.update()

while True:
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    for event in pygame.event.get():

#c1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                c1Sound.play()
                pygame.draw.rect(window, green, (0,300,50,300),5)
                pygame.display.update()
                print('c1')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (c1minx < x < c1maxx) and (c1miny < y < c1maxy):
            c1Sound.play()
            pygame.draw.rect(window, green, (0,300,50,300),5)
            pygame.display.update()
            print('c1')

#c1sharp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                c1sharpSound.play()
                pygame.draw.rect(window, green, (50,200,25,300),5)
                pygame.display.update()
                print('c1sharp')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (c1sharpminx < x < c1sharpmaxx) and (c1sharpminy < y < c1sharpmaxy):
            c1sharpSound.play()
            pygame.draw.rect(window, green, (50,200,25,300),5)
            pygame.display.update()
            print('c1sharp')

#d1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                d1Sound.play()
                pygame.draw.rect(window, green, (75,300,50,300),5)
                pygame.display.update()
                print('d1')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (d1minx < x < d1maxx) and (d1miny < y < d1maxy):
            d1Sound.play()
            pygame.draw.rect(window, green, (75,300,50,300),5)
            pygame.display.update()
            print('d1')

# d1sharp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                d1sharpSound.play()
                pygame.draw.rect(window, green, (125,200,25,300),5)
                pygame.display.update()
                print('d1sharp')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (d1sharpminx < x < d1sharpmaxx) and (d1sharpminy < y < d1sharpmaxy):
            d1sharpSound.play()
            pygame.draw.rect(window, green, (125,200,25,300),5)
            pygame.display.update()
            print('d1sharp')

# e1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                e1Sound.play()
                pygame.draw.rect(window, green, (150,300,50,300),5)
                pygame.display.update()
                print('e1')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (e1minx < x < e1maxx) and (e1miny < y < e1maxy):
            e1Sound.play()
            pygame.draw.rect(window, green, (150,300,50,300),5)
            pygame.display.update()
            print('e1')

# f1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                f1Sound.play()
                pygame.draw.rect(window, green, (200,300,50,300),5)
                pygame.display.update()
                print('f1')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (f1minx < x < f1maxx) and (f1miny < y < f1maxy):
            f1Sound.play()
            pygame.draw.rect(window, green, (200,300,50,300),5)
            pygame.display.update()
            print('f1')

# f1 sharp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                f1sharpSound.play()
                pygame.draw.rect(window, green, (250,200,25,300),5)
                pygame.display.update()
                print('f1sharp')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (f1sharpminx < x < f1sharpmaxx) and (f1sharpminy < y < f1sharpmaxy):
            f1sharpSound.play()
            pygame.draw.rect(window, green, (250,200,25,300),5)
            pygame.display.update()
            print('f1sharp')

# g1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                g1Sound.play()
                pygame.draw.rect(window, green, (275,300,50,300),5)
                pygame.display.update()
                print('g1')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (g1minx < x < g1maxx) and (g1miny < y < g1maxy):
            g1Sound.play()
            pygame.draw.rect(window, green, (275,300,50,300),5)
            pygame.display.update()
            print('g1')

# g1 sharp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                g1sharpSound.play()
                pygame.draw.rect(window, green, (325,200,25,300),5)
                pygame.display.update()
                print('g1sharp')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (g1sharpminx < x < g1sharpmaxx) and (g1sharpminy < y < g1sharpmaxy):
            g1sharpSound.play()
            pygame.draw.rect(window, green, (325,200,25,300),5)
            pygame.display.update()
            print('g1sharp')

# a1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                a1Sound.play()
                pygame.draw.rect(window, green, (350,300,50,300),5)
                pygame.display.update()
                print('a1')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (a1minx < x < a1maxx) and (a1miny < y < a1maxy):
            a1Sound.play()
            pygame.draw.rect(window, green, (350,300,50,300),5)
            pygame.display.update()
            print('a1')

# a1 sharp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                a1sharpSound.play()
                pygame.draw.rect(window, green, (400,200,25,300),5)
                pygame.display.update()
                print('a1sharp')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (a1sharpminx < x < a1sharpmaxx) and (a1sharpminy < y < a1sharpmaxy):
            a1sharpSound.play()
            pygame.draw.rect(window, green, (400,200,25,300),5)
            pygame.display.update()
            print('a1sharp')

# b1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                b1Sound.play()
                pygame.draw.rect(window, green, (425,300,50,300),5)
                pygame.display.update()
                print('b1')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (b1minx < x < b1maxx) and (b1miny < y < b1maxy):
            b1Sound.play()
            pygame.draw.rect(window, green, (425,300,50,300),5)
            pygame.display.update()
            print('b1')

#middle C
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                midcSound.play()
                pygame.draw.rect(window, green, (475,300,50,300),5)
                pygame.display.update()
                print('midc')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (midcminx < x < midcmaxx) and (midcminy < y < midcmaxy):
            midcSound.play()
            pygame.draw.rect(window, green, (475,300,50,300),5)
            pygame.display.update()
            print('midc')

# c sharp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                csharpSound.play()
                pygame.draw.rect(window, green, (525,200,25,300),5)
                pygame.display.update()
                print('csharp')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (csharpminx < x < csharpmaxx) and (csharpminy < y < csharpmaxy):
            csharpSound.play()
            pygame.draw.rect(window, green, (525,200,25,300),5)
            pygame.display.update()
            print('csharp')

# d
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                dSound.play()
                pygame.draw.rect(window, green, (550,300,50,300),5)
                pygame.display.update()
                print('d')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (dminx < x < dmaxx) and (dminy < y < dmaxy):
            dSound.play()
            pygame.draw.rect(window, green, (550,300,50,300),5)
            pygame.display.update()
            print('d')

# d sharp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_4:
                dsharpSound.play()
                pygame.draw.rect(window, green, (600,200,25,300),5)
                pygame.display.update()
                print('dsharp')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (dsharpminx < x < dsharpmaxx) and (dsharpminy < y < dsharpmaxy):
            dsharpSound.play()
            pygame.draw.rect(window, green, (600,200,25,300),5)
            pygame.display.update()
            print('dsharp')

# e
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                eSound.play()
                pygame.draw.rect(window, green, (625,300,50,300),5)
                pygame.display.update()
                print('e')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (eminx < x < emaxx) and (eminy < y < emaxy):
            eSound.play()
            pygame.draw.rect(window, green, (625,300,50,300),5)
            pygame.display.update()
            print('e')

# f
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                fSound.play()
                pygame.draw.rect(window, green, (675,300,50,300),5)
                pygame.display.update()
                print('f')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (fminx < x < fmaxx) and (fminy < y < fmaxy):
            fSound.play()
            pygame.draw.rect(window, green, (675,300,50,300),5)
            pygame.display.update()
            print('f')

# f sharp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_6:
                fsharpSound.play()
                pygame.draw.rect(window, green, (725,200,25,300),5)
                pygame.display.update()
                print('fsharp')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (fsharpminx < x < fsharpmaxx) and (fsharpminy < y < fsharpmaxy):
            fsharpSound.play()
            pygame.draw.rect(window, green, (725,200,25,300),5)
            pygame.display.update()
            print('fsharp')

# g
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                gSound.play()
                pygame.draw.rect(window, green, (750,300,50,300),5)
                pygame.display.update()
                print('g')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (gminx < x < gmaxx) and (gminy < y < gmaxy):
            gSound.play()
            pygame.draw.rect(window, green, (750,300,50,300),5)
            pygame.display.update()
            print('g')

# g sharp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_7:
                gsharpSound.play()
                pygame.draw.rect(window, green, (800,200,25,300),5)
                pygame.display.update()
                print('gsharp')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (gsharpminx < x < gsharpmaxx) and (gsharpminy < y < gsharpmaxy):
            gsharpSound.play()
            pygame.draw.rect(window, green, (800,200,25,300),5)
            pygame.display.update()
            print('gsharp')

# a
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                aSound.play()
                pygame.draw.rect(window, green, (825,300,50,300),5)
                pygame.display.update()
                print('a')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (aminx < x < amaxx) and (aminy < y < amaxy):
            aSound.play()
            pygame.draw.rect(window, green, (825,300,50,300),5)
            pygame.display.update()
            print('a')

# a sharp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_8:
                asharpSound.play()
                pygame.draw.rect(window, green, (875,200,25,300),5)
                pygame.display.update()
                print('asharp')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (asharpminx < x < asharpmaxx) and (asharpminy < y < asharpmaxy):
            asharpSound.play()
            pygame.draw.rect(window, green, (875,200,25,300),5)
            pygame.display.update()
            print('asharp')

# b
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                bSound.play()
                pygame.draw.rect(window, green, (900,300,50,300),5)
                pygame.display.update()
                print('b')


        if (event.type == pygame.MOUSEBUTTONDOWN) and (bminx < x < bmaxx) and (bminy < y < bmaxy):
            bSound.play()
            pygame.draw.rect(window, green, (900,300,50,300),5)
            pygame.display.update()
            print('b')

#c3
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                c3Sound.play()
                pygame.draw.rect(window, green, (950,300,50,300),5)
                pygame.display.update()
                print('c3')

        if (event.type == pygame.MOUSEBUTTONDOWN) and (c3minx < x < c3maxx) and (c3miny < y < c3maxy):
            c3Sound.play()
            pygame.draw.rect(window, green, (950,300,50,300),5)
            pygame.display.update()
            print('c3')

        if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYUP:
            pygame.mixer.fadeout(1000)
            pygame.draw.rect(window, white, (0,300,50,300),5) # c1
            pygame.draw.rect(window, white, (75,300,50,300),5) # d1
            pygame.draw.rect(window, white, (150,300,50,300),5) # e1
            pygame.draw.rect(window, white, (200,300,50,300),5) # f1
            pygame.draw.rect(window, white, (275,300,50,300),5) # g1
            pygame.draw.rect(window, white, (350,300,50,300),5) # a1
            pygame.draw.rect(window, white, (425,300,50,300),5) # b1
            pygame.draw.rect(window, blue, (50,200,25,300),5) # c1 sharp
            pygame.draw.rect(window, blue, (125,200,25,300),5) # d1 sharp
            pygame.draw.rect(window, blue, (250,200,25,300),5) # f1 sharp
            pygame.draw.rect(window, blue, (325,200,25,300),5) # g1 sharp
            pygame.draw.rect(window, blue, (400,200,25,300),5) # a1 sharp
            pygame.draw.rect(window, white, (475,300,50,300),5) # c
            pygame.draw.rect(window, white, (550,300,50,300),5) # d
            pygame.draw.rect(window, white, (625,300,50,300),5) # e
            pygame.draw.rect(window, white, (675,300,50,300),5) # f
            pygame.draw.rect(window, white, (750,300,50,300),5) # g
            pygame.draw.rect(window, white, (825,300,50,300),5) # a
            pygame.draw.rect(window, white, (900,300,50,300),5) # b
            pygame.draw.rect(window, blue, (525,200,25,300),5) # c sharp
            pygame.draw.rect(window, blue, (600,200,25,300),5) # d sharp
            pygame.draw.rect(window, blue, (725,200,25,300),5) # f sharp
            pygame.draw.rect(window, blue, (800,200,25,300),5) # g sharp
            pygame.draw.rect(window, blue, (875,200,25,300),5) # a sharp
            pygame.draw.rect(window, white, (950,300,50,300),5) # c3
            pygame.display.update()

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            pygame.display.update()
