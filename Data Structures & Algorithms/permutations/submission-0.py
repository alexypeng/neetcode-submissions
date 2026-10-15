class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(remaining, subset):
            if not remaining:
                res.append(subset.copy())
                return
            
            for i in range(len(remaining)):
                subset.append(remaining[i])
                
                dfs(remaining[:i] + remaining[i+1:], subset)
                subset.pop()
            
        dfs(nums, [])
        return res
        