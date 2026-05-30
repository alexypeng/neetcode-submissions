class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}

        for s in strs:
            letters = [0] * 26

            for c in s.lower():
                letters[ord(c) - ord('a')] += 1
            
            if tuple(letters) in tracker:
                tracker[tuple(letters)].append(s)
            else:
                tracker[tuple(letters)] = [s]
        
        return list(tracker.values())