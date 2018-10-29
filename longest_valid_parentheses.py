class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                if stack and s[stack[-1]]=="(":
                    stack.pop()
                else:
                    stack.append(i)
        if not stack:
            return len(s)
        print(stack)
        end = len(s)
        st = 0
        res = 0
        while stack:
            st = stack.pop()
            res = max(res, end-st-1)
            end = st
        res = max(st, res)
        return res

sol = Solution()
s = "())"
print(sol.longestValidParentheses(s))
