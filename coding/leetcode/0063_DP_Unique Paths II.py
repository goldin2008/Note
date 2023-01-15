class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 构造一个DP table
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        if dp[0][0] == 0:
            return 0  # 如果第一个格子就是障碍，return 0
        # 第一行
        for i in range(1, col):
            if obstacleGrid[0][i] == 1:
                # 遇到障碍物时，直接退出循环，后面默认都是0
                break
            dp[0][i] = 1

        # 第一列
        for i in range(1, row):
            if obstacleGrid[i][0] == 1:
                # 遇到障碍物时，直接退出循环，后面默认都是0
                break
            dp[i][0] = 1
        # print(dp)

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


class Solution:
    """
    使用一维dp数组
    """

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # 初始化dp数组
        # 该数组缓存当前行
        curr = [0] * n
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            curr[j] = 1
            
        for i in range(1, m): # 从第二行开始
            for j in range(n): # 从第一列开始，因为第一列可能有障碍物
                # 有障碍物处无法通行，状态就设成0
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                elif j > 0:
                    # 等价于
                    # dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    curr[j] = curr[j] + curr[j - 1]
                # 隐含的状态更新
                # dp[i][0] = dp[i - 1][0]
        
        return curr[n - 1]
