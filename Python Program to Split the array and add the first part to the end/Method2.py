def SplitArray(a, n, k):
    b = a[:k]
    return (a[k::] + b[::])


if __name__=='__main__':
    arr = [12, 222, 33, 45, 67, 89]
    n = len(arr)
    position = int(input("Enter the position : "))
    
    arr =SplitArray(arr, n, position)
    
    for i in range(0, n):
        print(arr[i], end=" ")
