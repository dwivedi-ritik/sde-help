def isAnagram(self, str1: str, str2: str) -> bool:
    chars = [0] * 26
    if len(str1) != len(str2):
        return False
    for s1, s2 in zip(str1, str2):
        is1 = ord(s1)
        is2 = ord(s2)
        chars[97 - is1] = chars[97 - is1] + 1
        chars[97 - is2] = chars[97 - is2] - 1
    for el in chars:
        if el != 0:
            return False
    return True

