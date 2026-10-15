class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(opens, closes, subset):
            if opens + closes == 2 * n:
                if opens == closes:
                    res.append("".join(subset))
                return
            
            if opens < n:
                subset.append('(')
                dfs(opens + 1, closes, subset)
                subset.pop()

            if closes < opens:
                subset.append(')')
                dfs(opens, closes + 1, subset)
                subset.pop()
        
        dfs(0, 0, [])
        return res