class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        res=""
        for key, value in c.items():
            if value == 1:
                return s.find(key)
        return -1


