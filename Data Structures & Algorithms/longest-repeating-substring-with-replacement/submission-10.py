class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cmap = defaultdict(int)
        res = 0

        start = 0
        for end in range(len(s)):
            cmap[s[end]] += 1

            while end - start + 1 - max(cmap.values()) > k:
                cmap[s[start]] -= 1
                start += 1
            
            res = max(res, end - start + 1)
        
        return res