class Solution:
    def repeatedCharacter(self, s: str) -> str:
        lis = []
        for i in s:
            if i not in lis:
                lis.append(i)
            else:
                return i
        