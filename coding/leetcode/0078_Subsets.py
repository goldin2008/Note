class Solution:
    def __init__(self):
        self.path: List[int] = []
        self.paths: List[List[int]] = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.paths.clear()
        self.path.clear()
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums: List[int], start_index: int) -> None:
        # 收集子集，要先于终止判断
        self.paths.append(self.path[:])
        # Base Case
        if start_index == len(nums):
            return

        # 单层递归逻辑
        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()     # 回溯

