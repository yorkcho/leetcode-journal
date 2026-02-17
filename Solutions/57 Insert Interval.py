from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        newList = []
        combined = 0
        current = newInterval
        for i in intervals:
            if current[1]< i[0] or newInterval[0] > i[1]:
                newList.append(i) 
            else:
                current = [min(current[0], i[0]), max(current[1], i[1])]
                combined = 1
        # at last apend the combined interval
        newList.append(current)
        newList.sort()
        return newList
    
                