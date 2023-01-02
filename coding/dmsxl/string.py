class Solution:
    #1.去除多余的空格
    def trim_spaces(self, s):     
        n=len(s)
        left=0
        right=n-1

        while left<=right and s[left]==' ':    #去除开头的空格
            left+=1
        while left<=right and s[right]==' ':   #去除结尾的空格
            right=right-1
        tmp=[]
        while left<=right:    #去除单词中间多余的空格
            if s[left]!=' ':
                tmp.append(s[left])
            elif tmp[-1]!=' ':   #当前位置是空格，但是相邻的上一个位置不是空格，则该空格是合理的
                tmp.append(s[left])
            left+=1
        return tmp
    #2.翻转字符数组
    def reverse_string(self, nums, left, right):
        while left<right:
            nums[left], nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        return None
    #3.翻转每个单词
    def reverse_each_word(self, nums):
        start=0
        end=0
        n=len(nums)
        while start<n:
            while end<n and nums[end]!=' ':
                end+=1
            self.reverse_string(nums,start,end-1)
            start=end+1
            end+=1
        return None

    #4.翻转字符串里的单词
    def reverseWords(self, s): #测试用例："the sky is blue"
        l = self.trim_spaces(s)   #输出：['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e'
        self.reverse_string(l, 0, len(l)-1)   #输出：['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']
        self.reverse_each_word(l)               #输出：['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']
        return ''.join(l)         #输出：blue is sky the
