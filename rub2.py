class Solution(object):
    def rob(self, nums):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        res1 = self.easy_max_profit(nums[1:])
        res2 = self.easy_max_profit(nums[2:-1]) + nums[0]
        return max(res1, res2)

    def easy_max_profit(self, nums):
        if not nums:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            dp = [nums[0], max(nums[0], nums[1])] + [0]*(len(nums)-2)
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            return max(dp[-1], dp[-2])

s = Solution()
nums = [2,3,2]
print(s.rob(nums))