class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for _ in range(32):
            res += n&1
            n>>=1
        return res

sol = Solution()
print(sol.hammingWeight(11))