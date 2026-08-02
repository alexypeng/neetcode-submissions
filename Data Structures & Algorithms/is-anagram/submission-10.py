class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            tracker[s[i]] += 1
            tracker[t[i]] -= 1
        
        for num in tracker.values():
            if num != 0:
                return False
        
        return True