# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                pnum = 2
                for k in range(len(points)):
                    if k!=i and k!=j and ifSameline(points[i], points[j], points[k]):
                        pnum += 1
                res = max(res, pnum)
        return res

    def ifSameline(p1, p2, p3):
        if (p1.y-p3.y)*(p2.x-p3.x) == (p2.y-p3.y)*(p1.x-p2.x):
            return True
        else:
            return False

        