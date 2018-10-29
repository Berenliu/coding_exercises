class Solution:
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)
        d = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i==0 and j==0:
                    d[i][j] = 0
                elif i==0 and j!=0:
                    d[i][j] = j
                elif j==0 and i!=0:
                    d[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        d[i][j] = d[i-1][j-1]
                    else:
                        d[i][j] = 1 + min(d[i-1][j], d[i][j-1], d[i-1][j-1])
        # for row in d:
        #     for item in row:
        #         print(item, end=" ")
        #     print()
        return d[n][m]

word1="intention"
word2="execution"

s = Solution()
print(s.minDistance(word1, word2))
