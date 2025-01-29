class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        expectedNums = set(nums)
        nums[:] = sorted(list(expectedNums)) 
        return len(expectedNums)
