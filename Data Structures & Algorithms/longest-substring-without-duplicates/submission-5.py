class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hi = 0

        for i in range(len(s)):
            count = 1
            track = set()
            track.add(s[i])
            
            j = i + 1
            while j < len(s) and s[j] not in track:
                count += 1
                track.add(s[j])
                j += 1
            
            hi = max(count, hi)
        
        return hi