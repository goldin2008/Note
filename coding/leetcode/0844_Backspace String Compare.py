class Solution:

    def get_string(self, s: str) -> str :
        bz = []
        for i in range(len(s)) :
            c = s[i]
            if c != '#' :
                bz.append(c) # 模拟入栈
            elif len(bz) > 0: # 栈非空才能弹栈
                bz.pop() # 模拟弹栈
        return str(bz)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.get_string(s) == self.get_string(t)
        pass

# 双指针
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_index, t_index = len(s) - 1, len(t) - 1
        s_backspace, t_backspace = 0, 0 # 记录s,t的#数量
        while s_index >= 0 or t_index >= 0: # 使用or，以防长度不一致
            while s_index >= 0: # 从后向前，消除s的#
                if s[s_index] == '#':
                    s_index -= 1
                    s_backspace += 1
                else:
                    if s_backspace > 0:
                        s_index -= 1
                        s_backspace -= 1
                    else:
                        break
            while t_index >= 0: # 从后向前，消除t的#
                if t[t_index] == '#':
                    t_index -= 1
                    t_backspace += 1
                else:
                    if t_backspace > 0:
                        t_index -= 1
                        t_backspace -= 1
                    else:
                        break
            if s_index >= 0 and t_index >= 0: # 后半部分#消除完了，接下来比较当前位的值
                if s[s_index] != t[t_index]:
                    return False
            elif s_index >= 0 or t_index >= 0: # 一个字符串找到了待比较的字符，另一个没有，返回False
                return False
            s_index -= 1
            t_index -= 1
        return True
