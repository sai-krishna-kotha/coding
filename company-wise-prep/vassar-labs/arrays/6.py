def second_max(arr: list):
    ans = float("-inf")
    first = float("-inf")
    for ele in arr:
        if ele > first:
            ans = first
            first = ele
        elif ele > ans and first != ele:
            ans = ele
    return -1 if ans == float("-inf") else ans

print(second_max([1,2,3,4,5,6,4,6]))