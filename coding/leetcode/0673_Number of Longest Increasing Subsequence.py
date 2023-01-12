class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size<= 1: return size

        dp = [1 for i in range(size)]
        count = [1 for i in range(size)]

        maxCount = 0
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i] :
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i] :
                        count[i] += count[j]
                if dp[i] > maxCount:
                    maxCount = dp[i]
        result = 0
        for i in range(size):
            if maxCount == dp[i]:
                result += count[i]
        return result
