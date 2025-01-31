class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for el in intervals:
            if len(res) == 0 or res[-1][1] < el[0]:
                res.append(el)
            else:
                res[-1][1] = max(res[-1][1],el[1])
        return res