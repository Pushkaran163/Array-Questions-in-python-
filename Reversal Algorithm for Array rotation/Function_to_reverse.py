def reverseArray(arr, d):
    c = (arr[d:]) + (arr[:d])
    return c


if __name__=='__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    d = int(input("enter the value : "))
    print(reverseArray(arr, d))
    