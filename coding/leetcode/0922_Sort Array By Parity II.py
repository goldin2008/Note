#方法2
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        evenIndex = 0
        oddIndex = 1
        for i in range(len(nums)):
            if nums[i] % 2: #奇数
                result[oddIndex] = nums[i]
                oddIndex += 2
            else: #偶数
                result[evenIndex] = nums[i]
                evenIndex += 2
        return result

#方法3
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        oddIndex = 1
        for i in range(0,len(nums),2): #步长为2
            if nums[i] % 2: #偶数位遇到奇数
                while  nums[oddIndex] % 2: #奇数位找偶数
                    oddIndex += 2
                nums[i], nums[oddIndex] = nums[oddIndex], nums[i]
        return nums
