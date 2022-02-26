def maxProduct(self, arr: List[int]) -> int:
        cmin , cmax = 1 , 1
        res = -11
        for el in arr:
            if el == 0:
                cmin , cmax = 1 , 1
            temp = cmin*el
            cmin = min(el*cmin , el*cmax , el)
            cmax = max(temp , el*cmax , el)
            res = max(res , cmin , cmax)
        return res
    
