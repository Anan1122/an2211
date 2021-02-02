num = int(input("enter the number::"))
fact=1
fac=0
if num==0:
    print(1)
else:
    while fact>=num:
        fac=fact*num
        fact+=1
    print(fac)