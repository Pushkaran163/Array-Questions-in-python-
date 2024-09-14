# Python Program to Find Sum of Array

def Sum(arr):
    
    Sum = 0
    
    for i in arr:
        Sum += i
    
    return Sum


if __name__=='__main__':
    
    arr = [1, 2, 3, 4, 5, 6]
    
    print("Summ of the array", arr, "is:", Sum(arr))