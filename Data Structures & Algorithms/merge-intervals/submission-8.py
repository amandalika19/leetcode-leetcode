class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        output = [intervals[0]]

        for s,e in intervals:

            laste = output[-1][1]

            if s <= laste:
                output[-1][1] = max(laste, e)
            else:
                output.append([s,e])
        
        return output
