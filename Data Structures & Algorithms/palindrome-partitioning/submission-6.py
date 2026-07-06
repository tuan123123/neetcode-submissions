from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(word):
            return word == word[::-1]

        res = []

        def dfs(start_index, path):
            if start_index == len(s):
                res.append(path.copy())
                return

            for end in range(start_index + 1, len(s) + 1):
                a = s[start_index:end]

                if not isPalin(a):
                    continue

                path.append(a)
                dfs(end, path)
                path.pop()

        dfs(0, [])
        return res