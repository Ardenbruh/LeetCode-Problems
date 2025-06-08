class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [num for num, count in Counter(nums).items() if count == 2]
        