class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # expectedNums = set(nums)
        # nums[:] = sorted(list(expectedNums))
        # return len(expectedNums)
        # Time Complexity - O(nlogn)

        write_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index

        #Time Complexity - O(n)
