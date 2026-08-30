class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        weighted graph then bfs multiply
        """

        graph = defaultdict(list)
        """
        graph[node] = [(neighbor, weight)]
        """

        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]

            graph[a].append((b, value))
            graph[b].append((a, 1/value))
        
        def bfs(start, target):
            if start not in graph or target not in graph:
                return -1.0
            
            if start == target:
                return 1.0
            
            q = deque([(start, 1.0)])
            visited = {start}

            while q:
                current, current_value = q.popleft()

                for nei, weight in graph[current]:
                    if nei in visited:
                        continue
                    
                    next_value = current_value * weight

                    if nei == target:
                        return next_value
                    
                    visited.add(nei)
                    q.append((nei, next_value))

            return -1.0

        res = []
        for start, target in queries:
            res.append(bfs(start, target))

        return res 