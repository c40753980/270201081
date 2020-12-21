def get_reversed(n):
  if len(n)==0:
    return []
  else:
    return n[::-1] #n.pop() + get_reversed(n[::-1])


print(get_reversed([1,2,3,4,]))