# incomplete
x = int(input())
n = 0
temp = 0
i = 1
if x == 1:
    print(1)
    exit()
while n+temp+i < x:
    temp = temp + i
    n = n + temp
    # print(f"{i, temp, n}")
    i += 1
print(i-1)