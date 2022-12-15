# Difficulty easy 

def climbStairs(self, n: int) -> int:
    ways = 0
    memo = {}
    def rec(i , n ):
        if i in memo:
            return memo[i]
        if i >n:
            return 0
        if i == n:
            return 1
        memo[i] = rec(i+1 , n) + rec(i+2 , n)
        return memo[i]
    
    ways = rec(0 , n)
    return ways
        