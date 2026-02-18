from typing import List 
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        # burst range
        burst = [] 
        curr = points[0]
        # merge
        for interval in points[1:]:
            if interval[0] > curr[1] or interval[1] < curr[0]:
                burst.append(curr)
                curr = interval
            else:
                curr = [max(curr[0], interval[0]), min(curr[1], interval[1])]       
        burst.append(curr)
        # the  length of merged list is answer
        return len(burst)