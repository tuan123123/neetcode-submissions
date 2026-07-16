class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]

        indegree = [0] * numCourses

        all_prereqs = [set() for _ in range(numCourses)]

        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        while q:
            course = q.popleft()

            for next_course in graph[course]:
                all_prereqs[next_course].add(course)

                all_prereqs[next_course].update(all_prereqs[course])

                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    q.append(next_course)

        result = []

        for u,v in queries:
            if u in all_prereqs[v]:
                result.append("True")
            else:
                result.append("False")

        return result
