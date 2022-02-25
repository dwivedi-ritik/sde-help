#Algo
# In Fractional Knapsack ration in fractional case will ( current_differ capacity) / current weight into your item value

def fractionalknapsack(self, W,Items,n):
    items = sorted(Items , reverse = True , key = lambda x: (x.value/x.weight))
    profit = 0
    curr_cap = 0
    for item in items:
        if item.weight < (W - curr_cap):
            curr_cap += item.weight
            profit += item.value
        else:
            profit +=  item.value*( (W - curr_cap)/ item.weight)
            break
    return profit

# Problem Link
# https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1#