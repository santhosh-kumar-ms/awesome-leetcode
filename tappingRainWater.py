def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        wSum = 0
        while(l < r):
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                wSum += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                wSum += maxR - height[r]
        return wSum
