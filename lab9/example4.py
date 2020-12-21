import time
def alert(t):
  if t==0:
    return('The end')

  print('Time remaining:',t)
  time.sleep(1)
  return alert(t-1)

print(alert(5))