
def solution():
    
    n, m = map(int, input().split())
    arr = [0]*n
    i = 0
    while m:
        arr[i] += 1
        m -= 1
        i = (i + 1) % n
    for i in range(n):
        print(arr[i])

if __name__ == "__main__":
    solution()