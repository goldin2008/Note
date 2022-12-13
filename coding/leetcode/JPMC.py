# 1. Array Reduction
# https://www.geeksforgeeks.org/minimize-cost-to-reduce-the-array-to-a-single-element-by-given-operations/


# 2. Break a Palindrome


# 3. Factors of 3 and 5


# 4. Selling Products


# 5. Longest Even Length Word


# 6. Missing Words


# 7. Highly Profitable Months
# https://leetcode.com/discuss/interview-question/1400404/bridge-water-assoc-oa-number-of-strinctly-increasing-subarrays-of-size-k-in-an-array


# 8. Subarray Sum
# https://www.geeksforgeeks.org/sum-of-all-subarrays/


# 9. Maximum Index


# 10. 计算Fibonachi number (509)
# 我用的带golden ratio的数学公式，时间复杂度是O(log n), 空间复杂度是O(1)
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)



# 11. Game Winner


# 12. Cardinality Sorting (1356)
# https://www.geeksforgeeks.org/sort-array-according-count-set-bits/

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda num : (sum((num >> i) & 1 for i in range(32)), num))

# Function to count setbits
def setBitCount(num):
    count = 0
    while (num):
        if (num & 1):
            count += 1
        num = num >> 1          
    return count

# Function to count setbits
def countSetBits(val):
    cnt = 0
    while val:
        cnt += val % 2
        val = val//2
    return cnt

sorted_arr = sorted(arr, key=lambda val: (
    countSetBits(val[0]), n-val[1]), reverse=True)
sorted_arr = [val[0] for val in sorted_arr]


# 13. Is Possible (780)


# 14. Rearranging a Word (556)


# 15. Lottery Coupons


# 16. Self Descriptive Number
# https://www.geeksforgeeks.org/self-descriptive-number/



# 17. Find minimum number of coins that make a given value
# https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
# https://www.enjoyalgorithms.com/blog/minimum-coin-change



# 18. Distinct Digit Numbers


# 19. Balanced or Not
