class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        visited = set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            visited.add(node)
            while q:
                current = q.popleft()
                for nei in adj[current]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
        

        res = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                res += 1
        
        return res
                