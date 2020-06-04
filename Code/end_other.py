def end_other(a, b):
  check = False
  checka = False
  checkb = False
  a = a.lower()
  b = b.lower()
  
  checka = a.endswith(b)
  checkb = b.endswith(a)
        
  if checka == True or checkb == True:
    check = True
  return check