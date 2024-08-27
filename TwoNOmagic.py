#Here the magic code gives Two as answer for any Numbers
a=int(input('Enter your Any number:\t'))
print(f'Frizz your No. {a}')
print(f'Given No. is under Magic')
a=a*3
#print(a)
a=a+6
#print(a)
a=a//3
#print(a)

b=int(input('Enter That number again:\t'))
a=a-b
print(f'Magic finished!!! \n Here\'$ the solution always 2 No. = {a}')
