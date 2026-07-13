class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def in_degree(graph):
            indegree = {node :0 for node in graph}
            for node in graph:
                for neighbor in graph[node]:
                    indegree[neighbor] += 1
            
            return indegree

        def topo_sort(graph):
            res = []
            q = deque()
            indegree = in_degree(graph)
            for node in indegree:
                if indegree[node] == 0:
                    q.append(node)

            while q:
                node = q.popleft()
                res.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)

            return res if len(res) == numCourses else None

        
        graph = {
            course: []
            for course in range(numCourses)
        }

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        order = topo_sort(graph)

        return order or []