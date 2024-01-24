def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       
        # not using dp
        # l= []
        # for i in range(n+1):
        #     l.append((bin(i).replace("0b", "")).count('1'))
        # return l
