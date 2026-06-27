class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])
        res = [["."] * rows for _ in range(cols)]
        for r in range(rows):
            i = cols - 1
            for c in reversed(range(cols)):
                if boxGrid[r][c] == "#":
                    res[i][rows - r - 1] = "#"
                    i -= 1
                elif boxGrid[r][c] == "*":
                    res[c][rows - r - 1] = "*"
                    i = c - 1
        return res
