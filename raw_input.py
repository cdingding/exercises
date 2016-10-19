x = int(raw_input('Please enter a number: '))
if x > 5:
    print('You entered a number bigger than 5.')
elif x > 0:
    print('You entered a positive number.')
elif x < 0:
    print('You entered a negative number.')
else:
    print('You entered the number 0.')