"""
01背包中二维dp数组的两个for遍历的先后循序是可以颠倒了，
一维dp数组的两个for循环先后循序一定是先遍历物品，再遍历背包容量。
在完全背包中，对于一维dp数组来说，其实两个for循环嵌套顺序是无所谓的!
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        # 遍历物品
        for i in range(len(coins)):
            # 遍历背包
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]
