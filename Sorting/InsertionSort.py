import numpy as np

def insertionSort(arr,start,end):
    arr=np.array(arr)
    def swap(i): #swap fucntion 
        arr[i-1]=arr[i]+arr[i-1]
        arr[i]=arr[i-1]-arr[i]
        arr[i-1]=arr[i-1]-arr[i]

    for i in range(start+1,end): #primary loop
        j=i #subindex
        while arr[j]<arr[j-1] and j>start: 
            # untill less than previous element 
            # and greater than starting index
            swap(j)
            j=j-1
    return arr
