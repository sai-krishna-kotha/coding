def spiral_matrix(mat):
    ans = []
    top = 0
    bottom = len(mat) - 1
    left = 0
    right = len(mat[0]) - 1
    while top <= bottom and left <= right:
        for col in range(left, right+1) :
            ans.append(mat[top][col])
        top += 1
        for row in range(top, bottom + 1):
            ans.append(mat[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left-1, -1):
                ans.append(mat[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top -1, -1):
                ans.append(mat[row][left])
            left += 1
    return ans
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
ans = spiral_matrix(matrix)
# print(ans)
def buy_sell(arr):
    mini = float('inf')
    ans = 0
    b_s = [-1,-1]
    for i, ele in enumerate(arr):
        if ele < mini:
            mini = ele
            b_s[0] = i
        else:
            if ele- mini > ans:
                ans = ele - mini
                b_s[1] = i
            # ans = max(ans, ele-mini)
    return ans, b_s

arr = [5,7,2,6,3]
ans, b_s = buy_sell(arr)
# print(ans, b_s)

class A:
	def p(self):
		return "Hii"
class B(A):
	def p(self):
		return "hello"
class C(A):
	def p(self):
		return "heyy"

a = [B(), C()]
for x in a:
	print(x.p())
