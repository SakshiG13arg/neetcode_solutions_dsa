class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            row_sum = sum(grid[r])
            if row_sum <= 1:
                continue
            res += row_sum
            for c in range(cols):
                if grid[r][c]:
                    grid[r][c] = -1
        for c in range(cols):
            col_sum = unmarked = 0
            for r in range(rows):
                col_sum += abs(grid[r][c])
                if grid[r][c] > 0:
                    unmarked += 1
                elif grid[r][c] < 0:
                    grid[r][c] = 1
            if col_sum >= 2:
                res += unmarked
        return res
