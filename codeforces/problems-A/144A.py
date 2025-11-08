n = int(input())
arr = list(map(int, input().split()))

maxi_i = arr.index(max(arr))

mini_i = n - 1 - arr[::-1].index(min(arr))

moves = maxi_i + n - mini_i - 1
if maxi_i > mini_i:
    moves -= 1
print(moves)