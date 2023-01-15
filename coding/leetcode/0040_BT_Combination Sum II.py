# 回溯+巧妙去重(省去使用used
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        类似于求三数之和，求四数之和，为了避免重复组合，需要提前进行数组排序
        '''
        self.paths.clear()
        self.path.clear()
        # 必须提前进行数组排序，避免重复
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates: List[int], target: int, sum_: int, start_index: int) -> None:
        # Base Case
        if sum_ == target:
            self.paths.append(self.path[:])
            return
        
        # 单层递归逻辑
        for i in range(start_index, len(candidates)):
            # 剪枝，同39.组合总和
            if sum_ + candidates[i] > target:
                return
            
            # 跳过同一树层使用过的元素
            if i > start_index and candidates[i] == candidates[i-1]:
                continue
            
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i+1)
            self.path.pop()             # 回溯，为了下一轮for loop
            sum_ -= candidates[i]       # 回溯，为了下一轮for loop


# 回溯+去重（使用used）
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []
        self.used = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        类似于求三数之和，求四数之和，为了避免重复组合，需要提前进行数组排序
        本题需要使用used，用来标记区别同一树层的元素使用重复情况：注意区分递归纵向遍历遇到的重复元素，和for循环遇到的重复元素，这两者的区别
        '''
        self.paths.clear()
        self.path.clear()
        self.usage_list = [False] * len(candidates)
        # 必须提前进行数组排序，避免重复
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates: List[int], target: int, sum_: int, start_index: int) -> None:
        # Base Case
        if sum_ == target:
            self.paths.append(self.path[:])
            return
        
        # 单层递归逻辑
        for i in range(start_index, len(candidates)):
            # 剪枝，同39.组合总和
            if sum_ + candidates[i] > target:
                return
            
            # 检查同一树层是否出现曾经使用过的相同元素
            # 若数组中前后元素值相同，但前者却未被使用(used == False)，说明是for loop中的同一树层的相同元素情况
            if i > 0 and candidates[i] == candidates[i-1] and self.usage_list[i-1] == False:
                continue

            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.usage_list[i] = True
            self.backtracking(candidates, target, sum_, i+1)
            self.usage_list[i] = False  # 回溯，为了下一轮for loop
            self.path.pop()             # 回溯，为了下一轮for loop
            sum_ -= candidates[i]       # 回溯，为了下一轮for loop
