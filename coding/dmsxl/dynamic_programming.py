"""
动态规划方法总结:

1. 确定dp数组（dp table）以及下标的含义
2. 确定递推公式
3. dp数组如何初始化
4. 确定遍历顺序
5. 举例推导dp数组

01背包:
二维数组，外层内层遍历可以交换，都是从小到大遍历
一维数组，外层物品从小到大，内层容量从大到小，遍历不可交换

完全背包:
纯完全背包（求是否能装满背包）
先遍历物品，再遍历背包 与 先遍历背包，再遍历物品都是可以的，都要从小到大去遍历

非纯完全背包（求装满背包有几种方法）
一维数组 (组合问题)，外层物品从小到大，内层容量从小到大，遍历不可交换
一维数组 (排列问题)，外层容量从小到大，内层物品从小到大，遍历不可交换
(DP方法求的是排列总和，而且仅仅是求排列总和的个数，并不是把所有的排列都列出来。
如果要把排列都列出来的话，只能使用回溯算法爆搜。)
"""

"""
01背包: 每件物品只能用一次
完全背包: 商品可以重复多次放入
多重背包
分组背包

对于背包问题其实状态都是可以压缩的。
在使用二维数组的时候，递推公式: 
dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i]);
其实可以发现如果把dp[i - 1]那一层拷贝到dp[i]上，表达式完全可以是: 
dp[i][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i]);
与其把dp[i - 1]这一层拷贝到dp[i]上，不如只用一个一维数组了，只用dp[j]（一维数组，也可以理解是一个滚动数组）。
这就是滚动数组的由来，需要满足的条件是上一层可以重复利用，直接拷贝到当前层。
读到这里估计大家都忘了 dp[i][j]里的i和j表达的是什么了，i是物品，j是背包容量。
dp[i][j] 表示从下标为[0-i]的物品里任意取，放进容量为j的背包，价值总和最大是多少

dp[j]可以通过dp[j - weight[i]]推导出来，dp[j - weight[i]]表示容量为j - weight[i]的背包所背的最大价值。
dp[j - weight[i]] + value[i] 表示 容量为 j - 物品i重量 的背包 加上 物品i的价值。
也就是容量为j的背包，放入物品i了之后的价值即:dp[j]）、
此时dp[j]有两个选择，一个是取自己dp[j] 相当于 二维dp数组中的dp[i-1][j]，即不放物品i
一个是取dp[j - weight[i]] + value[i]，即放物品i，指定是取最大的，毕竟是求最大价值，
dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);


01背包二维dp数组在遍历顺序上，外层遍历物品 ，内层遍历背包容量 和 外层遍历背包容量 ，内层遍历物品 都是可以的!
如果使用一维dp数组，物品遍历的for循环放在外层，遍历背包的for循环放在内层，且内层for循环倒序遍历!
二维dp遍历的时候，背包容量是从小到大，而一维dp遍历的时候，背包是从大到小。

1. 倒序遍历是为了保证物品i只被放入一次!
2. 为什么二维dp数组历的时候不用倒序呢？
因为对于二维dp，dp[i][j]都是通过上一层即dp[i - 1][j]计算而来，本层的dp[i][j]并不会被覆盖!
3. 对于一维dp，倒序遍历的原因是，本质上还是一个对二维数组的遍历，并且右下角的值依赖上一层左上角的值，
因此需要保证左边的值仍然是上一层的，从右向左覆盖。
4. 两个嵌套for循环的顺序，代码中是先遍历物品嵌套遍历背包容量，那可不可以先遍历背包容量嵌套遍历物品呢？不可以!
因为一维dp的写法，背包容量一定是要倒序遍历，如果遍历背包容量放在上一层，那么每个dp[j]就只会放入一个物品，即:背包里只放入了一个物品。
5. 一维dp数组在推导的时候一定是取价值最大的数, 首先dp[0]一定是0
如果题目给的价值都是正整数那么非0下标都初始化为0就可以了，如果题目给的价值有负数，那么非0下标就要初始化为负无穷。
因为重量都不会是负数，所以dp[j]都初始化为0就可以了，
这样在递归公式dp[j] = max(dp[j], dp[j - weights[i]] + values[i])中dp[j]才不会初始值所覆盖。
因为如果按照二维dp数组那样来初始化第一row，那么背包容量后序遍历的时候，同一个物品i会放两次。
"""
# 二维dp
def test_2_wei_bag_problem1(bag_size, weight, value) -> int: 
	rows, cols = len(weight), bag_size + 1
	dp = [[0 for _ in range(cols)] for _ in range(rows)]
    
	# 初始化dp数组. 
	for i in range(rows): 
		dp[i][0] = 0
	first_item_weight, first_item_value = weight[0], value[0]
	for j in range(1, cols): 	
		if first_item_weight <= j: 
			dp[0][j] = first_item_value

	# 更新dp数组: 先遍历物品, 再遍历背包. 
	for i in range(1, len(weight)): 
		cur_weight, cur_val = weight[i], value[i]
		for j in range(1, cols): 
			if cur_weight > j: # 说明背包装不下当前物品. 
				dp[i][j] = dp[i - 1][j] # 所以不装当前物品. 
			else: 
				# 定义dp数组: dp[i][j] 前i个物品里，放进容量为j的背包，价值总和最大是多少。
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight]+ cur_val)

	print(dp)

if __name__ == "__main__": 
	bag_size = 4
	weight = [1, 3, 4]
	value = [15, 20, 30]
	test_2_wei_bag_problem1(bag_size, weight, value)

# 一维dp
def test_1_wei_bag_problem():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4
    # 初始化: 全为0
    dp = [0] * (bag_weight + 1)

    # 先遍历物品, 再遍历背包容量
    for i in range(len(weight)):
        for j in range(bag_weight, weight[i] - 1, -1):
            # 递归公式
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp)

test_1_wei_bag_problem()


"""
01背包中二维dp数组的两个for遍历的先后循序是可以颠倒了，
一维dp数组的两个for循环先后循序一定是先遍历物品，再遍历背包容量。
在完全背包中，对于一维dp数组来说，其实两个for循环嵌套顺序是无所谓的!
"""
# 先遍历物品，再遍历背包
def test_complete_pack1():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4

    dp = [0]*(bag_weight + 1)

    for i in range(len(weight)):
        for j in range(weight[i], bag_weight + 1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    
    print(dp[bag_weight])

# 先遍历背包，再遍历物品
def test_complete_pack2():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4

    dp = [0]*(bag_weight + 1)

    for j in range(bag_weight + 1):
        for i in range(len(weight)):
            if j >= weight[i]: dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    
    print(dp[bag_weight])

if __name__ == '__main__':
    test_complete_pack1()
    test_complete_pack2()


"""
完全背包和01背包问题唯一不同的地方就是，每种物品有无限件。
我们知道01背包内嵌的循环是从大到小遍历，为了保证每个物品仅被添加一次。
而完全背包的物品是可以添加多次的，所以要从小到大去遍历

内外循环遍历顺序:
01背包中: 二维dp数组的两个for遍历的先后循序是可以颠倒了，一维dp数组的两个for循环先后循序一定是先遍历物品，再遍历背包容量。
完全背包中: 对于一维dp数组来说，其实两个for循环嵌套顺序是无所谓的!

如果求组合数就是外层for循环遍历物品，内层for遍历背包。
如果求排列数就是外层for遍历背包，内层for循环遍历物品。

又可以出一道面试题了，就是纯完全背包，要求先用二维dp数组实现，然后再用一维dp数组实现，
最后在问，两个for循环的先后是否可以颠倒？为什么？ 这个简单的完全背包问题，估计就可以难住不少候选人了。
"""
# 01背包的核心代码
for (int i = 0; i < weight.size(); i++) { // 遍历物品
    for(int j = bagWeight; j >= weight[i]; j--) { // 遍历背包容量
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);
    }
}

# 完全背包核心代码
# // 先遍历物品，再遍历背包
for(int i = 0; i < weight.size(); i++) { // 遍历物品
    for(int j = weight[i]; j <= bagWeight ; j++) { // 遍历背包容量
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);

    }
}

# // 先遍历背包，再遍历物品
for(int j = 0; j <= bagWeight; j++) { // 遍历背包容量
    for(int i = 0; i < weight.size(); i++) { // 遍历物品
        if (j - weight[i] >= 0) dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);
    }
    cout << endl;
}



#1 509. 斐波那契数
# 斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是： F(0) = 0，F(1) = 1 F(n) = F(n - 1) + F(n - 2)，其中 n > 1 给你n ，请计算 F(n) 。
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b, c = 0, 1, 0
        for i in range(1, n):
            c = a + b
            a, b = b, c
        return c
# 递归实现
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


#2 70. 爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。
# 空间复杂度为O(n)版本
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] 为第 i 阶楼梯有多少种方法爬到楼顶
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
# 空间复杂度为O(1)版本
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            tmp=dp[0]+dp[1]
            dp[0]=dp[1]
            dp[1]=tmp
        return dp[1]


#3 ??? 746. 使用最小花费爬楼梯
# 数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
# 每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。
# 请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
# 示例 1：输入：cost = [10, 15, 20] 输出：15 解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
# 示例 2：输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] 输出：6 解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[len(cost) - 1], dp[len(cost) - 2])


#4 62.不同路径
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 问总共有多少条不同的路径？
# 输入：m = 3, n = 7
# 输出：28
class Solution: # 动态规划
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]


#5 63. 不同路径 II
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
"""
但就算是做过62.不同路径，在做本题也会有感觉遇到障碍无从下手。
其实只要考虑到，遇到障碍dp[i][j]保持0就可以了。
也有一些小细节，例如: 初始化的部分，很容易忽略了障碍之后应该都是0的情况。
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 构造一个DP table
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        if dp[0][0] == 0: return 0  # 如果第一个格子就是障碍，return 0
        # 第一行
        for i in range(1, col):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]

        # 第一列
        for i in range(1, row):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
        print(dp)

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


#6 ??? 343. 整数拆分
# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
# 示例 1:
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 示例 2:
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 说明: 你可以假设 n 不小于 2 且不大于 58
# dp[i] = max(dp[i], dp[i - j] * dp[j])
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            # 假设对正整数 i 拆分出的第一个正整数是 j（1 <= j < i），则有以下两种方案：
            # 1) 将 i 拆分成 j 和 i−j 的和，且 i−j 不再拆分成多个正整数，此时的乘积是 j * (i-j)
            # 2) 将 i 拆分成 j 和 i−j 的和，且 i−j 继续拆分成多个正整数，此时的乘积是 j * dp[i-j]
            for j in range(1, i - 1):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]


#7 ??? 96.不同的二叉搜索树
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
# dp[i] += dp[j - 1] * dp[i - j]
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]


#8 01 背包
# 有n件物品和一个最多能背重量为w 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。
# dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
# 大家可以看出，虽然两个for循环遍历的次序不同，但是dp[i][j]所需要的数据就是左上角，根本不影响dp[i][j]公式的推导！
# 其实背包问题里，两个for循环的先后循序是非常有讲究的，理解遍历顺序其实比理解推导公式难多了。
def test_2_wei_bag_problem1(bag_size, weight, value) -> int: 
	rows, cols = len(weight), bag_size + 1
	dp = [[0 for _ in range(cols)] for _ in range(rows)]
    
	# 初始化dp数组. 
	for i in range(rows): 
		dp[i][0] = 0
	first_item_weight, first_item_value = weight[0], value[0]
	for j in range(1, cols): 	
		if first_item_weight <= j: 
			dp[0][j] = first_item_value

	# 更新dp数组: 先遍历物品, 再遍历背包. 
	for i in range(1, len(weight)): 
		cur_weight, cur_val = weight[i], value[i]
		for j in range(1, cols): 
			if cur_weight > j: # 说明背包装不下当前物品. 
				dp[i][j] = dp[i - 1][j] # 所以不装当前物品. 
			else: 
				# 定义dp数组: dp[i][j] 前i个物品里，放进容量为j的背包，价值总和最大是多少。
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight]+ cur_val)

	print(dp)


if __name__ == "__main__": 
	bag_size = 4
	weight = [1, 3, 4]
	value = [15, 20, 30]
	test_2_wei_bag_problem1(bag_size, weight, value)


#9 ？？？ 01 背包(滚动数组)
# 把i相关的部分去掉
# dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
# 二维dp遍历的时候，背包容量是从小到大，而一维dp遍历的时候，背包是从大到小。
# 倒序遍历是为了保证物品i只被放入一次！。但如果一旦正序遍历了，那么物品0就会被重复加入多次！
def test_1_wei_bag_problem():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4
    # 初始化: 全为0
    dp = [0] * (bag_weight + 1)

    # 先遍历物品, 再遍历背包容量
    for i in range(len(weight)):
        for j in range(bag_weight, weight[i] - 1, -1):
            # 递归公式
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp)

test_1_wei_bag_problem()


#10 ??? 416. 分割等和子集
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 注意: 每个数组中的元素不会超过 100 数组的大小不会超过 200
# 示例 1: 输入: [1, 5, 11, 5] 输出: true 解释: 数组可以分割成 [1, 5, 5] 和 [11].
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1: return False
        target //= 2
        # // 总和不会大于20000，背包最大只需要其中一半，所以10001大小就可以了
        dp = [0] * 10001
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        return target == dp[target]


