def nested(x):
  if not isinstance(x,list):
    return x
  else:
    sum = 0
    for a in x:
        sum += nested(a)
    return sum


print(nested([3, 12, 76, [4, 56, 43], [2, 8], 1500, 75]))

