# Linear search
def sol(arr: list, target: int) -> int:
    for i, ele in enumerate(arr):
        if ele == target:
            return i
    return -1

print(sol([1,2,34,5,4], 5)) # 3