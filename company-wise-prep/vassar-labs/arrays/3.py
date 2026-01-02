# three sum closest
def sol(arr: list, target: int) -> int:
    arr.sort()
    ans = float("inf")
    n = len(arr)
    for i in range(n-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            curr_sum = arr[i] + arr[j] + arr[k]
            if abs(curr_sum - target) < abs(ans - target):
                ans = curr_sum
            elif curr_sum < target:
                j += 1
            elif curr_sum > target:
                k -= 1
            else:
                return ans
    return ans

print(sol([-1,2,1,-4], 1)) # 2