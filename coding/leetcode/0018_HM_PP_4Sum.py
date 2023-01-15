# 双指针法
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):   
            if i > 0 and nums[i] == nums[i - 1]: continue  # 对nums[i]去重
            for k in range(i+1, n):
                if k > i + 1 and nums[k] == nums[k-1]: continue  # 对nums[k]去重
                p = k + 1
                q = n - 1

                while p < q:
                    if nums[i] + nums[k] + nums[p] + nums[q] > target: q -= 1
                    elif nums[i] + nums[k] + nums[p] + nums[q] < target: p += 1
                    else:
                        res.append([nums[i], nums[k], nums[p], nums[q]])
			# 对nums[p]和nums[q]去重
                        while p < q and nums[p] == nums[p + 1]: p += 1
                        while p < q and nums[q] == nums[q - 1]: q -= 1
                        p += 1
                        q -= 1
        return res


# 哈希表法
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # use a dict to store value:showtimes
        hashmap = dict()
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else: 
                hashmap[n] = 1
        
        # good thing about using python is you can use set to drop duplicates.
        ans = set()
        # ans = []  # save results by list()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = target - (nums[i] + nums[j] + nums[k])
                    if val in hashmap:
                        # make sure no duplicates.
                        count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                        if hashmap[val] > count:
                          ans_tmp = tuple(sorted([nums[i], nums[j], nums[k], val]))
                          ans.add(ans_tmp)
                          # Avoiding duplication in list manner but it cause time complexity increases
                          # if ans_tmp not in ans:  
                          #     ans.append(ans_tmp)
                        else:
                            continue
        return list(ans) 
        # if used list() to save results, just 
        # return ans
