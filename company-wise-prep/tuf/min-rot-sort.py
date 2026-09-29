def min_bs(arr):
    low = 0
    high = len(arr)-1
    ans = float("inf")
    while low <= high:
        mid = (low+high)//2
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue
        if arr[low] <= arr[mid]:
            ans = min(ans, arr[low])
            low = mid + 1
        else:
            ans = min(ans, arr[mid])
            high = mid - 1
    return ans


arr = [3,3,3,1,3,3,3,3,3,3]
ans = min_bs(arr)
print(ans)