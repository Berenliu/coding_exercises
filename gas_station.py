import time

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        for start in range(n):
            g = gas[start]
            c = cost[start]
            i = 0
            ind = start
            while g>=c and i<n:
                ind = (ind+1)%n
                g = g + gas[ind]
                c = c + cost[ind]
                i += 1
            if i<n:
                continue
            else:
                return start
        return -1

class Solution2(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        diff = [gas[i]-cost[i] for i in range(n)]
        for start in range(n):
            d = diff[start]
            i = 0
            ind = start
            while d>=0 and i<n:
                ind = (ind+1)%n
                d = d + diff[ind]
                i += 1
            if i<n:
                continue
            else:
                return start
        return -1

class Solution3(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        diff = [gas[i]-cost[i] for i in range(n)]
        if sum(diff)<0:
            return -1
        res = 0
        total = 0
        s = 0
        for i in range(n):
            s += diff[i]
            if s<0:
                res = i+1
                total += s
                s = 0
        return res


sol = Solution3()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
st = time.time()
print(sol.canCompleteCircuit(gas, cost))
print(time.time()-st)