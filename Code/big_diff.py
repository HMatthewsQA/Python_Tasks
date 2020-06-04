def big_diff(nums):
  mini = 10
  maxi = 0
  diff = 0
  
  for x in nums:
    mini = min(x,mini)
    maxi = max(x,maxi)
  
  diff = maxi - mini
    
  return diff