class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        path = []
        def dfs(i):
            if i == len(digits):
                res.append("".join(path))
                return
            
            for digit in phone_to_letter[digits[i]]:
                path.append(digit)
                dfs(i + 1)
                path.pop()
        

        if len(digits) > 0:
            dfs(0)
        else:
            return []
        
        return res