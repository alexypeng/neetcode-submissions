class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        res = ""

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if j == i:
                    dp[i][j] = True
                elif j - i == 1 and s[j] == s[i]:
                    dp[i][j] = True
                elif s[j] == s[i] and dp[i+1][j-1]:
                    dp[i][j] = True
                
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j+1]
                
        return res