def bs(arr, target):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (high+low)//2
        if arr[mid] == target:
            return mid
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue
        # left sorted?
        if arr[low] <= arr[mid]:
            if arr[low] <= target and target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # right sorted?
        else:
            if arr[mid] <= target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

    
arr = [6,7,1,2,3,4,5]
arr = [3,3,4,3,3,3,3]
ans = bs(arr, 4)
print(ans)    