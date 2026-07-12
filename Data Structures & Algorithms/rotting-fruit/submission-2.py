class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                for r_off, c_off in directions:
                    row, col = r + r_off, c + c_off
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1

            minute += 1
        
        return minute if fresh == 0 else -1
