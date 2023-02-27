"""
因为回溯的本质是穷举，穷举所有可能，然后选出我们想要的答案，如果想让回溯法高效一些，可以加一些剪枝的操作，但也改不了回溯法就是穷举的本质。
回溯法解决的问题都可以抽象为树形结构，所有回溯法的问题都可以抽象为树形结构
本题我把回溯问题抽象为树形结构，可以直观的看出其搜索的过程: for循环横向遍历，递归纵向遍历，回溯不断调整结果集。
因为回溯法解决的都是在集合中递归查找子集，集合的大小就构成了树的宽度，递归的深度，都构成的树的深度。
递归就要有终止条件，所以必然是一棵高度有限的树（N叉树)
1. 回溯函数模板返回值以及参数
2. 回溯函数终止条件
3. 回溯搜索的遍历过程
大家可以从图中看出for循环可以理解是横向遍历，backtracking（递归）就是纵向遍历，这样就把这棵树全遍历完了，一般来说，搜索叶子节点就是找的其中一个结果了。

回溯算法能解决如下问题:
组合问题: N个数里面按一定规则找出k个数的集合
排列问题: N个数按一定规则全排列，有几种排列方式
切割问题: 一个字符串按一定规则有几种切割方式
子集问题: 一个N个数的集合里有多少符合条件的子集
棋盘问题: N皇后，解数独等等
"""
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
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 示例:
# 输入: n = 4, k = 2
# 输出:
# [
# [2,4],
# [3,4],
# [2,3],
# [1,2],
# [1,3],
# [1,4],
# ]
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]  #存放符合条件结果的集合
        path=[]  #用来存放符合条件结果
        def backtrack(n,k,startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            # for i in range(startIndex, n+1):
            for i in range(startIndex,n-(k-len(path))+2):  #优化的地方
                path.append(i)  #处理节点
                backtrack(n,k,i+1)  #递归
                path.pop()  #回溯，撤销处理的节点
        backtrack(n,k,1)
        return res


# 216.组合总和III
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 示例 1: 输入: k = 3, n = 7 输出: [[1,2,4]]
# 示例 2: 输入: k = 3, n = 9 输出: [[1,2,6], [1,3,5], [2,3,4]]
class Solution:
    def __init__(self):
        self.res = []
        self.sum_now = 0
        self.path = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtracking(k, n, 1)
        return self.res

    def backtracking(self, k: int, n: int, start_num: int):
        if self.sum_now > n:  # 剪枝
            return
        if len(self.path) == k:  # len(path)==k时不管sum是否等于n都会返回
            if self.sum_now == n:
                self.res.append(self.path[:])
            return
        for i in range(start_num, 10 - (k - len(self.path)) + 1):
            self.path.append(i)
            self.sum_now += i
            self.backtracking(k, n, i + 1)
            self.path.pop()
            self.sum_now -= i


# 17.电话号码的字母组合
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 示例: 输入："23" 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 回溯
class Solution:
    def __init__(self):
        self.answers: List[str] = []
        self.answer: str = ''
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        self.answers.clear()
        if not digits: return []
        self.backtracking(digits, 0)
        return self.answers
    
    def backtracking(self, digits: str, index: int) -> None:
        # 回溯函数没有返回值
        # Base Case
        if index == len(digits):    # 当遍历穷尽后的下一层时
            self.answers.append(self.answer)
            return 
        # 单层递归逻辑  
        letters: str = self.letter_map[digits[index]]
        for letter in letters:
            self.answer += letter   # 处理
            self.backtracking(digits, index + 1)    # 递归至下一层
            self.answer = self.answer[:-1]  # 回溯
# 回溯简化
class Solution:
    def __init__(self):
        self.answers: List[str] = []
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        self.answers.clear()
        if not digits: return []
        self.backtracking(digits, 0, '')
        return self.answers
    
    def backtracking(self, digits: str, index: int, answer: str) -> None:
        # 回溯函数没有返回值
        # Base Case
        if index == len(digits):    # 当遍历穷尽后的下一层时
            self.answers.append(answer)
            return 
        # 单层递归逻辑  
        letters: str = self.letter_map[digits[index]]
        for letter in letters:
            self.backtracking(digits, index + 1, answer + letter)    # 递归至下一层 + 回溯


# 39. 组合总和
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 示例 1： 输入：candidates = [2,3,6,7], target = 7, 所求解集为： [ [7], [2,2,3] ]
# 示例 2： 输入：candidates = [2,3,5], target = 8, 所求解集为： [   [2,2,2,2],   [2,3,3],   [3,5] ]
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
        # 对总集合排序之后，如果下一层的sum（就是本层的 sum + candidates[i]）已经大于target，就可以结束本轮for循环的遍历。
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
        # 对总集合排序之后，如果下一层的sum（就是本层的 sum + candidates[i]）已经大于target，就可以结束本轮for循环的遍历。
        for i in range(start_index, len(candidates)):
            if sum_ + candidates[i] > target: 
                return 
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i)  # 因为无限制重复选取，所以不是i-1
            sum_ -= candidates[i]   # 回溯
            self.path.pop()        # 回溯


# 40.组合总和II
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 本题的难点在于区别2中：集合（数组candidates）有重复元素，但还不能有重复的组合。
# 示例 1: 输入: candidates = [10,1,2,7,6,1,5], target = 8, 所求解集为: [ [1, 7], [1, 2, 5], [2, 6], [1, 1, 6] ]
# 示例 2: 输入: candidates = [2,5,2,1,2], target = 5, 所求解集为: [   [1,2,2],   [5] ]
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


# 131.分割回文串
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 示例: 输入: "aab" 输出: [ ["aa","b"], ["a","a","b"] ]
# 回溯+正反序判断回文串
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def partition(self, s: str) -> List[List[str]]:
        '''
        递归用于纵向遍历
        for循环用于横向遍历
        当切割线迭代至字符串末尾，说明找到一种方法
        类似组合问题，为了不重复切割同一位置，需要start_index来做标记下一轮递归的起始位置(切割线)
        '''
        self.path.clear()
        self.paths.clear()
        self.backtracking(s, 0)
        return self.paths

    def backtracking(self, s: str, start_index: int) -> None:
        # Base Case
        if start_index >= len(s):
            self.paths.append(self.path[:])
            return
        
        # 单层递归逻辑
        for i in range(start_index, len(s)):
            # 此次比其他组合题目多了一步判断：
            # 判断被截取的这一段子串([start_index, i])是否为回文串
            temp = s[start_index:i+1]
            if temp == temp[::-1]:  # 若反序和正序相同，意味着这是回文串
                self.path.append(temp)
                self.backtracking(s, i+1)   # 递归纵向遍历：从下一处进行切割，判断其余是否仍为回文串
                self.path.pop()
            else:
                continue

# 回溯+函数判断回文串
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def partition(self, s: str) -> List[List[str]]:
        '''
        递归用于纵向遍历
        for循环用于横向遍历
        当切割线迭代至字符串末尾，说明找到一种方法
        类似组合问题，为了不重复切割同一位置，需要start_index来做标记下一轮递归的起始位置(切割线)
        '''
        self.path.clear()
        self.paths.clear()
        self.backtracking(s, 0)
        return self.paths

    def backtracking(self, s: str, start_index: int) -> None:
        # Base Case
        if start_index >= len(s):
            self.paths.append(self.path[:])
            return
        
        # 单层递归逻辑
        for i in range(start_index, len(s)):
            # 此次比其他组合题目多了一步判断：
            # 判断被截取的这一段子串([start_index, i])是否为回文串
            if self.is_palindrome(s, start_index, i):
                self.path.append(s[start_index:i+1])
                self.backtracking(s, i+1)   # 递归纵向遍历：从下一处进行切割，判断其余是否仍为回文串
                self.path.pop()             # 回溯
            else:
                continue    

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        i: int = start        
        j: int = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


# 93.复原IP地址
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
class Solution:
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        本质切割问题使用回溯搜索法，本题只能切割三次，所以纵向递归总共四层
        因为不能重复分割，所以需要start_index来记录下一层递归分割的起始位置
        添加变量point_num来记录逗号的数量[0,3]
        '''
        self.result.clear()
        if len(s) > 12: return []
        self.backtracking(s, 0, 0)
        return self.result

    def backtracking(self, s: str, start_index: int, point_num: int) -> None:
        # Base Case
        if point_num == 3:
            if self.is_valid(s, start_index, len(s)-1):
                self.result.append(s[:])
            return
        # 单层递归逻辑
        for i in range(start_index, len(s)):
            # [start_index, i]就是被截取的子串
            if self.is_valid(s, start_index, i):
                s = s[:i+1] + '.' + s[i+1:]
                self.backtracking(s, i+2, point_num+1)  # 在填入.后，下一子串起始后移2位
                s = s[:i+1] + s[i+2:]    # 回溯
            else:
                # 若当前被截取的子串大于255或者大于三位数，直接结束本层循环
                break
    
    def is_valid(self, s: str, start: int, end: int) -> bool:
        if start > end: return False
        # 若数字是0开头，不合法
        if s[start] == '0' and start != end:
            return False
        if not 0 <= int(s[start:end+1]) <= 255:
            return False
        return True


# 78.子集
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
# 示例: 输入: nums = [1,2,3] 输出: [ [3],   [1],   [2],   [1,2,3],   [1,3],   [2,3],   [1,2],   [] ]
# 但是要清楚子集问题和组合问题、分割问题的的区别，子集是收集树形结构中树的所有节点的结果。
# 而组合问题、分割问题是收集树形结构中叶子节点的结果。
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
        # 收集子集，要先于终止判断(因为要收集所以node，而不只是leaf，所以要base case前把path放入paths)
        self.paths.append(self.path[:])
        # Base Case
        if start_index == len(nums):
            return

        # 单层递归逻辑
        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()     # 回溯


# 90.子集II
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 输入: [1,2,2]
# 输出: [ [2], [1], [1,2,2], [2,2], [1,2], [] ]
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


# 491.递增子序列
# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# 本题求子序列，很明显一个元素不能重复使用，所以需要startIndex，调整下一层递归的起始位置。
# 回溯
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        '''
        本题求自增子序列，所以不能改变原数组顺序
        '''
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums: List[int], start_index: int):
        # 收集结果，同78.子集，仍要置于终止条件之前
        if len(self.path) >= 2:
            # 本题要求所有的节点
            self.paths.append(self.path[:])
        
        # Base Case（可忽略）
        if start_index == len(nums):
            return

        # 单层递归逻辑
        # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
        usage_list = set()
        # 同层横向遍历
        for i in range(start_index, len(nums)):
            # 若当前元素值小于前一个时（非递增）或者曾用过，跳入下一循环
            if (self.path and nums[i] < self.path[-1]) or nums[i] in usage_list:
                continue
            usage_list.add(nums[i])
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop() 

# 回溯+哈希表去重
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        '''
        本题求自增子序列，所以不能改变原数组顺序
        '''
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums: List[int], start_index: int):
        # 收集结果，同78.子集，仍要置于终止条件之前
        if len(self.path) >= 2:
            # 本题要求所有的节点
            self.paths.append(self.path[:])
        
        # Base Case（可忽略）
        if start_index == len(nums):
            return

        # 单层递归逻辑
        # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
        usage_list = [False] * 201  # 使用列表去重，题中取值范围[-100, 100]
        # 同层横向遍历
        for i in range(start_index, len(nums)):
            # 若当前元素值小于前一个时（非递增）或者曾用过，跳入下一循环
            if (self.path and nums[i] < self.path[-1]) or usage_list[nums[i]+100] == True:
                continue
            usage_list[nums[i]+100] = True
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()


# 46.全排列
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 输入: [1,2,3]
# 输出: [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]
# 回溯
class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        因为本题排列是有序的，这意味着同一层的元素可以重复使用，但同一树枝上不能重复使用(usage_list)
        所以处理排列问题每层都需要从头搜索，故不再使用start_index
        '''
        usage_list = [False] * len(nums)
        self.backtracking(nums, usage_list)
        return self.paths

    def backtracking(self, nums: List[int], usage_list: List[bool]) -> None:
        # Base Case本题求叶子节点
        if len(self.path) == len(nums):
            self.paths.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(0, len(nums)):  # 从头开始搜索
            # 若遇到self.path里已收录的元素，跳过
            if usage_list[i] == True:
                continue
            usage_list[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, usage_list)     # 纵向传递使用信息，去重
            self.path.pop()
            usage_list[i] = False

# 回溯+丢掉usage_list
class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        因为本题排列是有序的，这意味着同一层的元素可以重复使用，但同一树枝上不能重复使用
        所以处理排列问题每层都需要从头搜索，故不再使用start_index
        '''
        self.backtracking(nums)
        return self.paths

    def backtracking(self, nums: List[int]) -> None:
        # Base Case本题求叶子节点
        if len(self.path) == len(nums):
            self.paths.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(0, len(nums)):  # 从头开始搜索
            # 若遇到self.path里已收录的元素，跳过
            if nums[i] in self.path:
                continue
            self.path.append(nums[i])
            self.backtracking(nums)
            self.path.pop()


# 47.全排列 II
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 输入：nums = [1,1,2]
# 输出： [[1,1,2], [1,2,1], [2,1,1]]
# 还要强调的是去重一定要对元素进行排序，这样我们才方便通过相邻的节点来判断是否重复使用了。
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # res用来存放结果
        if not nums: return []
        res = []
        used = [0] * len(nums)
        def backtracking(nums, used, path):
            # 终止条件
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = 1
                    path.append(nums[i])
                    backtracking(nums, used, path)
                    path.pop()
                    used[i] = 0
        # 记得给nums排序
        backtracking(sorted(nums),used,[])
        return res


# ??? 332.重新安排行程
# 给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。
# 输入：[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# 输出：["JFK", "MUC", "LHR", "SFO", "SJC"]


# ??? 第51题. N皇后
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n: return []
        board = [['.'] * n for _ in range(n)]
        res = []
        def isVaild(board,row, col):
            #判断同一列是否冲突
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False
            # 判断左上角是否冲突
            i = row -1
            j = col -1
            while i>=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # 判断右上角是否冲突
            i = row - 1
            j = col + 1
            while i>=0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def backtracking(board, row, n):
            # 如果走到最后一行，说明已经找到一个解
            if row == n:
                temp_res = []
                for temp in board:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                res.append(temp_res)
            for col in range(n):
                if not isVaild(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtracking(board, row+1, n)
                board[row][col] = '.'
        backtracking(board, 0, n)
        return res


# ??? 37. 解数独
# 编写一个程序，通过填充空格来解决数独问题。
# 一个数独的解法需遵循如下规则： 
# 数字 1-9 在每一行只能出现一次。 
# 数字 1-9 在每一列只能出现一次。 
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
# 空白格用 '.' 表示。
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)

    def backtracking(self, board: List[List[str]]) -> bool:
        # 若有解，返回True；若无解，返回False
        for i in range(len(board)): # 遍历行
            for j in range(len(board[0])):  # 遍历列
                # 若空格内已有数字，跳过
                if board[i][j] != '.': continue
                for k in range(1, 10):  
                    if self.is_valid(i, j, k, board):
                        board[i][j] = str(k)
                        if self.backtracking(board): return True
                        board[i][j] = '.'
                # 若数字1-9都不能成功填入空格，返回False无解
                return False
        return True # 有解

    def is_valid(self, row: int, col: int, val: int, board: List[List[str]]) -> bool:
        # 判断同一行是否冲突
        for i in range(9):
            if board[row][i] == str(val):
                return False
        # 判断同一列是否冲突
        for j in range(9):
            if board[j][col] == str(val):
                return False
        # 判断同一九宫格是否有冲突
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(val):
                    return False
        return True
