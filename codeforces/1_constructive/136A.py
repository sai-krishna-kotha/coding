n = int(input())
arr = list(map(int, input().split()))
ans = [0]*len(arr)
for i , ele in enumerate(arr):
    ans[ele-1] = i+1
print(' '.join(map(str,ans)))