eq1 = input("Enter the first equation:\n")
eq2 = input("Enter the second equation:\n")

# Left side of equation 1
left_side_eq1 = ''
left_x_eq1 = ''
left_y_eq1 = ''
left_const_eq1 = ''

# Left side of equation 2
left_side_eq2 = ''
left_x_eq2 = ''
left_y_eq2 = ''
left_const_eq2 = ''

#Right side of equation 1
right_side_eq1 = ''
right_x_eq1 = ''
right_y_eq1 = ''
right_const_eq1 = ''

#Right side of equation 2
right_side_eq2 = ''
right_x_eq2 = ''
right_y_eq2 = ''
right_const_eq2 = ''

# Empty Strings for coding of equation 1
numbers_left_eq1 = ''
numbers_right_eq1 = ''

# Empty Strings for coding of equation 2
numbers_left_eq2 = ''
numbers_right_eq2 = ''

#After Simplifiying both sides equation 1
simple_x_eq1 = ''
simple_y_eq1 = ''
simple_const_eq1 = ''

#After Simplifiying both sides equation 2
simple_x_eq2 = ''
simple_y_eq2 = ''
simple_const_eq2 = ''


# seperating left and right side in eq1
for i in (eq1):
    if i == "=":
        break
    else:
        left_side_eq1 = left_side_eq1 + i
        z = eq1.replace(left_side_eq1, '')

right_side_eq1 = z.replace('=', '')

# seperating left and right side in eq2
for i in (eq2):
    if i == "=":
        break
    else:
        left_side_eq2 = left_side_eq2 + i
        k = eq2.replace(left_side_eq2, '')

right_side_eq2 = k.replace('=', '')

# Seperating x and y and constants in eq1 (left side)
for j in (left_side_eq1):
    if j=="x":
        left_x_eq1 += (numbers_left_eq1)
        numbers_left_eq1 = ''
        continue
    elif j=="y":
        left_y_eq1 += (numbers_left_eq1)
        numbers_left_eq1 = ''
        continue
    else:
         if (j == '-' or j == '+') and numbers_left_eq1 != '':
              left_const_eq1 += (numbers_left_eq1)
              numbers_left_eq1 = j
              continue


    numbers_left_eq1 += j
if numbers_left_eq1 != '':
    left_const_eq1 += (numbers_left_eq1)

for j in (left_side_eq2):
    if j=="x":
        left_x_eq2 += (numbers_left_eq2)
        numbers_left_eq2 = ''
        continue
    elif j=="y":
        left_y_eq2 += (numbers_left_eq2)
        numbers_left_eq2 = ''
        continue
    else:
         if (j == '-' or j == '+') and numbers_left_eq2 != '':
              left_const_eq2 += (numbers_left_eq2)
              numbers_left_eq2 = j
              continue

    numbers_left_eq2 += j
if numbers_left_eq2 != '':
    left_const_eq2 += (numbers_left_eq2)
# Seperating x and y and constants in eq1 (right side)

for i in (right_side_eq1):
    if i=="x":
        right_x_eq1 += (numbers_right_eq1)
        numbers_right_eq1 = ''
        continue
    elif i=="y":
        right_y_eq1 += (numbers_right_eq1)
        numbers_right_eq1 = ''
        continue
    else:
         if (i == '-' or i == '+') and numbers_right_eq1 != '':
              right_const_eq1 += (numbers_right_eq1)
              numbers_right_eq1 = i
              continue

    numbers_right_eq1 += i
if numbers_right_eq1 != '':
    right_const_eq1 += (numbers_right_eq1)

for i in (right_side_eq2):
    if i=="x":
        right_x_eq2 += (numbers_right_eq2)
        numbers_right_eq2 = ''
        continue
    elif i=="y":
        right_y_eq2 += (numbers_right_eq2)
        numbers_right_eq2 = ''
        continue
    else:
         if (i == '-' or i == '+') and numbers_right_eq1 != '':
              right_const_eq2 += (numbers_right_eq2)
              numbers_right_eq2 = i
              continue

    numbers_right_eq2 += i
if numbers_right_eq2 != '':
    right_const_eq2 += (numbers_right_eq2)

# Simplifiying the equation 1

if (left_x_eq1 == '' or right_x_eq1 == ''):

# x
        if left_x_eq1 == '' and right_x_eq1 != '':
            simple_x_eq1 = -(eval(right_x_eq1))
        elif right_x_eq1 == '' and left_x_eq1 != '':
            simple_x_eq1 = (eval(left_x_eq1))
        elif left_x_eq1 == '' and right_x_eq1 == '':
            simple_x_eq1 = ''
else:
    simple_x_eq1 = (eval(left_x_eq1) - eval(right_x_eq1))


# y
if  (left_y_eq1 == '' or right_y_eq1 == ''):
        if left_y_eq1 == '' and right_y_eq1 != '' :
            simple_y_eq1 = -(eval(right_y_eq1))
        elif right_y_eq1 == '' and left_y_eq1 != '' :
            simple_y_eq1 = eval(left_y_eq1)
        elif left_y_eq1 == '' and right_y_eq1 == '':
            simple_y_eq1 =''
else:
    simple_y_eq1 = eval(left_y_eq1) - eval(right_y_eq1)

# Constants
if (left_const_eq1 == '' or right_const_eq1 == ''):
        if left_const_eq1 == '' and right_const_eq1 != '':
            simple_const_eq1 = eval(right_const_eq1)
        elif right_const_eq1 == '' and left_const_eq1 != '':
            simple_const_eq1 = -(eval(left_const_eq1))
        elif left_const_eq1 == '' and right_const_eq1 == '':
            simple_const_eq1 = ''
else:
    simple_const_eq1 = -eval(left_const_eq1) + eval(right_const_eq1)

# Simplifiying the equation 2
if (left_x_eq2 == '' or right_x_eq2 == ''):

# x equation 2
        if left_x_eq2 == '' and right_x_eq2 != '':
            simple_x_eq2 = (eval(right_x_eq2))
        elif right_x_eq2 == '' and left_x_eq2 != '':
            simple_x_eq2 = (eval(left_x_eq2))
        elif left_x_eq2 == '' and right_x_eq2 == '':
            simple_x_eq2 = ''
else:
    simple_x_eq2 = (eval(left_x_eq2) - eval(right_x_eq2))


# y equation 2
if  (left_y_eq2 == '' or right_y_eq2 == ''):
        if left_y_eq2 == '' and right_y_eq2 != '':
            simple_y_eq2 = -(eval(right_y_eq2))
        elif right_y_eq2 == '' and left_y_eq2 != '':
            simple_y_eq2 = eval(left_y_eq2)
        elif left_y_eq2 == '' and right_y_eq2 == '':
            simple_y_eq2 =''
else:
    simple_y_eq2 = eval(left_y_eq2) - eval(right_y_eq2)


# Constants equation 2
if (left_const_eq2 == '' or right_const_eq2 == ''):
        if left_const_eq2 == '' and right_const_eq2 != '':
            simple_const_eq2 = eval(right_const_eq2)
        elif right_const_eq2 == '' and left_const_eq2 != '':
            simple_const_eq2 = -(eval(left_const_eq1))
        elif left_const_eq2 == '' and right_const_eq2 == '':
            simple_const_eq2 = ''
else:
    simple_const_eq2 = -eval(left_const_eq2) + eval(right_const_eq2)


print("Equations in the simplified form:")

if (simple_y_eq1=='') or (simple_x_eq1==''):
    if (simple_y_eq1==''):
        print(str(simple_x_eq1)+'x+0'+str(simple_y_eq1)+'y'+'='+str(simple_const_eq1))
    else:
        print('0'+str(simple_x_eq1)+'x+'+str(simple_y_eq1)+'y'+'='+str(simple_const_eq1))

elif (simple_y_eq1)>=0 :
    print(str(simple_x_eq1)+'x+'+str(simple_y_eq1)+'y'+'='+str(simple_const_eq1))

else:
    print(str(simple_x_eq1)+'x'+str(simple_y_eq1)+'y'+'='+str(simple_const_eq1))

if (simple_y_eq2=='') or (simple_x_eq2==''):
    if (simple_y_eq2 == ''):
        print(str(simple_x_eq2) + 'x+0' + str(simple_y_eq2) + 'y' + '=' + str(simple_const_eq2))
    else:
        print('0' + str(simple_x_eq2) + 'x+' + str(simple_y_eq2) + 'y' + '=' + str(simple_const_eq2))

elif (simple_y_eq2)>=0 :
    print(str(simple_x_eq2)+'x+'+str(simple_y_eq2)+'y'+'='+str(simple_const_eq2))

else:
    print(str(simple_x_eq2)+'x'+str(simple_y_eq2)+'y'+'='+str(simple_const_eq2))


print("Solution:")
# y for eqaution 1
if simple_x_eq2 == '' or simple_y_eq1 == '' or simple_y_eq1=='0' or simple_x_eq2 == '0':
    a = 0
else:
    a = -simple_x_eq2 * simple_y_eq1
# Constant for equation 1
if simple_x_eq2 == '' or simple_const_eq1 == '' or simple_x_eq2=='0' or simple_const_eq1 == '0':
    b = 0
else:
    b = -simple_x_eq2*simple_const_eq1
# y for equation 2
if simple_x_eq1 == '' or simple_y_eq2 == '' or simple_y_eq2=='0' or simple_x_eq1 == '0':
    c = 0
else:
    c = simple_x_eq1*simple_y_eq2
# Constant for equation 2
if simple_x_eq1 == '' or simple_const_eq2 == '' or simple_const_eq2=='0' or simple_x_eq1 == '0':
    d = 0
else:
    d = simple_x_eq1*simple_const_eq2

y = (b+d)/(a+c)

if (simple_y_eq1 == '0' or simple_y_eq1 == '') or (simple_y_eq2 == '0' or simple_y_eq2 == ''):
    if (simple_y_eq1 == '0' or simple_y_eq1 == ''):
        x=int(simple_const_eq1)/int(simple_x_eq1)
    elif (simple_y_eq2 == '0' or simple_y_eq2 == ''):
        x=int(simple_const_eq2)/int(simple_x_eq2)
else:
    x=(int(simple_const_eq2)-int(simple_y_eq2*int(y)))/(int(simple_x_eq2))

print('x='+str(int(x)))
print('y='+str(int(y)))