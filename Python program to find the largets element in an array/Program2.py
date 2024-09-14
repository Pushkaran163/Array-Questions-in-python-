# Python Program to Find Largest Element in an Array

# Find largest element in an array Using built-in function max()

def Largest(arr):
    ans = max(arr)
    return ans


if __name__=='__main__':
    arr = [22, 89, 76, 100, 23, 67, 299, 99, 89, 76]
    
    print("Largest element in the", arr ,"is :", Largest(arr))