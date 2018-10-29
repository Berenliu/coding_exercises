class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def combine(nums, k):
            if k==1:
                return [[i] for i in nums]
            else:
                pre_combine_result = combine(nums[:-1], k-1)
                res = []
                for r in pre_combine_result:
                    r.append(nums[-1])
                    res.append(r)
                return res
        return combine(list(range(1, n+1)), k)

s = Solution()
n=4
k=2
print(s.combine(n, k))
print(s.combine(n-1, k))
print(s.combine(n-2, k))