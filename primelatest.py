n=int(input("Oi!Gimme no.:\t"))
if n>1:
    for i in range(2,(n//2)+1):#i is use for divide 2 to half of no. +1 for least no to module
        if n%i==0:
            print("{0} is composite no.".format(n))
            break
    else:
        print("{0} is prime no.".format(n))
        