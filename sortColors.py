def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        i = 0

        def swap(m, n):
            temp = nums[m]
            nums[m] = nums[n]
            nums[n] = temp
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1

####################################################################################

def sortColors(self, nums: List[int]) -> None:
        c0 = c1 = c2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c0 += 1
            elif nums[i] == 1:
                c1 += 1
            elif nums[i] == 2:
                c2 += 1
        for j in range(len(nums)):
            if j >= 0 and j < c0:
                nums[j] = 0
            elif j >= c0 and j < c0 + c1:
                nums[j] = 1
            elif j >= c0 + c1 and j < len(nums):
                nums[j] = 2
