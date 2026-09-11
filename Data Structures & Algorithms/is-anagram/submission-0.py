class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {

        }
        count_t = {

        }
        for x in s:
            if x in count_s:
                count_s[x] += 1
            else:
                count_s[x] = 1
        for x in t:
            if x in count_t:
                count_t[x] += 1
            else:
                count_t[x] = 1
        if count_s == count_t:
            return True
        else:
            return False
        