# k: the required item to be found in the iterable 'arr'
# first: Starting index
# last: Ending index

def Bsearch(k,arr,last,first=0):
    mid=(first+last)//2
    if first==last:
        return False
    elif arr[mid]==k:
        return True
    elif arr[mid]<k:
        return Bsearch(k,arr,last,mid+1)
    elif arr[mid]>k:
        return Bsearch(k,arr,mid,first)
