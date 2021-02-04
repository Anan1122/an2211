# num=int(input("enter the number:"))
# pattern=0
# for i in range(1,num+1):
#     pattern=i*'*'
#     print(pattern)
    # pattern=0
    # for count in range(i):
    #     pattern+='*'
    # print(pattern)

n=int(input("number:"))
for i in range(1,n+1):
     for j in range(0,i):
            print("*",end="")
     print()