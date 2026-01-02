def merge_two_sorted_arrs(arr1: list, arr2: list):
    ans = []
    m = len(arr1)
    n = len(arr2)
    i = j = 0
    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    while i < m:
        ans.append(arr1[i])
        i += 1
    while j < n:
        ans.append(arr2[j])
        j += 1
    return ans
def merge_two_sorted_arrs_optimized(arr1: list, arr2: list):
    m = len(arr1)
    n = len(arr2)
    arr1 = arr1 + [0] * n
    last = m + n - 1
    # print(arr1)
    while m > 0 and n > 0:
        if arr1[m-1] >= arr2[n-1]:
            arr1[last] = arr1[m-1]
            m -= 1
        else:
            arr1[last] = arr2[n-1]
            n -= 1
        last -= 1
    while n > 0:
        arr1[last] = arr2[n-1]
        n -= 1
        last -= 1
    return arr1

print(merge_two_sorted_arrs(arr1=[0,1,2,3,4,5], arr2=[3,4,5,6,7,8]))
print(merge_two_sorted_arrs_optimized(arr1=[0,1,2,3,4,5], arr2=[3,4,5,6,7,8]))