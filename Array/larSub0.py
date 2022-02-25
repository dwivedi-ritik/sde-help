#Count number of subarray with 0 sum
def maxLen(arr):
    #Idea is to find the consecutive sum 
    #If that sum repeats this means sum is 0
    obj = {}
    sum_  = 0 
    max_len = 0
    
    for pos , el in enumerate(arr):
        sum_ += el
        
        if sum_ == 0 and max_len < pos+1:
            max_len = pos+1

        if sum_ in obj:
            curr_len = pos - obj[sum_]
            if curr_len > max_len:
                max_len = curr_len
        else:
            obj[sum_] = pos
    return max_len