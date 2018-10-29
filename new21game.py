class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if N >= K+W-1:
            return 1.0
        table = [[0 for _ in range(10*K+1)] for _ in range(K+1)]
        for i in range(1, W+1):
            table[1][i] = i*1./W
        if K >= 2:
            for i in range(2, K+1):
                for j in range(i, N+1):
                    if j < 10*K:
                        for w in range(1, W+1):
                            if i-w > 0:
                                for v in range(w, W+1):
                                    table[i][j] += 1./W*table[i-w][j-v]
                    else:
                        table[i][j] = 1.0
        return table[K][N]

s = Solution()
N = 5
K = 3
W = 3
print(s.new21Game(N,K,W)) 