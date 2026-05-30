class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charSet = set()
        start = 0

        for end in range(len(s)):
            while s[end] in charSet:
                charSet.remove(s[start])
                start += 1
            
            res = max(res, end - start + 1)
            charSet.add(s[end])
        
        return res