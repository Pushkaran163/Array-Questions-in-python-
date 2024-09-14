# Python Program to Find Largest Element in an Array

# Find largest element in an array Using operator.gt()

import operator 

arr = [22, 89, 76, 100, 23, 67, 299, 99, 89, 76]

max = 0

print("The given array is :", arr)

for i in arr:
    if operator.gt(i, max):
        max = i
        
print("Largest element in the array is :", max)