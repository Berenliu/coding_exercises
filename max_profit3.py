class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==1:
            return 0
        if len(prices)==2:
            return max(prices[1]-prices[0], 0)
        def get_max_profit(nums):
            if not prices:
                return 0
            min_cur = prices[0]
            max_profit = 0
            for p in prices[1:]:
                max_profit = max(max_profit, p-min_cur)
                min_cur = min(p, min_cur)
            return max_profit
        dp = [0]*len(prices)
        max_profit = 0
        for i in range(len(prices)):
            left_profit = prices[i]-min(prices[:i+1])
            right_profit = get_max_profit(prices[i+1:])
            max_profit = max(max_profit, left_profit + right_profit)
        return max_profit

class Solution2:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==1:
            return 0
        if len(prices)==2:
            return max(prices[1]-prices[0], 0)
        def get_max_profit(nums):
            if not prices or len(prices)==1:
                return 0
            min_cur = prices[0]
            max_profit = 0
            for p in prices[1:]:
                max_profit = max(max_profit, p-min_cur)
                min_cur = min(p, min_cur)
            return max_profit
        dp = [0]*len(prices)
        max_profit = 0
        min_cur = prices[0]
        for i in range(len(prices)):
            if i<len(prices)-1 and prices[i]>=prices[i+1] and prices[i]>min_cur:
                left_profit = prices[i]-min_cur
                right_profit = get_max_profit(prices[i+1:])
                max_profit = max(max_profit, left_profit + right_profit)
            elif i==len(prices)-1:
                max_profit = max(max_profit, prices[i]-min(prices))
            min_cur = min(min_cur, prices[i])
        return max_profit

class Solution3:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==1:
            return 0
        if len(prices)==2:
            return max(prices[1]-prices[0], 0)
        dp = [0]*len(prices)
        max_profit = 0
        min_cur = prices[0]
        max_cur = prices
        for i in range(len(prices)):
            if i<len(prices)-1 and prices[i]>=prices[i+1] and prices[i]>min_cur:
                left_profit = prices[i]-min_cur
                right_profit = get_max_profit(prices[i+1:])
                max_profit = max(max_profit, left_profit + right_profit)
            elif i==len(prices)-1:
                max_profit = max(max_profit, prices[i]-min(prices))
            min_cur = min(min_cur, prices[i])
        return max_profit


class Solution4(object):
    """docstring for Solution4"""
    def maxProfit(self, prices):
        release1 = release2 = 0
        hold1 = hold2 = float('-inf')
        for i in prices:
            print(hold1, hold2, release1, release2)
            release2 = max(release2, hold2+i)
            hold2 = max(hold2, release1-i)
            release1 = max(release1, hold1+i)
            hold1 = max(hold1, -i)
        print(hold1, hold2, release1, release2)
        return release2
        

sol = Solution4()
prices = [3,2,4,5,7,1]
print(sol.maxProfit(prices))


