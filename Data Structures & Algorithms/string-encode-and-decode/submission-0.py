class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            ind = s.index('#')
            i = int(s[:ind])
            s = s[ind+1:]
            res.append(s[:i])
            s = s[i:]
        return res