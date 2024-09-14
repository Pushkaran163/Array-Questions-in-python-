# Partitioning the sub arrays and reversing them

def Reverse(start, end, arr):
    
    number_of_reverse = end - start + 1
    
    count = 0
    
    while(number_of_reverse//2 != count):
        arr[start + count], arr[end - count] = arr[end - count], arr[start + count]
        count += 1
    return arr

def left_rotate(arr, size, d):
    start = 0
    end = size - 1
    arr = Reverse(start, end, arr)
    
    start = size - d
    end = size - 1
    arr = Reverse(start, end, arr)
    
    return arr


if __name__=='__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    d = 1
    size = len(arr)
    print('Original array:', arr)
    
    if(d <= size):
        print('Rotated array: ', left_rotate(arr, size, d))
    else:
        d = d % size
        print('Rotated array: ', left_rotate(arr, size, d))