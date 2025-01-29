class Solution:
    def repeatedCharacter(self, s: str) -> str:
        NewSet = set()
        for el in s:
            if el in NewSet:
                return el
            NewSet.add(el)
