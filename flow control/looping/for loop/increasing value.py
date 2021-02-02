num=int(input("enter the number:"))
sum=0
for i in range(1,num+1):
    pattern=(str(num)*i)
    print(pattern)
    sum = sum+(int(pattern))
print("sum=",sum)