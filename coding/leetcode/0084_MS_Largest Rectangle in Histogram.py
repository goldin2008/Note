# 双指针；暴力解法（leetcode超时）
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 从左向右遍历：以每一根柱子为主心骨（当前轮最高的参照物），迭代直到找到左侧和右侧各第一个矮一级的柱子
        res = 0

        for i in range(len(heights)):
            left = i
            right = i
            # 向左侧遍历：寻找第一个矮一级的柱子
            for _ in range(left, -1, -1):
                if heights[left] < heights[i]:
                    break
                left -= 1
            # 向右侧遍历：寻找第一个矮一级的柱子
            for _ in range(right, len(heights)):
                if heights[right] < heights[i]:
                    break
                right += 1
                
            width = right - left - 1
            height = heights[i]
            res = max(res, width * height)

        return res

# DP动态规划
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        # 两个DP数列储存的均是下标index
        min_left_index = [0] * size
        min_right_index = [0] * size
        result = 0

        # 记录每个柱子的左侧第一个矮一级的柱子的下标
        min_left_index[0] = -1  # 初始化防止while死循环
        for i in range(1, size):
            # 以当前柱子为主心骨，向左迭代寻找次级柱子
            temp = i - 1
            while temp >= 0 and heights[temp] >= heights[i]:
                # 当左侧的柱子持续较高时，尝试这个高柱子自己的次级柱子（DP
                temp = min_left_index[temp]
            # 当找到左侧矮一级的目标柱子时
            min_left_index[i] = temp
        
        # 记录每个柱子的右侧第一个矮一级的柱子的下标
        min_right_index[size-1] = size  # 初始化防止while死循环
        for i in range(size-2, -1, -1):
            # 以当前柱子为主心骨，向右迭代寻找次级柱子
            temp = i + 1
            while temp < size and heights[temp] >= heights[i]:
                # 当右侧的柱子持续较高时，尝试这个高柱子自己的次级柱子（DP
                temp = min_right_index[temp]
            # 当找到右侧矮一级的目标柱子时
            min_right_index[i] = temp
        
        for i in range(size):
            area = heights[i] * (min_right_index[i] - min_left_index[i] - 1)
            result = max(area, result)
        
        return result

# 单调栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic Stack
        '''
        找每个柱子左右侧的第一个高度值小于该柱子的柱子
        单调栈：栈顶到栈底：从大到小（每插入一个新的小数值时，都要弹出先前的大数值）
        栈顶，栈顶的下一个元素，即将入栈的元素：这三个元素组成了最大面积的高度和宽度
        情况一：当前遍历的元素heights[i]大于栈顶元素的情况
        情况二：当前遍历的元素heights[i]等于栈顶元素的情况
        情况三：当前遍历的元素heights[i]小于栈顶元素的情况
        '''

        # 输入数组首尾各补上一个0（与42.接雨水不同的是，本题原首尾的两个柱子可以作为核心柱进行最大面积尝试
        heights.insert(0, 0)
        heights.append(0)
        stack = [0]
        result = 0
        for i in range(1, len(heights)):
            # 情况一
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            # 情况二
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            # 情况三
            else:
                # 抛出所有较高的柱子
                while stack and heights[i] < heights[stack[-1]]:
                    # 栈顶就是中间的柱子，主心骨
                    mid_index = stack[-1]
                    stack.pop()
                    if stack:
                        left_index = stack[-1]
                        right_index = i
                        width = right_index - left_index - 1
                        height = heights[mid_index]
                        result = max(result, width * height)
                stack.append(i)
        return result

# 单调栈精简
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)
        stack = [0]
        result = 0
        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                mid_height = heights[stack[-1]]
                stack.pop()
                if stack:
                    # area = width * height
                    area = (i - stack[-1] - 1) * mid_height
                    result = max(area, result)
            stack.append(i)
        return result
