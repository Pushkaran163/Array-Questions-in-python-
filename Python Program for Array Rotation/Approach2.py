# Python Program for Array Rotation Using temp array

def RotateArray(arr, n, d):
    temp = []
    i = 0
    while(i < d):
        temp.append(arr[i])
        i += 1
    i = 0
    while(d<n):
        arr[i] = arr[d]
        i += 1
        d += 1
    arr[:] = arr[:i] + temp
    return arr


if __name__=='__main__':
   arr = [1, 2, 3, 4, 5, 6, 7, 8]
   print("Original array: ", arr)
   d = 2
   n = len(arr)
   
   print("Rotated array: ", RotateArray(arr, n, d))
     