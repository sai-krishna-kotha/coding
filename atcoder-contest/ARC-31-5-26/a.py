from math import gcd
N = int(input())
for _ in range(N):
  n, a, b, c, d = map(int, input().split())
  ans = 0
#   def gcd(a, b):
#     if a == 0: return b
#     if b == 0: return a
#     if a > b:
#       a = a % b
#       return gcd(a, b)
#     else:   
#       b = b % a
#       return gcd(a, b)
  for i in range(1, n+1):
    ans += gcd(a*i+b, c*i+d)
  print(ans)