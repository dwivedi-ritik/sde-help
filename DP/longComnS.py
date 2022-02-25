def lcs(self , s1 , s2 , i , j , obj):
        
        if i < len(s1) and j < len(s2):
            
            if obj.get((i , j)):
                return obj[(i , j)]
            if s1[i] == s2[j]:
                obj[(i , j)] =  1 + self.lcs(s1 , s2 , i+1 , j + 1 , obj)
                return obj[(i , j)]

            else:
                obj[(i , j)] = max(self.lcs(s1 , s2 , i + 1 , j , obj) , self.lcs(s1 , s2 , i , j+1 , obj))	

                return obj[(i , j)]
        return 0
    
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    n = self.lcs( text1 , text2 , 0 , 0 , {})
    return n
