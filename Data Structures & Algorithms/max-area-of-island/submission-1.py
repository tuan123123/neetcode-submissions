class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        rows, cols = len(grid), len(grid[0])
        area = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            res = 1

            while q:
                ro, co = q.popleft()
                for row_off, col_off in directions:
                    row = ro + row_off
                    col = co + col_off
                    if not(0 <= row < rows and 0 <= col < cols):
                        continue
                    if grid[row][col] == 0:
                        continue
                    
                    q.append((row, col))
                    grid[row][col] = 0
                    res += 1
            
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))

        return area

        
