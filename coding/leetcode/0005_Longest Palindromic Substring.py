class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        maxlenth = 0
        left = 0
        right = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[j] == s[i]:
                    if j - i <= 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                if dp[i][j] and j - i + 1 > maxlenth:
                    maxlenth = j - i + 1
                    left = i
                    right = j
        return s[left:right + 1]

双指针：

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def find_point(i, j, s):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j

        def compare(start, end, left, right):
            if right - left > end - start:
                return left, right
            else:
                return start, end

        start = 0
        end = 0
        for i in range(len(s)):
            left, right = find_point(i, i, s)
            start, end = compare(start, end, left, right)

            left, right = find_point(i, i + 1, s)
            start, end = compare(start, end, left, right)
        return s[start:end]
