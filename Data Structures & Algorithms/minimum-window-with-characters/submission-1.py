class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = Counter(t)
        shortest = float('inf')
        res = ""

        start = 0
        for end in range(len(s)):
            if s[end] in tmap:
                tmap[s[end]] -= 1

            while max(tmap.values()) <= 0:
                if s[start] in tmap:
                    tmap[s[start]] += 1
                if end - start + 1 < shortest:
                    shortest = end - start + 1
                    res = s[start : end + 1]
                start += 1
        
        return res