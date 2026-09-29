def one(n: int):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

def two(n: int):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end=" ")
        print()

def three(n: int):
    for i in range(1, n+1):
        for j in range(i):
            print(j+1, end=" ")
        print()
        
def four(n: int):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()
        
def five(n: int):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def six(n: int):
    for i in range(n, 0, -1):
        for j in range(i):
            print(j+1, end=" ")
        print()

def seven(n: int):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end=" ")
        for j in range(2*i-1):
            print("*", end=" ")
        print()
        
def eight(n: int):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(" ", end=" ")
        for j in range(2*i-1):
            print("*", end=" ")
        print()
        
def nine(n: int):
    for i in range(1, n+1):
        for j in range(n-i, 0, -1):
            print(" ", end=" ")
        for j in range(2*i-1):
            print("*", end=" ")
        print()
    for i in range(n, 0, -1):
        for j in range(n-i, 0, -1):
            print(" ", end=" ")
        for j in range(2*i-1):
            print("*", end=" ")
        print()
    
def ten(n: int):
    for i in range(1, 2*n):
        if i <= n:
            for j in range(i):
                print("*", end=" ")
            print()
        else:
            for j in range(2*n-i):
                print("*", end=" ")
            print()
            
def eleven(n: int):
    for i in range(1, n+1):
        flag = 1 if i & 1 != 0 else 0
        for i in range(i):
            print(flag, end=" ")
            flag = 0 if flag == 1 else 1
        print()
    
        
n = 5
# one(n)
# two(n)
# three(n)
# four(n)
# five(n)
# six(n)
# seven(n)
# eight(n)
# nine(n)
# ten(n)
eleven(n)