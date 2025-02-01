class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        # fil = []
        # for num in nums:
        #     if num % 2 == 0:
        #         fil.append(True)
        #     else:
        #         fil.append(False)

        # for j in range(1, len(fil)):
        #     if fil[j] == fil[j-1]:
        #         return False
        # return True

        if len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            if nums[i] % 2 == nums[i+1] % 2:
                return False 
        return True