class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "#" + str(len(s)) + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        for i in range(len(s)):
            if s[i] == '#':
                i += 1
                j = i + 1
                while j in range(len(s)) and s[j].isnumeric():
                    j += 1
                length = int(s[i : j])
            
                res.append(s[j : j + length])
                i += j+length
        
        return res

