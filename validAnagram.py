def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False
        alphabets = [0] * 26
        for i in range(n):
            alphabets[ord(s[i]) - ord('a')] += 1
            alphabets[ord(t[i]) - ord('a')] -= 1
        for i in alphabets:
            if i != 0:
                return False
        return True