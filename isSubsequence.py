def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        i = j = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1
            i += 1
        if j == len(s):
            return True
        else:
            return False
