class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = [[False] * cols for _ in range(rows)]
        q = deque()
        land = 0
        borderLand = 0
        for r in range(rows):
            for c in range(cols):
                land += grid[r][c]
                if (grid[r][c] == 1 and (r in [0, rows - 1] or c in [0, cols - 1])):
                    q.append((r, c))
                    visit[r][c] = True
        while q:
            r, c = q.popleft()
            borderLand += 1
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and not visit[nr][nc]):
                    q.append((nr, nc))
                    visit[nr][nc] = True
        return land - borderLand
