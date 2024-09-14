# Using slicing and extend() methods

arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = int(input("enter the position : "))
x = arr[:position]
y = arr[position:]
y.extend(x)
for i in y:
	print(i, end=" ")
