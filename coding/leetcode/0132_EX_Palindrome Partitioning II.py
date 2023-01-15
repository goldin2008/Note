class Solution:
    def minCut(self, s: str) -> int:

        isPalindromic=[[False]*len(s) for _ in range(len(s))]

        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i]!=s[j]:
                    isPalindromic[i][j] = False
                elif  j-i<=1 or isPalindromic[i+1][j-1]:
                    isPalindromic[i][j] = True

        # print(isPalindromic)
        dp=[sys.maxsize]*len(s)
        dp[0]=0

        for i in range(1,len(s)):
            if isPalindromic[0][i]:
                dp[i]=0
                continue
            for j in range(0,i):
                if isPalindromic[j+1][i]==True:
                    dp[i]=min(dp[i], dp[j]+1)
        return dp[-1]
