class Solution:
    def decode_ways2(self, s):
        if not s:
            return 0
        d = [0]*(len(s)+1)
        d[0] = 1
        if s[0]=="*":
            d[1] = 9
        elif s[0]!="0":
            d[1] = 1
        for i in range(2, len(s)+1):
            if s[i-1]!="*" and s[i-1]!="0":
                d[i] += d[i-1]
            elif s[i-1]=="*":
                d[i] += 9*d[i-1]
            if s[i-2]=="*":
                if s[i-1]=="*":
                    d[i] += 15*d[i-2]
                elif int(s[i-1])<7:
                    d[i] += 2*d[i-2]
                else:
                    d[i] += d[i-2]
            elif s[i-2]!="0":
                if s[i-1]=="*":
                    if s[i-2]=="1":
                        d[i] += 9*d[i-2]
                    elif s[i-2]=="2":
                        d[i] += 6*d[i-2]
                elif int(s[i-2:i])>0 and int(s[i-2:i])<27:
                    d[i] += d[i-2]
            if d[i]>10**9+7:
                d[i]=d[i]%(10**9+7)
        return d[-1]

sol = Solution()
s = "*********"
print(sol.decode_ways2(s))
