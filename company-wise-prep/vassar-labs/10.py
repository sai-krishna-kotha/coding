def reverse(arr, x, y):
    while x < y:
        arr[x], arr[y] = arr[y], arr[x]
        x += 1
        y -= 1
def left_k_rotations(arr: list, k: int):
    reverse(arr, 0, k-1)
    reverse(arr, k, len(arr)-1)
    reverse(arr, 0, len(arr)-1)
    return arr
def right_k_rotations(arr: list, k: int):
    reverse(arr, 0, len(arr)-k-1)
    reverse(arr, 0, len(arr)-1)
    return arr
print(left_k_rotations([1,2,3,4,5,6,7,8,9,10], 2))
print(right_k_rotations([1,2,3,4,5,6,7,8, 9, 10], 2))