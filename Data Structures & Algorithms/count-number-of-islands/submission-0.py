class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (0, 1),   # right
            (0, -1),  # left
            (1, 0),   # down
            (-1, 0),  # up
        ]

        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)])

            # Mark the starting land as visited.
            grid[start_row][start_col] = "0"

            while queue:
                row, col = queue.popleft()

                for row_off, col_off in directions:
                    new_row = row + row_off
                    new_col = col + col_off

                    # Skip positions outside the grid.
                    if not (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                    ):
                        continue

                    # Skip water or previously visited land.
                    if grid[new_row][new_col] == "0":
                        continue

                    # Mark before adding to the queue.
                    grid[new_row][new_col] = "0"
                    queue.append((new_row, new_col))

        count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col)
                    count += 1

        return count