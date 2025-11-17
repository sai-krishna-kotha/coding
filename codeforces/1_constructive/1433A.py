for _ in range(int(input())):
    ip = int(input())
    flag = False
    ans = 0
    for i in range(1, 11):
        j = 1
        temp = i
        while j < 5:
            ans += j
            if temp == ip:
                print(ans)
                flag = True
                break
            temp = temp * 10 + i
            j += 1
        if flag:
            break