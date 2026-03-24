class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lenghts are not equal then automatically it is not an anagram
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            # return 0 if any value is not in the string
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
