# Sum of matrix
def sol(mat: list) -> int:
    rows = len(mat)
    cols = len(mat[0])
    ans = 0
    for i in range(rows):
        for j in range(cols):
            ans += mat[i][j]
    return ans

print(sol([[1,2,3,4],[1,2,3,4],[1,1,1,1]])) # 24