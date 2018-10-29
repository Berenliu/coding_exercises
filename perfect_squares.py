class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0,1] + [0]*(n-1)
        for i in range(2, n+1):
            tmp = i
            for j in range(1, i):
                if i>=j*j:
                    tmp = min(tmp, 1+dp[i-j*j])
                else:
                    break
            dp[i] = tmp
        return dp[-1]

sol = Solution()
n = 7217
print(sol.numSquares(n))

