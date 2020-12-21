def harmonic(n):
  a=0
  for i in range(n):
    a+=1/(i+1)
  return a

print(harmonic(5))