class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # res = [el for el in prices]
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] <= prices[i]:
        #             res[i] -= prices[j]
        #             break
        # return res

        res = prices[:]
        stack = []

        for i, el in enumerate(prices):
            while stack and res[stack[-1]] >= el:
                res[stack.pop()] -= el
            stack.append(i)
        return res
            