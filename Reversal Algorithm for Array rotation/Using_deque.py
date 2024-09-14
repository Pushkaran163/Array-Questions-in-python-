from collections import deque

def ReverseArrayDeque(arr, d):
    n = len(arr)
    rotatedArray = deque(arr)
    rotatedArray.rotate(-d)
    return list(rotatedArray)


if __name__=='__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    d = int(input("enter the value : "))
    
    print("Original Array : ", arr)
    print("Rotated Array : ", ReverseArrayDeque(arr, d))