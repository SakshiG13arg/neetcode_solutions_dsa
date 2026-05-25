class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [0] * (n + 1)
        max_square = 0
        for r in range(m - 1, -1, -1):
            prev = 0
            for c in range(n - 1, -1, -1):
                temp = dp[c]
                if matrix[r][c] == "1":
                    dp[c] = 1 + min(dp[c], dp[c + 1], prev)
                    max_square = max(max_square, dp[c])
                else:
                    dp[c] = 0
                prev = temp
        return max_square * max_square
