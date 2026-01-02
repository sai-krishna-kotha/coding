# two sum
def sol(arr: list, target: int) -> list:
    dici = dict()
    ans = []
    for i, ele in enumerate(arr):
        x = target - ele
        if x in dici:
            # return [dici[x], i]
            ans.append([dici[x], i])
        dici[ele] = i
    # return []
    return ans

print(sol([1,2,3,4,5], 7)) # [2, 3]