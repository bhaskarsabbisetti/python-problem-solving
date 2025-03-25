a=int(input("enter first number"))
b=int(input("enter second number"))
sum=0
for i in range(a,b+1):
    sum+=i
print(sum)
#method 2
c=((b*(b+1))/2) - ((a*(a+1))/2) +a
print(c) 