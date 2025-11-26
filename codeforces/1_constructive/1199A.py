n, x, y = map(int, input().split())
arr = list(map(int, input().split()))
def valid_x(d, x):
    i = d-1
    while i >= 0 and x > 0:
        x -= 1
        if arr[d] >= arr[i]:
            return False
        i -= 1
    return True
def valid_y(d, y):
    i = d+1
    while i < len(arr) and y > 0:
        y -= 1
        if arr[d] >= arr[i]:
            return False
        i += 1
    return True
for i in range(n):
    if valid_x(i, x) and valid_y(i, y):
        print(i+1)
        break