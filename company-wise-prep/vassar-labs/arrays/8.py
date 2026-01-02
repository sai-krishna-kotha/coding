def buy_sell_i(arr):
    min_so_far = float('inf')
    ans = float('-inf')
    for ele in arr:
        min_so_far = min(min_so_far, ele)
        ans = max(ans, ele - min_so_far)
    return ans

def buy_sell_ii(arr):
    ans = 0
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            ans += arr[i] - arr[i-1]
    return ans
