class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # l = []
        # for i in range(1,n + 1):
        #     l.append(bin(i)[2:])

        # return all(el in s for el in l)

        return all(bin(i)[2:] in s for i in range(1, n + 1))