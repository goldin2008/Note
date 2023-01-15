class Solution:
    def balancedStringSplit(self, s: str) -> int:
        diff = 0 #右左差值
        ans = 0
        for c in s:
            if c == "L":
                diff -= 1
            else:
                diff += 1
            if diff == 0:
                ans += 1
        return ans
