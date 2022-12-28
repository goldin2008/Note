# Python写法一（使用数组作为哈希表）
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        arr = [0] * 26

        for x in magazine:    # 记录 magazine里各个字符出现次数
            arr[ord(x) - ord('a')] += 1

        for x in ransomNote:  # 在arr里对应的字符个数做--操作
            if arr[ord(x) - ord('a')] == 0:  # 如果没有出现过直接返回
                return False
            else:
                arr[ord(x) - ord('a')] -= 1
        
        return True

# Python写法二（使用defaultdict）
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        from collections import defaultdict

        hashmap = defaultdict(int)

        for x in magazine:
            hashmap[x] += 1

        for x in ransomNote:
            value = hashmap.get(x)
            if value is None or value == 0:
                return False
            else:
                hashmap[x] -= 1

        return True

# Python写法三
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        # use a dict to store the number of letter occurance in ransomNote
        hashmap = dict()
        for s in ransomNote:
            if s in hashmap:
                hashmap[s] += 1
            else:
                hashmap[s] = 1
        
        # check if the letter we need can be found in magazine
        for l in magazine:
            if l in hashmap:
                hashmap[l] -= 1
        
        for key in hashmap:
            if hashmap[key] > 0:
                return False
        
        return True

# Python写法四
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        x = c1 - c2
        #x只保留值大于0的符号，当c1里面的符号个数小于c2时，不会被保留
        #所以x只保留下了，magazine不能表达的
        if(len(x)==0):
            return True
        else:
            return False
