# 贪心
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        preC,curC,res = 0,0,1  #题目里nums长度大于等于1，当长度为1时，其实到不了for循环里去，所以不用考虑nums长度
        for i in range(len(nums) - 1):
            curC = nums[i + 1] - nums[i]
            if curC * preC <= 0 and curC !=0:  #差值为0时，不算摆动
                res += 1
                preC = curC  #如果当前差值和上一个差值为一正一负时，才需要用当前差值替代上一个差值
        return res


# 动态规划
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 0 i 作为波峰的最大长度
        # 1 i 作为波谷的最大长度
        # dp是一个列表，列表中每个元素是长度为 2 的列表
        dp = []
        for i in range(len(nums)):
            # 初始为[1, 1]
            dp.append([1, 1])
            for j in range(i):
                # nums[i] 为波谷
                if nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
                # nums[i] 为波峰 
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
        return max(dp[-1][0], dp[-1][1])


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # up i作为波峰最长的序列长度
	# down i作为波谷最长的序列长度
        n = len(nums)
	# 长度为0和1的直接返回长度
	if n<2: return n
        for i in range(1,n):
            if nums[i]>nums[i-1]:
	    # nums[i] 为波峰，1. 前面是波峰，up值不变，2. 前面是波谷，down值加1
	    # 目前up值取两者的较大值(其实down+1即可，可以推理前一步down和up最多相差1，所以down+1>=up)
                up = max(up, down+1)
            elif nums[i]<nums[i-1]:
	    # nums[i] 为波谷，1. 前面是波峰，up+1，2. 前面是波谷，down不变，取较大值
                down = max(down, up+1)
        return max(up, down)
