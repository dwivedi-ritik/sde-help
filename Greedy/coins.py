	
def minCoins(self, coins, M, V):
    i , j = 0 , 0
    while j < M:
        if sum(coins[i:j+1]) == V:
            return len(coins[i:j+1])
        elif sum(coins[i:j+1]) < V:
            j += 1
	    else:
	        i += 1

