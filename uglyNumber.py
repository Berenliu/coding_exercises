class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        while num>1:
            if num % 5 == 0:
                num = num // 5
            elif num % 3 == 0:
                num = num // 3
            elif num % 2 == 0:
                num = num // 2
            else:
                return False
        return True

sol = Solution()
num = -2147483648
print(sol.isUgly(num))
