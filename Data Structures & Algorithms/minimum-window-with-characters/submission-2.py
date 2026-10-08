class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = Counter(t)
        missing = len(t)
        res_start = 0
        shortest = float('inf')

        start = 0
        for end in range(len(s)):
            if s[end] in tmap:
                if tmap[s[end]] > 0:
                    missing -= 1
                tmap[s[end]] -= 1

            while missing == 0:
                if end - start + 1 < shortest:
                    shortest = end - start + 1
                    res_start = start
                if s[start] in tmap:
                    tmap[s[start]] += 1
                    if tmap[s[start]] > 0:
                        missing += 1
                
                start += 1
        
        return s[res_start : res_start + shortest] if shortest < float('inf') else ""