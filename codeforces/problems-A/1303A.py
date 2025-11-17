for _ in range(int(input())):
    string = input()
    for i in range(len(string)):
        if string[i] == '1':
            break
    for j in range(len(string)-1, -1, -1):
        if string[j] == '1':
            break
    ans = 0
    
    while i < j:
        if string[i] == '0':
            ans += 1
        i += 1
    print(ans)