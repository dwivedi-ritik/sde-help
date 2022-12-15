
def longestCommonSubstr(s1, s2, n, m):
    # code here
    maxans = 0
    table = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1 , n+1):
        for j in range(1 , m+1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
                maxans = max(maxans , table[i][j])
    return maxans



ans = longestCommonSubstr("adac" , "adadac" , 4 , 6)

print(ans)
