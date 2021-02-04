n=int(input("number"))
lower=int(input("lower_limit"))
upper=int(input("upper_limit"))
for i in range(1,upper+1):
    if i**n in range(lower,upper+1):
        print(i**n)
    
