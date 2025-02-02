class Solution:
    def check(self, nums: List[int]) -> bool:

        sort_nums = sorted(nums)
        double_arr = 2*nums
        for i in range(len(nums)):
            if double_arr[i:i + len(nums)] == sort_nums:
                return True
        return False