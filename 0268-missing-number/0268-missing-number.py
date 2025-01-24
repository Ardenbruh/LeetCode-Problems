class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = n*(n+1)/2 # this gives 2.0 if u dont type cast the int in the last as its floating point division

        for i in range(len(nums)):
            sum = sum - nums[i]
        
        return int(sum)
        