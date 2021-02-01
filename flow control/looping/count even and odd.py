num=int(input("enter the number:"))
i=1
o_count=0
e_count=0
while(i<=num):
    if i%2==0:
       e_count= e_count+1
    else:
       o_count=o_count+1
    i+=1
print("total  umber of even",e_count)
print("total number of odd",o_count)