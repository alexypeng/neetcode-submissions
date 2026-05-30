class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            alpha = [0] * 26

            for c in s:
                alpha[ord(c) - ord('a')] += 1
            
            res[tuple(alpha)].append(s)

        return list(res.values())