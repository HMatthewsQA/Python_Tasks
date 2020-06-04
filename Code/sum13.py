def sum13(nums):
  sums = 0
  skip = False
  for x in range(len(nums)):
    if nums[x] == 13:
      skip = True
      continue
    if skip:
      skip = False
      continue
    sums = sums + nums[x]
  return sums