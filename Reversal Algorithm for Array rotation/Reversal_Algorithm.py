def reverseArray(arr, start, end):
    while(start<end):
        temp =arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
        
def leftRotate(arr, d):
    n =len(arr)
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
    
def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=" ")
        
if __name__=='__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    d = int(input("enter the value : "))
    leftRotate(arr, d)
    printArray(arr)
    