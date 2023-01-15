class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        default_dict1 = defaultdict(str)
        default_dict2 = defaultdict(str)
    
        if len(s) != len(t): return false

        for i in range(len(s)):
            if not default_dict1[s[i]]:
                default_dict1[s[i]] = t[i]
            
            if not default_dict2[t[i]]:
                default_dict2[t[i]] = s[i]

            if default_dict1[s[i]] != t[i] or default_dict2[t[i]] != s[i]:
                return False
            
        return True
