#Linear Search Code
def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10
print("Element found at index "+str(linearSearch(arr,x)))
