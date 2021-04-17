import numpy as np

def insertionSortRecu(arr,start,end):
    arr=np.array(arr)
    def swap(i): #swap fucntion 
        arr[i-1]=arr[i]+arr[i-1]
        arr[i]=arr[i-1]-arr[i]
        arr[i-1]=arr[i-1]-arr[i]

    def in_sort(start,end): # Recursion Function
        if start>=end: # Base case
            return arr

        in_sort(start,end-1) # recursion
        #putting/inserting the last element to correct place
        j=end
        while arr[j]<arr[j-1] and j>start: 
            # untill less than previous element 
            # and greater than starting index
            swap(j)
            j=j-1

    in_sort(start,end)
    return arr