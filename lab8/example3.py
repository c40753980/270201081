import random
random.seed(123)

def get_list(b,e,N):

  rl = l1 = random.sample(range(b,e),N)

  return rl

def main():

  l1 = get_list(b=0,e=10,N=5)
  l2 = get_list(b=0,e=10,N=5)

  print(l1)
  print(l2)


main()