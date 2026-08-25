class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        abbadc

        """
        def is_palin(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        l = 0
        r =  len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return (is_palin(l + 1, r) or is_palin(l, r - 1))
            l += 1
            r -= 1
        
        """
        O(n)
        O(1)
        """
        return True


        

            

        