class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # use a dict to store the elements in nums1 and nums2 and their sum
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashmap:
                    hashmap[n1+n2] += 1
                else:
                    hashmap[n1+n2] = 1
        
        # if the -(a+b) exists in nums3 and nums4, we shall add the count
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                if key in hashmap:
                    count += hashmap[key]
        return count


class Solution:
    def fourSumCount(self, nums1: list, nums2: list, nums3: list, nums4: list) -> int:
        from collections import defaultdict # You may use normal dict instead.
        rec, cnt = defaultdict(lambda : 0), 0
        # To store the summary of all the possible combinations of nums1 & nums2, together with their frequencies.
        for i in nums1:
            for j in nums2:
                rec[i+j] += 1
        # To add up the frequencies if the corresponding value occurs in the dictionary
        for i in nums3:
            for j in nums4:
                cnt += rec.get(-(i+j), 0) # No matched key, return 0.
        return cnt
