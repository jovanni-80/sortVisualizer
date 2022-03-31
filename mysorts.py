from printfuncs import *

def sort(arr, option):

    #get the screen once so recursive sorts don't have to call the
    #get_surface() function every pass
    screen = pygame.display.get_surface()

    if option == 1:
        quicksort(arr, 0, len(arr)-1, screen)
    elif option == 2:
        mergesort(arr, len(arr), screen)
    elif option == 3:
        bubblesort(arr)
    elif option == 4:
        selectionsort(arr)
    elif option == 5:
        insertionsort(arr)

# function to find the partition position
def partition(arr, low, high, screen):

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1

            (arr[i], arr[j]) = (arr[j], arr[i])
            drawSwap(screen, arr, j, i)
            pygame.time.delay(50)

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    drawSwap(screen, arr, i+1, high)
    pygame.time.delay(50)

    return i + 1

#quicksort function
def quicksort(arr, first, last, screen):
    #if arr parameter is an array list
    if isList(arr):

        #perform quicksort
        if first < last:

            #call this shit
            p = partition(arr, first, last, screen)
            quicksort(arr, first, p - 1, screen)
            quicksort(arr, p + 1, last, screen)

def mergesort(arr, size, screen):
    if isList(arr):
        if size > 1:
            #get floor value with //
            middle = size//2

            left = arr[:middle]

            right = arr[middle:]

            mergesort(left, len(left), screen);
            mergesort(right, len(right), screen);

            i = k = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i+=1
                else:
                    arr[k] = right[j]
                    j+=1
                k+=1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

def bubblesort(l):
    #check that parameter is an array list
    if isList(l):

        #get screen
        screen = pygame.display.get_surface()
        #get arr length
        end = len(l)

        #set interval based on size
        if end == SMALL:
            interval = 50
        elif end == MEDIUM:
            interval = 20
        elif end == LARGE:
            interval = 10

        #perform the bubblesort
        for i in range(end):
            for j in range(0, end-i-1):
                if l[j+1] < l[j]:
                    (l[j+1], l[j]) = (l[j], l[j+1])
                    drawSwap(screen, l, j+1, j)
                    pygame.time.delay(interval)

#fully functioning selection sort that prints each pass
def selectionsort(l):
    #check that parameter is an array list
    if isList(l):

        #get screen
        screen = pygame.display.get_surface()
        #get array length
        end = len(l)

        #get interval based on arr size
        if end == SMALL:
            interval = 100
        elif end == MEDIUM:
            interval = 50
        elif end == LARGE:
            interval = 20

        #perform selection sort
        for i in range(end):
            minimum = i
            #start step
            for j in range(i+1, end):
                if l[j] < l[minimum]:
                    minimum = j
            #put min at the front
            (l[i], l[minimum]) = (l[minimum], l[i])
            drawSwap(screen, l, minimum, i)

            #draw white bar where the switched bars go
            pygame.time.delay(interval)
            #end step

def insertionsort(arr):
    if isList(arr):
        #get size of array
        size = len(arr)

        #get interval based on arr size
        if size == SMALL:
            interval = 80
        elif size == MEDIUM:
            interval = 50
        elif size == LARGE:
            interval = 20

        screen = pygame.display.get_surface()
        #start the insertion sort
        for i in range(1, size):
            key = arr[i]
            j = i-1

            #while j hasn't gone past 0, and the key is less than the arr at j
            while j >= 0 and key < arr[j]:
                (arr[j+1], arr[j]) = (arr[j], arr[j+1])
                drawSwap(screen, arr, j+1,j)
                pygame.time.delay(interval)
                j = j-1

            #increment the key
            arr[j+1] = key
