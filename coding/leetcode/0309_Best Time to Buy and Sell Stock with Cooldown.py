class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0] * 4 for _ in range(n)]
        dp[0][0] = -prices[0] #持股票
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], max(dp[i-1][3], dp[i-1][1]) - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][3])
            dp[i][2] = dp[i-1][0] + prices[i]
            dp[i][3] = dp[i-1][2]
        return max(dp[n-1][3], dp[n-1][1], dp[n-1][2])
