class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums: List[int], start_index: int) -> None:
        # ps.空集合仍符合要求
        self.paths.append(self.path[:])
        # Base Case
        if start_index == len(nums):
            return
        
        # 单层递归逻辑
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i-1]:
                # 当前后元素值相同时，跳入下一个循环，去重
                continue
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()


# 不使用used数组
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort() # 去重需要先对数组进行排序

        def backtracking(nums, startIndex):
            # 终止条件
            res.append(path[:])
            if startIndex == len(nums):
                return
            
            # for循环
            for i in range(startIndex, len(nums)):
                # 数层去重
                if i > startIndex and nums[i] == nums[i-1]: # 去重
                    continue
                path.append(nums[i])
                backtracking(nums, i+1)
                path.pop()
        
        backtracking(nums, 0)
        return res


# 使用used数组
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        nums.sort()
        used = [0] * len(nums)
        def backtrack(nums, startIdx):
            result.append(path[:])
            for i in range(startIdx, len(nums)):
                if i > startIdx and nums[i] == nums[i-1] and used[i-1] == 0:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()
                used[i] = 0
        backtrack(nums, 0)
        return result
