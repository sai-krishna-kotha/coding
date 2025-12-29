# Binary Search in Array
def sol(arr: list, target: int) -> int:
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        # mid = low + (high - low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(sol([1,2,3,4,5], 4)) # 3