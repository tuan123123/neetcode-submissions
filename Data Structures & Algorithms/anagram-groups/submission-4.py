class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.value())
#Time complexity: O(N log N)
#Space O(N)


#bat, tab, atb
# abt : bat, tab, atb
"""
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())
        
        




