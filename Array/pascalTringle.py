# Pascal Triangle
def generate(numRows: int) -> List[List[int]]:
    print(numRows)

    res = [[1],[1,1],[1,2,1]]
    if len(res) < 4:
        return res[:numRows]
    
    print(numRows)

    numRows -= 3
    while numRows != 0:
        temp = []
        temp.append(1)
        for i in range(len(res[-1]) - 1):
            temp.append(res[-1][i]+res[-1][i+1])
        numRows -= 1
        temp.append(1)
        res.append(temp)
        print(temp)
    return res