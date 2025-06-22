class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        m = {n:i for i, n in enumerate(nums1)}
        res = [-1]*len(nums1)
        stack = []

        for el in nums2:
            while stack and stack[-1] < el:
                val = stack.pop()
                idx = m[val]
                res[idx] = el
            if el in m: 
                stack.append(el)
        return res


        
            