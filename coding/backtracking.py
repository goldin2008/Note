# 回溯算法模板：
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择: 本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}


# 第77题. 组合
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]  #存放符合条件结果的集合
        path=[]  #用来存放符合条件结果
        def backtrack(n,k,startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex,n-(k-len(path))+2):  #优化的地方
                path.append(i)  #处理节点
                backtrack(n,k,i+1)  #递归
                path.pop()  #回溯，撤销处理的节点
        backtrack(n,k,1)
        return res


# 39. 组合总和
class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        因为本题没有组合数量限制，所以只要元素总和大于target就算结束
        '''
        self.path.clear()
        self.paths.clear()

        # 为了剪枝需要提前进行排序
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates: List[int], target: int, sum_: int, start_index: int) -> None:
        # Base Case
        if sum_ == target:
            self.paths.append(self.path[:]) # 因为是shallow copy，所以不能直接传入self.path
            return
        # 单层递归逻辑 
        # 如果本层 sum + condidates[i] > target，就提前结束遍历，剪枝
        for i in range(start_index, len(candidates)):
            if sum_ + candidates[i] > target: 
                return 
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i)  # 因为无限制重复选取，所以不是i-1
            sum_ -= candidates[i]   # 回溯
            self.path.pop()        # 回溯

