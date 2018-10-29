class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1]
        res = 1
        for i in range(1, len(nums)):
            tmp = 1
            for j in range(i):
                if nums[i]>nums[j]:
                    tmp = max(tmp, 1+dp[j])
            dp.append(tmp)
            res = max(res, tmp)
        return res

sol = Solution()
nums = []
print(sol.lengthOfLIS(nums))
