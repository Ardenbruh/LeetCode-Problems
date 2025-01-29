class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = 0  
        for char in s:
            
            bit = ord(char) - ord('a')
           
            if seen & (1 << bit):
                return char
            seen |= (1 << bit)
        return ''
