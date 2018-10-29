from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """       
        def comparator(s1, s2):
            k1 = int(s1 + s2)
            k2 = int(s2 + s1)
            return k1 - k2
        nums = [str(i) for i in nums]
        nums.sort(key=cmp_to_key(comparator))
        return "".join(nums[::-1])

nums = [824, 8247]
s = Solution()
print(s.largestNumber(nums))

