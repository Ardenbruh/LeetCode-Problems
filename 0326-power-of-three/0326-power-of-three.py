class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0 
        #1162261467 is 3^19, the largest power of 3 that fits in a 32-bit integer.


             