class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        outputs = [intervals[0]]

        for s, e in intervals:
        
            laste = outputs[-1][1]

            if s <= laste:
                outputs[-1][1] = max(e, laste)
            else:
                outputs.append([s, e])
        
        return outputs
            