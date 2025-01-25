class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {nums[i]: i for i in range(len(nums))}
        
        for i in range(len(nums)):
            x = target - nums[i]
            if x in d and i != d[x]:
                return [i, d[x]]