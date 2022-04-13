import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time

#visualizer popup screen dimensions must be divisible by 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#define array sizes based on screen size
SMALL = int(SCREEN_WIDTH/20)
MEDIUM = int(SCREEN_WIDTH/10)
LARGE = int(SCREEN_WIDTH/5)

#colors for pygame screen
background = (76, 86, 106)
foreground = (46, 52, 64)
red = (191, 97, 106)
green = (163, 190, 140)

#start function definitions
#check if a variable is an array list
def isList(l):
    return type(l) == list

#draw the whole bar array
def drawBarArr(screen, arr, color, interval):
    if isList(arr):

        size = len(arr)
        maxW, maxH = screen.get_width(), screen.get_height()
        barWidth = int(maxW)/size

        for j in range(size):
            i = arr[j]
            r = pygame.Rect(j*barWidth, maxH-i, barWidth, i)
            drawBar(screen, r, color)
            pygame.display.flip()
            pygame.time.delay(interval)

#erase and redraw two specific bars
def drawSwap(screen, arr, x, y):
    #get maximum screen dimensions
    maxW, maxH = screen.get_width(), screen.get_height()
    barWidth = int(maxW)/len(arr)

    #create bars as tall as can be that are blank
    r_min = pygame.Rect(x*barWidth, 0, barWidth, maxH)
    r_i = pygame.Rect(y*barWidth, 0, barWidth, maxH)

    #draw the blank bars
    drawBar(screen, r_min, background)
    drawBar(screen, r_i, background)

    #create the updated bars post swap
    r_min = pygame.Rect(x*barWidth, maxH-arr[x], barWidth, arr[x])
    r_i = pygame.Rect(y*barWidth, maxH-arr[y], barWidth, arr[y])

    #draw the updated bars
    drawBar(screen, r_min, foreground)
    drawBar(screen, r_i, foreground)

    #update the screen
    pygame.display.flip()


#draw a single bar
def drawBar(screen, r, color):
    pygame.draw.rect(screen, color, r)

#print the starting menu
def printMenu():

    validInput = False

    while validInput == False:
        #for input choice validation
        validInput = True

        #get input choice
        sortChoice = int(input('\nChoose type of sort\n1) Quick\n2) Merge\n3) Bubble\n4) Selection\n5) Insertion Sort\n'))

        #sort choice has to be 1-5
        if sortChoice < 1 or sortChoice > 5:
            validInput = False

        #process input for array size
        sizeChoice = int(input('\nChoose an array size\n1) Small\n2) Medium\n3) Large\n'))
        size = MEDIUM
        if sizeChoice == 1:
            size = SMALL
        elif sizeChoice == 2:
            size = MEDIUM
        elif sizeChoice == 3:
            size = LARGE
        else:
            validInput = False

        if validInput == False:
            print('\nPlease enter valid input')

    return sortChoice, size
