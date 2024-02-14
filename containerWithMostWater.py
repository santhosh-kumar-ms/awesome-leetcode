def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maxArea = 0
        while(i < j):
            area = (j - i) * min(height[i], height[j])
            maxArea = max(maxArea, area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxArea
