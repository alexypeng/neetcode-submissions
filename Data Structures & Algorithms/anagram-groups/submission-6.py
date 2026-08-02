class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)

        for s in strs:
            letters = [0] * 26

            for c in s.lower():
                letters[ord(c)-ord('a')] += 1
            
            tracker[tuple(letters)].append(s)

        return list(tracker.values())

