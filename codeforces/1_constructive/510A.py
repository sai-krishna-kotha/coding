n, m = map(int, input().split())
side = 'R'
for i in range(1, n+1):
    if i & 1 == 1:
        print("#"*m)
    else:
        if side=='R':
            print(f"{'.'*(m-1)}#")
            side ='L'
        else:
            print(f"#{'.'*(m-1)}")
            side = 'R'