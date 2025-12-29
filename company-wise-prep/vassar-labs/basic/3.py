# Reverse an Array
# first approach 
# O(n), O(1)
def sol(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
arr = [1,2,3,4,5]
sol(arr)
print(arr)