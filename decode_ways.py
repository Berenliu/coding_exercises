class Solution:
    def decodeWays(self, s):
        if not s:
            return 0
        d = [0]*(len(s)+1)
        d[0] = 1
        if s[0] != "0":
            d[1] = 1
        for i in range(2, len(s)+1):
            if s[i-1]=="0" and int(s[i-2])>2:
                continue
            if s[i-1]!="0":
                d[i] += d[i-1]
            if s[i-2]!="0" and int(s[i-2:i])>0 and int(s[i-2:i])<27:
                if i>2:
                    d[i] += d[i-2]
                else:
                    d[i] += 1
        return d[-1]

s = "01"
sl = Solution()
print(sl.decodeWays(s))

