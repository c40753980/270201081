def multiply(n):
  if n==1:
    return 3
  else:
    return 3+multiply(n-1)

print(multiply(6))
