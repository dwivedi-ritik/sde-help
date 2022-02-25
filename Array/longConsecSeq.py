def longestConsecutive(self, nums: List[int]) -> int:
        obj = {}
        for el in nums:
            obj[el] = True
        res = [ k for k in obj if obj.get(k-1) is None]
        max_el = 0
        for el in res:
            count = 0 
            curr_el = el
            while obj.get(curr_el) is not None:
                curr_el += 1
                count += 1
            if count > max_el:
                max_el = count
                
        return max_el