from collections import Counter

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        c = Counter(nums)
        if not nums:
            return [[]]
        res = []
        k = c[nums[-1]]
        pre_result = self.subsetsWithDup(nums[:-k])
        for i in range(c[nums[-1]]+1):
            for s in pre_result:
                res.append(s+ [nums[-1]]*i)
        return res

class Solution2(object):
    """docstring for Solution2"""
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            print("="*20)
            print(res)
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
                print(res)
            print("="*20)
        return res
       

s = Solution()
nums = [1]*10+[2]*10+[3]*10+[4]*50
print(s.subsetsWithDup(nums))
