class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # n = len(nums)
        # prefixSum = [0] * (n+1)
        # for i in range(1, n+1):
        #     prefixSum[i] = prefixSum[i-1] + nums[i-1]
        
        # for i in range(n+1):
        #     for j in range(i+2, n+1): 
        #         subarray_sum = prefixSum[j] - prefixSum[i]
        #         if subarray_sum % k == 0:
        #             return True
        # return False
        remidx = {0:-1}
        total = 0
        for i, el in enumerate(nums):
            total += el
            rem = total%k
            if rem not in remidx:
                remidx[rem] = i
            elif i - remidx[rem] > 1:
                return True
        return False