# 直接使用sorted()会开辟新的空间并返回一个新的list，故补充一个原地反转函数
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length - 1, -1, -1):
            for j in range(length - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    self.reverse(nums, i + 1, length - 1)
                    return  
        self.reverse(nums, 0, length - 1)
    
    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
"""
265 / 265 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 14.9 MB
"""