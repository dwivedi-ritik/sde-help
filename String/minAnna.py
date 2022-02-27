def minSteps(self, s: str, t: str) -> int:
        table1 = [0]*26
        table2 = [0]*26
        for c_s , c_t in zip(s , t):
            table1[ord(c_s)- 97] += 1
            table2[ord(c_t)- 97] += 1
            
        count = 0
        for i in range(len(table1)):
            if table2[i] > table1[i]:
                count += table2[i] - table1[i]
                
        return count
