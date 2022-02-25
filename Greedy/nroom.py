# Greedy approach require sorting 
arr = [list(arr) for arr in zip(start , end)]

arr = sorted(arr , key=lambda x:x[-1])
last_m = arr[0][0]-1
total_m = 0

for s , e in arr:
    if last_m < s:
        total_m += 1
        last_m = e
return total_m
