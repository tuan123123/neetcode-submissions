class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0] * (n + 1)
        trusted_by = [0] * (n + 1)

        for person_a, person_b in trust:
            trusts[person_a] += 1
            trusted_by[person_b] += 1
        
        for person in range(1, n + 1):
            if trusts[person] == 0 and trusted_by[person] == n - 1:
                return person
        
        return -1
