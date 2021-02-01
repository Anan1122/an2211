num=int(input("enter the reversing number"))
while(num!=0):
    digit=num%10
    print(digit,end="")
    num=num//10