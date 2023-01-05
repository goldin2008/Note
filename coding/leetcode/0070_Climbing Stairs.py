# 空间复杂度为O(n)版本
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] 为第 i 阶楼梯有多少种方法爬到楼顶
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# 空间复杂度为O(1)版本
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            tmp = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = tmp
        return dp[1]
