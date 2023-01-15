class Solution: # 贪心思路
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minPrice: # 此时有更低的价格，可以买入
                minPrice = prices[i]
            elif prices[i] > (minPrice + fee): # 此时有利润，同时假买入高价的股票，看看是否继续盈利
                result += prices[i] - (minPrice + fee)
                minPrice = prices[i] - fee
            else: # minPrice<= prices[i] <= minPrice + fee， 价格处于minPrice和minPrice+fee之间，不做操作
                continue
        return result
