class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)]]*n
        print(dp)
        return self.get_dp_res(dp, 1, n)

    def get_dp_res(self, dp, s, t):
        if s>=t:
            return 0
        print(s, t)
        if dp[s-1][t-1] != 0:
            return dp[s-1][t-1]
        res = float("inf")
        for i in range(s, t):
            tmp = i + max(self.get_dp_res(dp, s, i-1), self.get_dp_res(dp, i+1, t))
            res = min(res, tmp)
        dp[s-1][t-1] = res
        return res

sol = Solution()
n = 3
print(sol.getMoneyAmount(n))