class Solution:
    def validIp(self, string):
        if len(string)>12 or len(string)<4:
            return []
        def valid_number(string, n):
            if not string:
                return []
            if n==1:
                if string[0]=="0" and len(string)>1:
                    return []
                if len(string)<=3 and int(string)<256:
                    return [string]
                else:
                    return []
            else:
                res = []
                for i in range(1, 4):
                    if string[0]=="0" and i>1:
                        continue
                    if int(string[:i])<256 and valid_number(string[i:], n-1):
                        for s in valid_number(string[i:], n-1):
                            res.append(string[:i]+"."+s)
                return res
        return valid_number(string, 4)

s = Solution()
string = "010010"
print(s.validIp(string))






