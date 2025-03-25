#USING  ASCII value 
a=int(input("enter a number"))
sum=0
for i in range(len(str(a))):
    sum+=ord(str(a)[i])-48
    #ord method helps with ascii
print(sum)