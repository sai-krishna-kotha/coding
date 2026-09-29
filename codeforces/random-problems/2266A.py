
def solve(total, arr):
	return total - min(arr)

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        total = int(input())
        arr = list(map(int, input().split()))
        ans = solve(total, arr)
        print(ans)