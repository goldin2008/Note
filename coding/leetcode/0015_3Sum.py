# Python
class Solution:
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        nums.sort()
	# 找出a + b + c = 0
        # a = nums[i], b = nums[left], c = nums[right]
        for i in range(n):
            left = i + 1
            right = n - 1
	    # 排序之后如果第一个元素已经大于零，那么无论如何组合都不可能凑成三元组，直接返回结果就可以了
            if nums[i] > 0: 
                break
            if i >= 1 and nums[i] == nums[i - 1]: # 去重a
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
		    # 去重逻辑应该放在找到一个三元组之后，对b 和 c去重
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
        return ans

# Python (v3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums, res = sorted(nums), []
        for i in range(len(nums) - 2):
            cur, l, r = nums[i], i + 1, len(nums) - 1
            if res != [] and res[-1][0] == cur: continue # Drop duplicates for the first time.

            while l < r:
                if cur + nums[l] + nums[r] == 0:
                    res.append([cur, nums[l], nums[r]])
                    # Drop duplicates for the second time in interation of l & r. Only used when target situation occurs, because that is the reason for dropping duplicates.
                    while l < r - 1 and nums[l] == nums[l + 1]:
                        l += 1
                    while r > l + 1 and nums[r] == nums[r - 1]:
                        r -= 1
                if cur + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return res
