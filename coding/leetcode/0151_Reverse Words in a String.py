class Solution:
  #1.去除多余的空格
        def trim_spaces(self, s):     
            n = len(s)
            left = 0
            right = n-1
        
            while left <= right and s[left] == ' ':    #去除开头的空格
                left += 1
            while left <= right and s[right] == ' ':   #去除结尾的空格
                right = right-1
            tmp = []
            while left <= right:                      #去除单词中间多余的空格
                if s[left] != ' ':
                    tmp.append(s[left])
                elif tmp[-1] != ' ':                 #当前位置是空格，但是相邻的上一个位置不是空格，则该空格是合理的
                    tmp.append(s[left])
                left += 1
            return tmp
	    
 #2.翻转字符数组
        def reverse_string(self, nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return None
	    
 #3.翻转每个单词
        def reverse_each_word(self, nums):
            start = 0
            end = 0
            n = len(nums)
            while start < n:
                while end < n and nums[end] != ' ':
                    end += 1
                self.reverse_string(nums, start, end-1)
                start = end + 1
                end += 1
            return None

#4.翻转字符串里的单词
        def reverseWords(self, s):                #测试用例："the sky is blue"
            l = self.trim_spaces(s)               #输出：['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e'
            self.reverse_string(l,  0, len(l)-1)  #输出：['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']
            self.reverse_each_word(l)             #输出：['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']
            return ''.join(l)                    #输出：blue is sky the


class Solution:
    def reverseWords(self, s: str) -> str:
        # method 1 - Rude but work & efficient method.
        s_list = [i for i in s.split(" ") if len(i) > 0]
        return " ".join(s_list[::-1])

        # method 2 - Carlo's idea
        def trim_head_tail_space(ss: str):
            p = 0
            while p < len(ss) and ss[p] == " ":
                p += 1
            return ss[p:]

        # Trim the head and tail space
        s = trim_head_tail_space(s)
        s = trim_head_tail_space(s[::-1])[::-1]

        pf, ps, s = 0, 0, s[::-1] # Reverse the string.
        while pf < len(s):
            if s[pf] == " ":
                # Will not excede. Because we have clean the tail space.
                if s[pf] == s[pf + 1]:
                    s = s[:pf] + s[pf + 1:]
                    continue
                else:
                    s = s[:ps] + s[ps: pf][::-1] + s[pf:]
                    ps, pf = pf + 1, pf + 2
            else:
                pf += 1
        return s[:ps] + s[ps:][::-1] # Must do the last step, because the last word is omit though the pointers are on the correct positions,
