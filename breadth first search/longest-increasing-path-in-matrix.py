class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        indegree = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < matrix[r][c]):
                        indegree[r][c] += 1
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if indegree[r][c] == 0:
                    q.append([r, c])
        length = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]):
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            q.append([nr, nc])
            length += 1
        return length
