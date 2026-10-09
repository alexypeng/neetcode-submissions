class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        i = 0

        while i < len(s):
            length = 0
            chars = set()

            while i < len(s) and s[i] not in chars:
                chars.add(s[i])
                length += 1
                i += 1
            
            longest = max(length, longest)
        return longest