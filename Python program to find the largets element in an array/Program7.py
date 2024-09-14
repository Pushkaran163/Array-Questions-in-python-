# Python Program to Find Largest Element in an Array

# Find Largest Element with Python Lambda

arr = [22, 89, 76, 100, 23, 67, 299, 99, 89, 76]

largest_element = max(arr, key=lambda x: x)

print("Largest element in the array is :", largest_element)