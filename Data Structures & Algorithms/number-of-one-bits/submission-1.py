class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        sn = bin(n)
        for i in range(len(sn)):
            if sn[i] == "1":
                res += 1
        
        return res