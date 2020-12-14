def is_prime(n):

  if n<2:

    return False
  
  for i in  range(2,n):

    if (n%i) == 0:

      return False

    else:

      continue

    return True
  


def print_primes_between(s,f):
  
  for i in range(s,f):
    
    if is_prime(i):
      
      print(i,end='')

def main():
  x = int(input('Start: '))
  y = int(input('Finish: '))

  print_primes_between(x,y)

main()