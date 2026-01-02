# three sum
def sol(arr: list):
    arr.sort()
    n = len(arr)
    ans = []
    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            triple = arr[i] + arr[j] + arr[k]
            if triple == 0:
                ans.append([arr[i], arr[j], arr[k]])
                while j < k and arr[j] == arr[j+1]:
                    j += 1
                while k < n and arr[k] == arr[k-1]:
                    k -= 1
                j += 1
                k -= 1
            elif triple > 0:
                k -= 1
            else:
                j += 1
    return ans

print(sol([-1,0,1,2,-1,-4]))