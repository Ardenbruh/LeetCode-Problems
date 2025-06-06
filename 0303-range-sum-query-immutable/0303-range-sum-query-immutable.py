class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix.append(self.prefix[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        
        rSum = self.prefix[right]
        lSum = self.prefix[left-1] if left > 0 else 0

        return rSum - lSum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)