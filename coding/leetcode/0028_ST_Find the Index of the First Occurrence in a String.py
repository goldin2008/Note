"""
https://www.xdull.cn/kmp.html



"""
# //暴力解法：
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        for i in range(m):
            if haystack[i:i+n] == needle:
                return i
        return -1   


# // 方法一
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        next = self.getnext(a,needle)
        p=-1
        for j in range(b):
            while p >= 0 and needle[p+1] != haystack[j]:
                p = next[p]
            if needle[p+1] == haystack[j]:
                p += 1
            if p == a-1:
                return j-a+1
        return -1

    def getnext(self,a,needle):
        next = ['' for i in range(a)]
        k = -1
        next[0] = k
        for i in range(1, len(needle)):
            while (k > -1 and needle[k+1] != needle[i]):
                k = next[k]
            if needle[k+1] == needle[i]:
                k += 1
            next[i] = k
        return next


# // 方法二
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        i = j = 0
        next = self.getnext(a, needle)
        while(i < b and j < a):
            if j == -1 or needle[j] == haystack[i]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == a:
            return i-j
        else:
            return -1

    def getnext(self, a, needle):
        next = ['' for i in range(a)]
        j, k = 0, -1
        next[0] = k
        while(j < a-1):
            if k == -1 or needle[k] == needle[j]:
                k += 1
                j += 1
                next[j] = k
            else:
                k = next[k]
        return next
