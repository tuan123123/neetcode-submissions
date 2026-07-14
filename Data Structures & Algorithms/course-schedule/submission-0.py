from collections import deque
from typing import List


class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:

        def find_indegree(graph):
            indegree = {node: 0 for node in graph}

            for node in graph:
                for neighbor in graph[node]:
                    indegree[neighbor] += 1

            return indegree

        def topo_sort(graph):
            result = []
            q = deque()
            indegree = find_indegree(graph)

            for node in indegree:
                if indegree[node] == 0:
                    q.append(node)

            while q:
                node = q.popleft()
                result.append(node)

                for neighbor in graph[node]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        q.append(neighbor)

            if len(result) == len(graph):
                return result

            return None

        # This must be outside topo_sort
        graph = {
            course: []
            for course in range(numCourses)
        }

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        order = topo_sort(graph)

        return order is not None