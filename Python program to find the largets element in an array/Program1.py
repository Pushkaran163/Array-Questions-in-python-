# Python Program to Find Largest Element in an Array

def Largest(arr, max):
    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
            
    return max

if __name__=='__main__':
    arr = [10, 22, 44, 58, 1, 3, 99, 4, 77]
    
    max = arr[0]
    
    print("Largest element i the array is :", Largest(arr, max))