class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -10**5
        for el in nums:
            curr_sum +=  el
            if max_sum < curr_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum