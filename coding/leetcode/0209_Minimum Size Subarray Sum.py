class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = float("inf")   # 定义一个无限大的数
        Sum = 0     # 滑动窗口数值之和
        i = 0      # 滑动窗口起始位置
        for j in range(len(nums)):
            Sum += nums[j]
            while Sum >= s:
                res = min(res, j-i+1)
                Sum -= nums[i]
                i += 1
        return 0 if res == float("inf") else res
