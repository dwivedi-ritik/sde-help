# Longest increasing subsequence
#Algorithm
#Create total possible increasing sequence at each element in dp array
#Return max of dp array n^2


def lengthOfLIS(self, arr: List[int]) -> int:
        dp = [1]*len(arr)
        length = len(arr)

        for i in range(length):
            j = i-1
            while j >= 0:
                if arr[j] < arr[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j]+1  
                j -= 1

        return max(dp)
