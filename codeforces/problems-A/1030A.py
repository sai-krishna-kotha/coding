n = int(input())
arr = list(map(int, input().split()))
if any(arr):
    print("HARD")
else:
    print("EASY")