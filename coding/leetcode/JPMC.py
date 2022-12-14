# 1. Array Reduction
# https://www.geeksforgeeks.org/minimize-cost-to-reduce-the-array-to-a-single-element-by-given-operations/


# 2. Break a Palindrome (1328)
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b'


# 3. Factors of 3 and 5
# https://leetcode.com/discuss/interview-question/528041/mathworks-edg-new-grad-oa-2020-ideal-numbers-in-a-range
# ideal numbers in a range
def findMultiples(x):
  for x in range(0, x + 1):
    if x % 3 == 0 and x % 5 == 0:
        print(x)

# 4. Selling Products (1481)
# https://www.geeksforgeeks.org/minimum-number-of-distinct-elements-after-removing-m-items/
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/solutions/686335/java-python-3-greedy-alg-3-methods-from-o-nlogn-to-o-n-w-brief-explanation-and-analysis/?orderBy=most_votes
# Minimum number of distinct elements after removing m items
def distinctIds(arr, n, mi):
  m = {}
  v = []
  count = 0
 
  # Store the occurrence of ids
  for i in range(n):
    if arr[i] in m:
      m[arr[i]] += 1
    else:
      m[arr[i]] = 1
 
  # Store into the list value as key and vice-versa
  for i in m:
    v.append([m[i],i])
 
  v.sort()
  size = len(v)
 
  # Start removing elements from the beginning
  for i in range(size):
     
    # Remove if current value is less than
    # or equal to mi
    if (v[i][0] <= mi):
      mi -= v[i][0]
      count += 1
         
    else:   # Return the remaining size
      return size - count
  return size - count


# 5. Longest Even Length Word


# 6. Missing Words


# 7. Highly Profitable Months
# https://leetcode.com/discuss/interview-question/1400404/bridge-water-assoc-oa-number-of-strinctly-increasing-subarrays-of-size-k-in-an-array
def numIncreaseSubarray(nums, k):
    size = len(nums)
    if k==0 or k>size:
        return 0

    # Build preCompute array
    preCompute = [1] * size
    i = 0
    while i < size-1:
        # check the edge case at the end
        curr = 0
        if nums[i+1] > nums[i]:
            curr += 1
        else:
            preCompute[i-curr] = curr+1
            curr = 0
        i += 1
    
    # Generate number of strictly increaing subarrays
    ans = 0
    for i in range(size):
        if preCompute[i] != 1 and preCompute[i] >= k:
            ans += preCompute[i] - k + 1

    return ans


# 8. Subarray Sum
# https://www.geeksforgeeks.org/sum-of-all-subarrays/


# 9. Maximum Index
# https://www.geeksforgeeks.org/maximum-index-a-pointer-can-reach-in-n-steps-by-avoiding-a-given-index-b/
def maximumIndex(N, B):
    max_index = 0
    # Calculate maximum possible
    # index that can be reached
    for i in range(1, N + 1):
        max_index += i
    current_index = max_index
    step = N
 
    while (1): 
        # Check if current index and step
        # both are greater than 0 or not
        while (current_index > 0 and N > 0):
            # Decrement current_index by step
            current_index -= N
            # Check if current index is
            # equal to B or not
            if (current_index == B):
                # Restore to previous index
                current_index += N
            # Decrement step by one
            N -= 1 
        # If it reaches the 0th index
        if (current_index <= 0):
            # Print result
            print(max_index)
            break
 
        # If max index fails to
        # reach the 0th index
        else:
            N = step
            # Store max_index - 1 in current index
            current_index = max_index - 1
            # Decrement max index
            max_index -= 1
            # If current index is equal to B
            if (current_index == B):
                current_index = max_index - 1 
                # Decrement current index
                max_index -= 1


# 10. 计算Fibonachi number (509)
# 我用的带golden ratio的数学公式，时间复杂度是O(log n), 空间复杂度是O(1)
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)

# Bottom-Up Approach using Tabulation
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        
        cache = [0] * (N + 1)
        cache[1] = 1
        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[N]

# Top-Down Approach using Memoization
class Solution:
    cache = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]

# Iterative Bottom-Up Approach
class Solution:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N

        current = 0
        prev1 = 1
        prev2 = 0

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current



# 11. Game Winner (2038)
# Remove Colored Pieces if Both Neighbors are the Same Color
class Solution:
    def winnerOfGame(self, s: str) -> bool:
        
        a = b = 0
        
        for i in range(1,len(s)-1):
            if s[i-1] == s[i] == s[i+1]:
                if s[i] == 'A':
                    a += 1
                else:
                    b += 1
                    
        return a>b



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
# Reaching Points
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy


# 14. Rearranging a Word (556)
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 1
        # print(bin(1<<31))
        while i-1 >= 0 and digits[i] <= digits[i-1]:
            i -= 1
            
        if i == 0: return -1
        
        j = i
        while j+1 < len(digits) and digits[j+1] > digits[i-1]:
            j += 1
        
        digits[i-1], digits[j] = digits[j], digits[i-1]
        digits[i:] = digits[i:][::-1]
        ret = int(''.join(digits))
        
        return ret if ret < 1<<31 else -1


# 15. Lottery Coupons


# 16. Self Descriptive Number (728)
# https://www.geeksforgeeks.org/self-descriptive-number/
class Solution:
    def selfDividingNumbers(self, left, right):
        def self_dividing(n):
            for d in str(n):
                if d == '0' or n % int(d) > 0:
                    return False
            return True
        """
        Alternate implementation of self_dividing:
        def self_dividing(n):
            x = n
            while x > 0:
                x, d = divmod(x, 10)
                if d == 0 or n % d > 0:
                    return False
            return True
        """
        ans = []
        for n in range(left, right + 1):
            if self_dividing(n):
                ans.append(n)
        return ans #Equals filter(self_dividing, range(left, right+1))


# 17. Coin Change (322) 
# Find minimum number of coins that make a given value
# https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
# https://www.enjoyalgorithms.com/blog/minimum-coin-change
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 

# m is size of coins array (number of
# different coins)
def minCoins(coins, m, V):
     
    # table[i] will be storing the minimum
    # number of coins required for i value.
    # So table[V] will have result
    table = [0 for i in range(V + 1)]
 
    # Base case (If given value V is 0)
    table[0] = 0
 
    # Initialize all table values as Infinite
    for i in range(1, V + 1):
        table[i] = sys.maxsize
 
    # Compute minimum coins required
    # for all values from 1 to V
    for i in range(1, V + 1):
         
        # Go through all coins smaller than i
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                    sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
     
    if table[V] == sys.maxsize:
        return -1
       
    return table[V]


# 18. Distinct Digit Numbers


# 19. Balanced or Not


# 20. Fun with Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
            print(ans)
        return ans.values()

# 21. Jumbled Numbers (423)
class Solution:
    def originalDigits(self, s: str) -> str:
        # building hashmap letter -> its frequency
        count = collections.Counter(s)
        
        # building hashmap digit -> its frequency 
        out = {}
        # letter "z" is present only in "zero"
        out["0"] = count["z"]
        # letter "w" is present only in "two"
        out["2"] = count["w"]
        # letter "u" is present only in "four"
        out["4"] = count["u"]
        # letter "x" is present only in "six"
        out["6"] = count["x"]
        # letter "g" is present only in "eight"
        out["8"] = count["g"]
        # letter "h" is present only in "three" and "eight"
        out["3"] = count["h"] - out["8"]
        # letter "f" is present only in "five" and "four"
        out["5"] = count["f"] - out["4"]
        # letter "s" is present only in "seven" and "six"
        out["7"] = count["s"] - out["6"]
        # letter "i" is present in "nine", "five", "six", and "eight"
        out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
        # letter "n" is present in "one", "nine", and "seven"
        out["1"] = count["n"] - out["7"] - 2 * out["9"]

        # building output string
        output = [key * out[key] for key in sorted(out.keys())]
        return "".join(output)


# 22. Minimum flips required to form given binary string where every flip changes all bits to its right as well
# https://www.geeksforgeeks.org/minimum-flips-required-to-form-given-binary-string-where-every-flip-changes-all-bits-to-its-right-as-well/

