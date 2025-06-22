class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = [el for el in prices]
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    res[i] -= prices[j]
                    break
        return res
