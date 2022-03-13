def lengthOfLongestSubstring(self, s: str) -> int:
    temp = 0
    max = 0
    length = len(s)
    temp_d = {}
    for i in range(length):
        for j in range(i , length):
            if s[j] in temp_d:
                break
            else:
                temp_d[ s[j] ] = 1
        temp = len(temp_d)
        temp_d = {}
        if temp > max:
            max = temp
        temp = 0
    return max