"""
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.
"""
class Solution:
    def maxProfit(self, inv: List[int], orders: int) -> int:
        arr=sorted(Counter(inv).items(), reverse=True)+[(0,0)]
        ans, ind, width=0,0,0
        
        while orders>0:
            width += arr[ind][1]
            sell=min(orders, width * (arr[ind][0] - arr[ind+1][0]))
            whole, remainder= divmod(sell, width)
            ans += width*(whole*(arr[ind][0]+arr[ind][0]-(whole-1)))//2 + remainder*(arr[ind][0]-whole)
            orders -= sell
            ind += 1
        return ans % 1_000_000_007
