class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        original = image[sr][sc]
        """
        1 1 1
        1 1 0
        1 0 1
        """
        if original == color:
            return image
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        q = deque([(sr, sc)])
        while q:
            row, col = q.popleft()
            image[row][col] = color
            for r_off, c_off in directions:
                r, c = row + r_off, col + c_off
                if 0 <= r < m and 0 <= c < n and image[r][c] == original:
                    image[r][c] = color
                    q.append((r, c))
        
        return image
