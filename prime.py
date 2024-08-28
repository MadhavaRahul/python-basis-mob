n=int(input("Enter any No. \t"))
if n>1:
    for i in range(2, int(n/2)+1):
        if n%i ==0:
            print(f'{n} is not a prime no.')
            break
    else:
         print(f'{n} is  a prime no.')
