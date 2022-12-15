class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {} 
        def rec(i , j):
            if i < 0 or j < 0:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if text1[i] == text2[j]:
                ans = 1 + rec(i-1 , j-1)
                cache[(i ,j)] = ans
                return ans
            else:
                ans = max(rec(i-1 , j) , rec(i , j-1))
                cache[(i , j)] = ans
                return ans

        return rec(len(text1)-1 , len(text2)-1)


class Solution: #No cacheing
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def rec(i , j):
            if i < 0 or j < 0: #Base condition
                return 0
            
            if text1[i] == text2[j]: #Choice Diagram
                ans = 1 + rec(i-1 , j-1)
                return ans
            else:
                ans = max(rec(i-1 , j) , rec(i , j-1)) #Choice diagram
                return ans
                
        return rec(len(text1)-1 , len(text2)-1)