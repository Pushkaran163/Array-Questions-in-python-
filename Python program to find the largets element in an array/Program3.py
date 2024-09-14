# Python Program to Find Largest Element in an Array

# Find largest element in an array Using sort() function

def Largest(arr, n):
    
    arr.sort()
    
    return arr[n - 1]


if __name__=='__main__':
    arr = [23, 45, 78, 11, 24, 99, 7, 56, 89]
    
    n = len(arr)
    
    print("Largest element in ", arr, "is :", Largest(arr, n))