def xyz_there(str):
  check = False
  for x in range(len(str)-2):
    if str[x:x+3] == 'xyz':
      if str[x-1] != '.':
        check = True
  return check