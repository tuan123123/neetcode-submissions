class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [
            (1,0),
            (0,1),
            (0,-1),
            (-1,0)
        ]

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == "O":
                    q.append((r,c))

        while q:
            r,c = q.popleft()
            if board[r][c] == "O":
                board[r][c] = "T"
                for dr, dc in directions:
                    newr, newc = r + dr, c + dc
                    if 0 <= newr < rows and 0 <= newc < cols:
                        q.append((newr, newc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
