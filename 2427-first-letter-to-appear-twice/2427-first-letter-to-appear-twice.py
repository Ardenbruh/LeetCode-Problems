class Solution:
    def repeatedCharacter(self, s: str) -> str:
        lis = []
        for i in s:
            if i in lis:
                return i
            else:
                lis.append(i)
        