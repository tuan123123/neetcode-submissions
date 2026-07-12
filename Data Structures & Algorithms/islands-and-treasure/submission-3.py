class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()
        directions = [
            (1,0),
            (-1, 0),
            (0, -1),
            (0, 1)
        ]
        dist = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                for r_off, c_off in directions:
                    rnew, cnew = r + r_off, c + c_off
                    if not (0 <= rnew < rows and 0 <= cnew < cols):
                        continue
                    if (rnew, cnew) in visited:
                        continue
                    if grid[rnew][cnew] == - 1:
                        continue
                    
                    
                    queue.append([rnew, cnew])
                    visited.add((rnew, cnew))
            
            dist += 1

            
        