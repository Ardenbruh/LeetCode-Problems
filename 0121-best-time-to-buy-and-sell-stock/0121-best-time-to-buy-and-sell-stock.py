class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = 99999999
        for price in prices:
            maxprofit = max(maxprofit,price-minprice)
            minprice = min(minprice, price)
        return maxprofit