def mergesort(arr, firstIdx, lastIdx):

    #call mergesort on left, and right of array, then merge them
    if (lastIdx > firstIdx):

        #get the middle index
        midIdx = int((lastIdx-firstIdx)/2 + firstIdx)

        #call mergesort on left and right sub arrays
        mergesort(arr, firstIdx, midIdx)
        mergesort(arr, midIdx+1, lastIdx)

        #merge the subarrays
        merge(arr, firstIdx, midIdx, lastIdx)
        print(arr)

def merge(arr, firstIdx, midIdx, lastIdx):

    startIdx = midIdx+1

    #if arr at midindex is larger, perform the sorting step of merge
    if (arr[midIdx] > arr[startIdx]):

        #wile first index is on its side and start index is within bounds
        while (firstIdx <= midIdx and startIdx <= lastIdx):

            #dont swap if element from first half is in place
            if (arr[firstIdx] <= arr[startIdx]):
                firstIdx+=1
            else:
                value = arr[startIdx]
                idx = startIdx

                while (idx != firstIdx):
                    #draw Swap would go here
                    print(arr[idx], arr[idx-1])
                    arr[idx] = arr[idx-1]
                    idx-=1

                #draw swap would also go here
                #print(arr[firstIdx], value)
                arr[firstIdx] = value

                #update the pointers
                firstIdx+=1
                midIdx+=1
                startIdx+=1


array = [5,3,4,6,7,1,9,7,6,5]
print(array)

#call mergesort with correct parameters
mergesort(array, 0, len(array)-1)

print(array)

exit(0)
