"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        
        return [lower_bound, upper_bound]
        
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        
        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)    
            
            if nums[mid] == target:
                
                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    # Search on the left side for the bound.
                    end = mid - 1
                else:
                    
                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    
                    # Search on the right side for the bound.
                    begin = mid + 1
            
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        
        return -1

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRightBorder(nums:List[int], target:int) -> int:
            left, right = 0, len(nums)-1
            rightBoder = -2 # 记录一下rightBorder没有被赋值的情况
            while left <= right:
                middle = left + (right-left) // 2
                if nums[middle] > target:
                    right = middle - 1
                else: # 寻找右边界，nums[middle] == target的时候更新left
                    left = middle + 1
                    rightBoder = left
    
            return rightBoder
        
        def getLeftBorder(nums:List[int], target:int) -> int:
            left, right = 0, len(nums)-1 
            leftBoder = -2 # 记录一下leftBorder没有被赋值的情况
            while left <= right:
                middle = left + (right-left) // 2
                if nums[middle] >= target: #  寻找左边界，nums[middle] == target的时候更新right
                    right = middle - 1;
                    leftBoder = right;
                else:
                    left = middle + 1
            return leftBoder
        leftBoder = getLeftBorder(nums, target)
        rightBoder = getRightBorder(nums, target)
        # 情况一
        if leftBoder == -2 or rightBoder == -2: return [-1, -1]
        # 情况三
        if rightBoder -leftBoder >1: return [leftBoder + 1, rightBoder - 1]
        # 情况二
        return [-1, -1]
# 解法2
# 1、首先，在 nums 数组中二分查找 target；
# 2、如果二分查找失败，则 binarySearch 返回 -1，表明 nums 中没有 target。此时，searchRange 直接返回 {-1, -1}；
# 3、如果二分查找成功，则 binarySearch 返回 nums 中值为 target 的一个下标。然后，通过左右滑动指针，来找到符合题意的区间
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums:List[int], target:int) -> int:
            left, right = 0, len(nums)-1
            while left<=right: # 不变量：左闭右闭区间
                middle = left + (right-left) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target: 
                    left = middle + 1
                else:
                    return middle
            return -1
        index = binarySearch(nums, target)
        if index == -1:return [-1, -1] # nums 中不存在 target，直接返回 {-1, -1}
        # nums 中存在 targe，则左右滑动指针，来找到符合题意的区间
        left, right = index, index
        # 向左滑动，找左边界
        while left -1 >=0 and nums[left - 1] == target: left -=1
        # 向右滑动，找右边界
        while right+1 < len(nums) and nums[right + 1] == target: right +=1
        return [left, right]
# 解法3
# 1、首先，在 nums 数组中二分查找得到第一个大于等于 target的下标（左边界）与第一个大于target的下标（右边界）；
# 2、如果左边界<= 右边界，则返回 [左边界, 右边界]。否则返回[-1, -1]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums:List[int], target:int, lower:bool) -> int:
            left, right = 0, len(nums)-1
            ans = len(nums)
            while left<=right: # 不变量：左闭右闭区间
                middle = left + (right-left) //2 
                # lower为True，执行前半部分，找到第一个大于等于 target的下标 ，否则找到第一个大于target的下标
                if nums[middle] > target or (lower and nums[middle] >= target): 
                    right = middle - 1
                    ans = middle
                else: 
                    left = middle + 1
            return ans

        leftBorder = binarySearch(nums, target, True) # 搜索左边界
        rightBorder = binarySearch(nums, target, False) -1  # 搜索右边界
        if leftBorder<= rightBorder and rightBorder< len(nums) and nums[leftBorder] == target and  nums[rightBorder] == target:
            return [leftBorder, rightBorder]
        return [-1, -1]
# 解法4
# 1、首先，在 nums 数组中二分查找得到第一个大于等于 target的下标leftBorder；
# 2、在 nums 数组中二分查找得到第一个大于等于 target+1的下标， 减1则得到rightBorder；
# 3、如果开始位置在数组的右边或者不存在target，则返回[-1, -1] 。否则返回[leftBorder, rightBorder]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums:List[int], target:int) -> int:
            left, right = 0, len(nums)-1
            while left<=right: # 不变量：左闭右闭区间
                middle = left + (right-left) //2 
                if nums[middle] >= target: 
                    right = middle - 1
                else: 
                    left = middle + 1
            return left  # 若存在target，则返回第一个等于target的值 

        leftBorder = binarySearch(nums, target) # 搜索左边界
        rightBorder = binarySearch(nums, target+1) -1  # 搜索右边界
        if leftBorder == len(nums) or nums[leftBorder]!= target: # 情况一和情况二
            return [-1, -1]
        return [leftBorder, rightBorder]
