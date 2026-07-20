class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(string1):
            return string1 == string1[::-1]
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j + 1]
                if is_palindrome(substring):
                    if len(substring) > len(res):
                        res = substring
        
        return res