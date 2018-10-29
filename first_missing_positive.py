class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        exist_pos_nums = set()
        for n in nums:
            if n>0 and n not in exist_pos_nums:
                exist_pos_nums.add(n)
        for i in range(len(exist_pos_nums)):
            if i+1 not in exist_pos_nums:
                return i+1
        else:
            return len(exist_pos_nums)+1

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, n in enumerate(nums):
            if n <= len(nums) and n>0:
                nums[i], nums[n-1] = nums[n-1], nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        else:
            return len(nums)+1

s = Solution()
nums = [3,4,-1,1]
print(s.firstMissingPositive(nums))
print(nums)
