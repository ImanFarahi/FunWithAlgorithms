class Solution(object):
    def smallestGoodBase(self, n):
        n = int(n)
        for m in range(int(math.log(n, 2)), 1, -1):
            k = int(n ** (1.0 / m))
            if sum(k ** i for i in range(m + 1)) == n:
                return str(k)
        return str(n - 1)
