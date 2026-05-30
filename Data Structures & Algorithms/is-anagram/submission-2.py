class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = s.lower()
        t = t.lower()

        letter_tracker = [0] * 26

        for i in range(len(s)):
            letter_tracker[ord(s[i]) - ord('a')] += 1
            letter_tracker[ord(t[i]) - ord('a')] -= 1
            
        return letter_tracker == [0] * 26