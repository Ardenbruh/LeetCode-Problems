class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for el in s:
            if not stack or stack[-1] != el:
                stack.append(el)
            else:
                stack.pop()

        return "".join(stack)