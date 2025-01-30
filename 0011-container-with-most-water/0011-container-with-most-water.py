class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        i = 0
        j = len(height) - 1
        while i < j:
            f_height = min(height[i],height[j]) 
            width = j - i
            curr_water = f_height * width
            if curr_water > max_water:
                max_water = curr_water
            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
        return max_water

    