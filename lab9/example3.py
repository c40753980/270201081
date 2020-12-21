def even(n):
  a = 0
  if len(n)==0:
    return 0
  
  if n[0]%2==0:
    a = 1
  
  return (a + even(n[1:]))



print(even([0,1,2,3,4,5,6]))