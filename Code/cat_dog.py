def cat_dog(str):
  yesno = False
  countcat = 0
  countdog = 0
  for x in range(len(str)-1):
    if str[x:x+3] == 'cat':
      countcat += 1
  for x in range(len(str)-1):
    if str[x:x+3] == 'dog':
      countdog += 1
  if countdog == countcat:
    yesno = True
  else:
    yesno = False
      
  return yesno