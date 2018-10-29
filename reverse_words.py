class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        word = ""
        for i in range(len(s)-1, -1, -1):
            if s[i]!=" ":
                word = s[i] + word
            elif s[i]==" " and word:
                res = res + word + " "
                word = ""
        res = res + word
        return res

sol = Solution()
s = " "
print(sol.reverseWords(s))