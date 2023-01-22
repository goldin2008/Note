"""
注意最后的结果可不是dp[nums.size() - 1]!
在回顾一下dp[i]的定义:包括下标i之前的最大连续子序列和为dp[i]。
那么我们要找最大的连续子序列，就应该找每一个i为终点的连续最大子序列。
所以在递推公式的时候，可以直接选出最大的dp[i]。
"""
# 动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i]) #状态转移公式
            result = max(result, dp[i]) #result 保存dp[i]的最大值
        return result


# 贪心法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -float('inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count <= 0:
                count = 0
        return result
