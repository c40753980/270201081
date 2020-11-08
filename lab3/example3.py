gpa=float(input('Enter your GPA : '))
lectures=int(input('Enter number of lectures that you take : '))

if gpa>=2.0:
  if lectures>=47:
    print('Graduated!')
  else:
      print('Not Enough Lectures')
else:
    if lectures>=47:
      print('Not Enough GPA')
    else:
      print('Not Enough Lectures and GPA')
