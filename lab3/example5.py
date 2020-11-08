month = str(input('Enter the month : '))
day = int(input('Enter the day : '))
if (month=='April' and 1<=day<=30) or (month=='May' and 1<=day<=31) or (month=='March' and 20<=day<=31) or (month=='June' and 1<=day<=20):
    print('You are in Spring Season !')
elif (month=='July' and 1<=day<=31) or (month=='August' and 1<=day<=31) or (month=='June' and 21<=day<=30) or (month=='September' and 1<=day<=21):
    print('You are in Summer Season !')
elif (month=='October' and 1<=day<=31) or (month=='November' and 1<=day<=30) or (month=='September' and 22<=day<=30) or (month=='December' and 1<=day<=20):
    print('You are in Autumn Season !')
elif (month=='January' and 1<=day<=31) or (month=='Februrary' and 1<=day<=29) or (month=='December' and 21<=day<=31) or (month=='March' and 1<=day<=19):
    print('You are in Winter Season !')
else:
    print('Wrong Info! Try Again!')