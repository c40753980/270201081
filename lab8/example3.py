import random
random.seed(123)

def get_list(b,e,N):

  rl = l1 = random.sample(range(b,e),N)

  return rl

def get_overlap(L1,L2):

  L3 = []

  for i in L1:

    if i in L2:

      L3.append(i)

  return L3


def main():

  l1 = get_list(b=0,e=10,N=5)
  l2 = get_list(b=0,e=10,N=5)

  print(l1)
  print(l2)

  l3 =get_overlap(l1,l2)

  print(l3)


main()