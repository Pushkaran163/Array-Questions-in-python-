# Python Program to Find remainder of array multiplication divided by n using Naive approach

def FindRemainder(arr, length, n):
    product = 1
    for i in range(length):
        product = product * arr[i]
    return product % n


arr = [100, 10, 5, 25, 35, 14]
length = len(arr)
n = int(input("Enter the value of n: "))
print("Remainder of array multiplication divided by n is: ", FindRemainder(arr, length, n))
