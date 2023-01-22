"""
dp[i]: 以下标i为结尾的连续递增的子序列长度为dp[i]。
注意这里的定义，一定是以下标i为结尾，并不是说一定以下标0为起始位置。

贪心法更好理解，而且空间复杂度为O(1)，比动规O(n)更好
"""
# 动态规划：
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1
        dp = [1] * len(nums)
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]: #连续记录
                dp[i+1] = dp[i] + 1
            result = max(result, dp[i+1])
        return result

# 贪心法：
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1 #连续子序列最少也是1
        count = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]: #连续记录
                count += 1
            else: #不连续，count从头开始
                count = 1
            result = max(result, count)
        return result
