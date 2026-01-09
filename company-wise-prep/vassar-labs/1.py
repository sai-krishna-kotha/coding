def f(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = f(n-1,dp) + f(n-2, dp)
    return dp[n]
n = 6
dp = [-1]*(n+1)
print(f(n, dp))