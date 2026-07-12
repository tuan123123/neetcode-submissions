class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_q = deque()
        p_s = set()

        a_q = deque()
        a_s = set()

        m,n = len(heights), len(heights[0])

        for j in range(n):
            p_q.append((0, j))
            p_s.add((0, j))

        for i in range(1, m):
            p_q.append((i, 0))
            p_s.add((i, 0))
        
        for i in range(m):
            a_q.append((i, n - 1))
            a_s.add((i, n - 1))

        for j in range(n - 1):
            a_q.append((m - 1, j))
            a_s.add((m - 1, j))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def get_coords(que, seen):
            while que:
                r, c = que.popleft()
                for r_off, c_off in directions:
                    rnew, cnew = r + r_off, c + c_off
                    if 0  <= rnew < m and 0 <= cnew < n and heights[rnew][cnew] >= heights[r][c] and (rnew, cnew) not in seen:
                        seen.add((rnew, cnew))
                        que.append((rnew, cnew))


        get_coords(p_q, p_s)
        get_coords(a_q, a_s)
        ans = []
        for (r,c) in p_s:
            if (r ,c) in a_s:
                ans.append((r,c))

        return ans
          
