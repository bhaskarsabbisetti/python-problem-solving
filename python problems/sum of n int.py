a=int(input("enter a number:"))
sum=0
for i in range(a+1):
    sum+=i
print(sum)
#method 2
b=(a*(a+1))/2
print(b)
#method 3
def getSum(num):
  if num == 1:
    return 1
  return num + getSum(num-1)

num = a
print(getSum(num))