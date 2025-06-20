class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {"{":"}", "(":")", "[":"]"}
        for el in s:
            if el in m:
                stack.append(el)
            else:
                if len(stack) == 0:
                    return False
                elif m[stack[-1]] == el:
                    stack.pop()
                else:
                    return False

        return True if not stack else False #if not stack = if len(stack) == 0

        # count = 0
        # for el in s:
        #     if count >= 0:
        #         if el == '(' or '{' or '[':
        #             count += 1
        #         else:
        #             count -= 1
                
        # return bool(count)
        #lol this works for (()()) type questions 

