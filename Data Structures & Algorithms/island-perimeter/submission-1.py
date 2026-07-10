class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        col = len(grid[0])
        perimeter = 0

        directions = [(0, -1),  (0, 1), (1, 0), (-1, 0)]

        for row in range(rows):
            for column in range(col):
                if grid[row][column] == 0:
                    continue
                
                for row_off, col_off in directions:
                    r = row + row_off
                    c = column + col_off

                    outside = not (0 <= r < rows and 0 <= c < col)

                    if outside:
                        perimeter += 1
                    elif grid[r][c] == 0:
                        perimeter += 1
        
        return perimeter