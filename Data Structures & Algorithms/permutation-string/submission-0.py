class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = [0] * 26
        for c in s1:
            s1_map[ord(c) - ord('a')] += 1
    
        s2_map = [0] * 26
        for i in range(len(s1)):
            s2_map[ord(s2[i]) - ord('a')] += 1

        if s1_map == s2_map:
            return True
        
        start = 0
        for end in range(len(s1), len(s2)):
            s2_map[ord(s2[start]) - ord('a')] -= 1
            start += 1
            s2_map[ord(s2[end]) - ord('a')] += 1

            print(s2[start:end+1])

            if s1_map == s2_map:
                return True
        
        return False