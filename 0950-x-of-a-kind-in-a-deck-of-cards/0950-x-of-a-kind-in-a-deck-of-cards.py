class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a,b):
            if b == 0:
                return a
            
            return gcd(b, a%b)

        # m = {}
        # for i in deck:
        #     if i not in m:
        #         m[i] = 1
        #     else:
        #         m[i] += 1

        m = Counter(deck)

        g = m[deck[0]]

        for count in m.values():
            g = gcd(max(g,count), min(g,count))
        return g>1