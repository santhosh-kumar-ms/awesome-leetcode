def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in nums:
            if i in h:
                return True
            h[i] = i
        return False