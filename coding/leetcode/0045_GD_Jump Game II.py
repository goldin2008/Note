class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        ans = 0
        curDistance = 0
        nextDistance = 0
        for i in range(len(nums)):
            nextDistance = max(i + nums[i], nextDistance)
            if i == curDistance: 
                if curDistance != len(nums) - 1:
                    ans += 1
                    curDistance = nextDistance
                    if nextDistance >= len(nums) - 1: break
        return ans

# 贪心版本二
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        curDistance, nextDistance = 0, 0
        step = 0
        for i in range(len(nums)-1):
            nextDistance = max(nextDistance, nums[i]+i)
            if i == curDistance:
                curDistance = nextDistance
                step += 1
        return step
