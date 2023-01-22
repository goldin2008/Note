"""
dp[i] = max(dp[i], dp[j] + 1)
位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1 的最大值。
dp[i] 是有0到i-1各个位置的最长递增子序列 推导而来，那么遍历i一定是从前向后遍历。

现用dp[i]记录内层循环最大值，再用result记录外层循环，也是整个的最大值.
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        result = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i]) #取长的子序列
        return result
