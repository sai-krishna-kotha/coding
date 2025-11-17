n, m, a = map(int, input().split())
ans = (n // a +( n % a != 0))*(m // a + (m % a != 0))
print(ans)