# Very Very Asshole type of question

def solve(self, A, B):
    sum_ = 0
    ans = 0
    obj = {}
    for el in A:
        sum_ = sum_ ^ el
        if sum_ == B:
            ans += 1
        
        if sum_ ^ B in obj:
            ans += obj[sum_ ^ B]
        
        if sum_  in obj:
            obj[sum_] += 1
        else:
            obj[sum_] = 1

    return ans