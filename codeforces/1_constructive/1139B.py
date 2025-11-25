n = int(input())
arr = list(map(int, input().split()))
ans = 0
if len(arr) >= 1:
    ans += arr[-1]

for i in range(n-2, -1, -1):
    if arr[i] < arr[i+1]:
        ans += arr[i]
        # print(f"i is {i},ans is {ans},arr[i] is {arr[i]}")
    else:
        diff = arr[i] - arr[i+1]
        arr[i] = arr[i] - diff - 1
        if arr[i] < arr[i+1] and arr[i] > 0:
            ans += arr[i]
            # print(f"i is {i},ans is {ans},arr[i] is {arr[i]}")
        else:
            break
print(ans)