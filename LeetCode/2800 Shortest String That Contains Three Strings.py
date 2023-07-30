class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def helper(a, b):
            if a in b:
                return b
            if b in a:
                return a
            mx = 0
            aLen = len(a)
            bLen = len(b)

            for i in range(1, min(aLen, bLen)):
                if a[aLen - i :] == b[:i]:
                    mx = max(mx, i)

            ret = a + b[mx:]
            return ret

        lst = []
        lst.append(helper(helper(a, b), c))
        lst.append(helper(helper(a, c), b))
        lst.append(helper(helper(b, a), c))
        lst.append(helper(helper(b, c), a))
        lst.append(helper(helper(c, a), b))
        lst.append(helper(helper(c, b), a))

        shortest = 10**6

        for l in lst:
            if len(l) < shortest:
                shortest = len(l)

        cand = []
        for l in lst:
            if len(l) == shortest:
                cand.append(l)

        cand.sort()
        return cand[0]
