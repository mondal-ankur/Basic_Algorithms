#Selection Sort

def SelectionSort(arr, start, end):
    arr=np.array(arr) #creating a new numpy array, for faster processing speed
    def swap(i,j): #swap fucntion in C language style
        if i!=j:
            arr[j]=arr[i]+arr[j]
            arr[i]=arr[j]-arr[i]
            arr[j]=arr[j]-arr[i]

    def sl_sort(start, end): #sort function
        #if starting position is greater or equal to the ebd position
        #i.e. array od size one
        # No calculation needed
        if start>=end-1: 
            return arr 

        # Now, obtaining the index of the min value
        m=start #say, start be the index for the mean initially
        for i in range(start,end):
            if arr[i]<arr[m]:
                m=i #updating index value of the min element
        swap(start,m) #swaping first and min element
        return sl_sort(start+1,end) #same process for the next index ***
    return sl_sort(start, end)


### Note: Here I have used nested function just to use the numpy array. 


### ***After first execution of sl_sort function,
# value in zero-th index is correctly placed, 
# so the minimum value of the array. 
# Now for the next index, i.e. for first index, 
# we have to call the same fucntion, 
# starting with the first index to the last index.