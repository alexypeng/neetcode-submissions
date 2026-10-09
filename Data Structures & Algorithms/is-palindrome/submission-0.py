class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while (r > l):
            while not s[l].isalnum():
                l += 1
            while not s[r].isalnum():
                r -= 1
            if s[r].lower() != s[l].lower():
                return False
            r -= 1
            l += 1
        
        return True