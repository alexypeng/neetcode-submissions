class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hi = 0

        for i in range(len(s)):
            repl = 0
            length = 0
            j = i
            while j < len(s) and (repl < k or s[j] == s[i]):
                if s[j] != s[i]:
                    repl += 1
                length += 1
                j += 1
            hi = max(hi, length)
        
        return hi