#https://leetcode.com/problems/smallest-string-with-swaps/submissions/

from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        par = [ i for i in range(len(s))]
        
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        def union(n1 , n2):
            p1 , p2 = find(n1) , find(n2)
            if p1 != p2:
                par[p2] = p1
        for n1 , n2  in pairs:
            union(n1, n2)
        
        d = defaultdict(list)
        res = list(s)
        for i , el in enumerate(par):
            d[find(el)].append(i)
            
        for k in d.keys():
            ind_list = d[k]
            char_list = [ s[i] for i in ind_list ]
            char_list.sort()
            
            for i , char in zip(ind_list , char_list):
                res[i] = char
        return "".join(res)