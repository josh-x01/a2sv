class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        usedArrow = 0
        points.sort()
        bulletRange = points[0]
        for i in range(len(points)):
            cStart = points[i][0]
            cEnd = points[i][1]
            bStart = bulletRange[0]
            bEnd = bulletRange[1]
            if bStart <= cStart <= bEnd or bStart <= cEnd <= bEnd or (cStart < bStart and cEnd > bEnd):
                if bStart <= cStart <= bEnd:
                    bulletRange[0] = cStart
                if bStart <= cEnd <= bEnd:
                    bulletRange[1] = cEnd
            else:
                usedArrow += 1
                bulletRange = points[i]
        #     print(bulletRange)
        # print('all', points)


        return usedArrow+1
