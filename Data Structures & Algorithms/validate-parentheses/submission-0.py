class Solution:
    def isValid(self, s: str) -> bool:
        para = []
        closeToOpen = { "}": "{", ")": "(", "]": "[" }

        for c in s:
            if c in closeToOpen:
                if para and para[-1] == closeToOpen[c]:
                    para.pop()
                else:
                    return False
            else:
                para.append(c)

        return True if not para else False