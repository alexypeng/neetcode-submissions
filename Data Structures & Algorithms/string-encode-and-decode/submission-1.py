class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        while s:
            length = ""
            while s[0] != "#":
                length += s[0]
                s = s[1:]
            length = int(length)

            res.append(s[1: 1+length])

            s = s[1+length:]
        
        return res
