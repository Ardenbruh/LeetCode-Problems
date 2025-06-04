class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dic = Counter(nums1) #Makes a Occurance Dict
        res = []
        for num in nums2:
            if dic[num] > 0: #We check if the occurance is more than 0 (repeating)
                res.append(num) #Found the repeat so append in list
                dic[num] -= 1 #Remove the occurance for next checks
        return res