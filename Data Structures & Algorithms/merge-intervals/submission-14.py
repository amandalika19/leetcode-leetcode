class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])
        outputs = [intervals[0]]

        for start, end in intervals:

            lastEnd = outputs[-1][1]

            if start <= lastEnd:
                outputs[-1][1] = max(end, lastEnd)
            else:
                outputs.append([start, end])
        
        return outputs

