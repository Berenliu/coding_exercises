class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(k, n, t):
            if n==0:
                if k==0 and t>0:
                    return [[]]
                else:
                    return []
            elif n == 1:
                if k == 1 and t>=1:
                    return [[1]]
                else:
                    return []
            else:
                res = []
                for i in range(t, 0, -1):
                    if n>=i:
                        pre_res = helper(k-1, n-i, i-1)
                        if pre_res:
                            res.extend([item + [i] for item in pre_res])
                return res

        return helper(k,n,9)

class Solution2:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(list(range(1, 10)), res, 0, [], k, n)
        return res
    
    def dfs(self, nums, res, index, path, k, n):
        if n < 0:
            return
        elif not n and not k:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, res, i+1, path+[nums[i]], k-1, n-nums[i])
