# Find an element in a array
def sol(arr: list, target):
    for ele in arr:
        if ele == target:
            return True
    return False

print(sol([1,2,3,4,5], 6))