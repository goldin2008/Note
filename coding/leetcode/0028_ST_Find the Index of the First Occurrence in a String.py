"""
https://www.xdull.cn/kmp.html

https://binary-baba.medium.com/string-matching-kmp-algorithm-27c182efa387
https://www.zhihu.com/question/21923021
https://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
https://juejin.cn/post/7061562409202221092
https://writings.sh/post/algorithm-string-searching-kmp
https://doc.yonyoucloud.com/doc/wiki/project/kmp-algorithm/define.html
https://towardsdatascience.com/pattern-search-with-the-knuth-morris-pratt-kmp-algorithm-8562407dba5b
"""
# 暴力解法：
class Solution:
    def strStr(self, text: str, pattern: str) -> int:
        n1,n2=len(text),len(pattern)
        if n2==0:
            return 0
        i,j=0,0
        while i<n1:
            if text[i]==pattern[j]:  #相等时同时移动
                i+=1
                j+=1
            else:
                i-=j   #回到最开始匹配的位置
                i+=1   #向右移动一格
                j=0    #j回到位置0
            if j==n2:          #到达字符串末尾，说明匹配成功，返回结果
                return i-n2
        return -1
    
# KMP
class Solution:
    def strStr(self, text: str, patten: str) -> int:
        next=self.KMP(patten)       #获取next数组
        n1,n2=len(text),len(patten)
        if n2==0:
            return 0
        i,j=0,0
        while i<n1:
            if text[i]==patten[j]:
                i+=1
                j+=1
            else:
                if j>0:
                    j=next[j-1]
                else:
                    i+=1
            if j==n2:
                return i-n2
        return -1

    def KMP(self, patten):
        if not patten:
            return []
        n=len(patten)
        next=[0]*n
        i,j=1,0
        while i<n:
            if patten[i]==patten[j]:
                next[i]=j+1
                i+=1
                j+=1
            else:
                if j>0:
                    j=next[j-1]
                else:
                    next[i]=0
                    i+=1
        return next

# From dmslx
# 暴力解法：
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


# 方法一
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


# 方法二
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
