class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        if len(s) > len(t):
            return False

        s_index = 0
        t_index = 0

        while t_index < len(t):
            if s_index < len(s) and s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1

        return s_index == len(s)
