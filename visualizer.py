from mysorts import *

from numpy import random

from pygame.locals import ( #for tracking specific keypresses
    K_ESCAPE,
    KEYDOWN,
)

from pygame import time

#START LOGIC

#print the menu
sortType, arrSize = printMenu()

#start pygame
pygame.init()

#set the popup screen up
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

#fill the screen with white
screen.fill(background)

#the arary to be sorted
arr = [0] * arrSize

#fill the array with random numbers
for j in range(arrSize):
    arr[j] = random.randint(SCREEN_HEIGHT)

if arrSize == SMALL:
    interval = 80
elif arrSize == MEDIUM:
    interval = 50
elif arrSize == LARGE:
    interval = 20

#draw the array bars before it's sorted
drawBarArr(screen, arr, red, interval)

#perform selection sort
sort(arr, sortType)

#let the sorted array sit for some time
pygame.time.delay(100)

#clear and print the final sorted array
screen.fill(background)

#draw the whole array as bars after it's sorted
drawBarArr(screen, arr, green, 0)

#final view loop
displaying = True
    
#REMOVE THIS SECTION LATER
while displaying:
    for event in pygame.event.get():
        if event.type == KEYDOWN: #While the user hasn't quit out
            if event.key == K_ESCAPE:
                displaying = False

#quit pygame
pygame.quit()
