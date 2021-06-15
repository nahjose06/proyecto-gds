def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binarySearch (arr, l, r, x):
    if r >= l: 
        mid = l + (r - l) // 2
 
        if arr[mid] == x:
            return mid
         
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:
        return -1
