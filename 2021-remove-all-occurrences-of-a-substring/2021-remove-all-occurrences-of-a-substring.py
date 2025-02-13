class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # stack = []
        # n = len(part)

        # for char in s:
        #     stack.append(char)

        #     if len(stack) >= n and "".join(stack[-n:]) == part:
        #         del stack[-n:]
        
        # return "".join(stack)


        while part in s:
            s = s.replace(part, "", 1)
        return s