class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        if n == 1:
            return 1
        directions = [0, 1, 0, -1, 0, 1, 1, -1, -1, 1]
        q1 = deque([(0, 0)])
        q2 = deque([(n -1, n - 1)])
        grid[0][0] = -1
        grid[n - 1][n - 1] = -2
        res = 2
        start = -1
        end = -2
        while q1 and q2:
            for _ in range(len(q1)):
                r, c = q1.popleft()
                for d in range(9):
                    nr = r + directions[d]
                    nc = c + directions[d + 1]
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == end:
                            return res
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = start
                            q1.append((nr, nc))
            q1, q2 = q2, q1
            start, end = end, start
            res += 1
        return -1
