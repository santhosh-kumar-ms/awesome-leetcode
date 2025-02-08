def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = suffix = 1

        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        for j in range(n - 1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]

        return res