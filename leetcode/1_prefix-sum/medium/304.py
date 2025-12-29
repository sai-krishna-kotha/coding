matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0]*n for _ in range(m)]
        for i in range(m):
            prefix = 0
            for j in range(n):
                prefix += matrix[i][j]
                self.prefix[i][j] = prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            if col1 == 0:
                ans += self.prefix[i][col2]
            else:
                ans += self.prefix[i][col2] - self.prefix[i][col1-1]
        return ans