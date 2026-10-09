class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            "]" : '[',
            '}' : '{',
            ')' : '('
        }
        stack = []

        for c in s:
            if c in closeToOpen:
                if closeToOpen[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return True if not stack else False