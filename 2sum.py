n = len(nums)
for i in range(n):
  for j in range(i+1, n):
    if(nums[i]+nums[j]==target):
      return [i, j]

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

n = len(nums)
h = {}
for i in range(n):
  comp = target - nums[i]
  if comp in h:
    return [h[comp], i]
  h[nums[i]] = i
