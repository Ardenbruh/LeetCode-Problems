class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        sum = n*(n+1)//2
        for i in nums:
            sum -= i
        return sum

        
        # n = len(nums)
        # result = 0

        # for i in nums:
        #     result ^= i 

        # for i in range(n + 1):
        #     result ^= i  

        # return result