k, n, w = map(int, input().split())
req = 0
for i in range(1, w+1):
    req += i*k
borrow = req-n
if borrow < 0:
    print(0)
else:
    print(req-n)