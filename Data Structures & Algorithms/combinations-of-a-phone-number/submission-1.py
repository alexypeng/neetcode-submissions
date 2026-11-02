class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        substring = ""

        def backtrack(idx):
            nonlocal substring
            if idx == len(digits):
                res.append(substring)
                return
            
            for char in digitToChar[digits[idx]]:
                substring += char
                backtrack(idx + 1)
                substring = substring[:-1]
        
        backtrack(0)
        return res
