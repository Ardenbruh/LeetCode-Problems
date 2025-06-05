class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rdict = Counter(ransomNote)
        mdict = Counter(magazine)

        if rdict & mdict == rdict:
            return True
        return False
        