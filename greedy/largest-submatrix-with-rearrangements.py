class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        for r in range(1, rows):
            for c in range(cols):
                if matrix[r][c]:
                    matrix[r][c] += matrix[r - 1][c]
        for r in range(rows):
            matrix[r].sort(reverse = True)
            for i in range(cols):
                res = max(res, (i + 1) * matrix[r][i])
        return res
