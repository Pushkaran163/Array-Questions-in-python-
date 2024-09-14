# Using list comprehension and modulo

def SplitAndAdd(arr, n):
    return [arr[(i + n) % len(arr)] for i in range(len(arr))]


if __name__=='__main__':
    arr = [12, 222, 33, 45, 67, 89]
    position = int(input("enter the position : "))
    
    result = SplitAndAdd(arr, position)
    
    print(*result)