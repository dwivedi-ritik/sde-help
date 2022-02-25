def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals = sorted(intervals)
        
        previous_interval = intervals[0]
        result = []
        
        for interval in intervals[1:]:
            if previous_interval[1] >= interval[0]:
                previous_interval = [ previous_interval[0] , max(previous_interval[1] , interval[1]) ]
            else:
                result.append(previous_interval)
                previous_interval = interval
        result.append(previous_interval)
        return result