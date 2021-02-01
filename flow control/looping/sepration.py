num=int(input("enter the number:"))
i=1
even=0
odd=0
while(i<=num):
    if i%2==0:
        even+=i

    else:
        odd+=i
    i+=1
print(even)
print(odd)
