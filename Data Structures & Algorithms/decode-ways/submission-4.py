class Solution:
    def numDecodings(self, s: str) -> int:
        dp = defaultdict(int)
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                if i == 0 or s[i-1] == '0':
                    return 0
                elif i == len(s) - 1:
                    dp[i] = 0
                else:
                    dp[i] += dp[i+1]
            else:
                dp[i] += dp[i+1]
                if int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+2]

        return dp[0]