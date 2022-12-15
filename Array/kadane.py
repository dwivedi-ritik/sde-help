def maxSubArray(self, nums: List[int]) -> int:
    # initialise the max_sum variable with small value
    max_sum = -10001
    # initialise current sum as 0 
    curr_sum = 0
    for el in nums:
        curr_sum += el
        if curr_sum > max_sum:
            max_sum = curr_sum
        
        if curr_sum < 0:
            curr_sum = 0
            
     return max_sum
     # Time complexity - O(n)
     # Space Complexity - O(1)
    