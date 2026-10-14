def solution():
    def solve(i, capacity, selected):
        if selected == 3:
            return 0
        if i == n:
            return float("-inf")
        not_take = solve(i+1, capacity, selected)
        take = float("-inf")
        if i+1 <= capacity:
            take = w[i] + solve(
                i+1, 
                capacity-(i+1), 
                selected+1
            )
        return max(take, not_take)
    
    n, v = map(int, input().split())
    w = list(map(int, input().split()))
    ans = solve(0, v, 0)
    print(ans)
if __name__ == "__main__":
    solution()