class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rr, cc = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r,c):
            q = deque([(r, c)])

            grid[r][c] == "0"

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    row_off, col_off = row + dr, col + dc
                    if (row_off < 0 or col_off < 0 or row_off >= len(grid) or col_off >= len(grid[0])):
                        continue
                    
                    if grid[row_off][col_off] == "0":
                        continue
                    
                    grid[row_off][col_off] = "0"
                    q.append((row_off, col_off))
        count = 0
        for i in range(rr):
            for j in range(cc):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        
        return count