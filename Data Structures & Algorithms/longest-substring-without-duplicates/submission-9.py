class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        length = 0
        seen = set()

        left = 0

        for right in s:
            while right in seen:
                length -= 1
                seen.remove(s[left])
                left += 1
            
            seen.add(right)
            length += 1

            res = max(res, length)
        
        return res