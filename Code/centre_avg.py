def centered_average(nums):
  avg = 0
  
  nums.sort()
  
  for x in nums[1:-1]:
    avg = avg + x
    
  avg = avg / (len(nums)-2)
  return avg