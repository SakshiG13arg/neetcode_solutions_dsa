class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image
        m = len(image)
        n = len(image[0])
        q = deque([(sr, sc)])
        image[sr][sc] = color
        dirs = ([1, 0], [-1, 0], [0, 1], [0, -1])
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == orig:
                    image[nr][nc] = color
                    q.append((nr, nc))
        return image
