class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        index = { "}": "{", ")": "(", "]": "[" }

        for c in s:
            if c in index:
                if stack and stack[-1] == index[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
