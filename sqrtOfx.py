def mySqrt(self, x: int) -> int:
        l, r = 1, x
        res = 0
        while l <= r:
            mid = l + ((r - l) // 2)
            if mid <= x // mid:
                l = mid + 1
                res = mid
            else:
                 r = mid - 1
        return res
