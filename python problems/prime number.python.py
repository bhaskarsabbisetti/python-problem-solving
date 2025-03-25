a=int(input("enter a number to check if its is prime no are not:"))
for i in range(2,a):
    if a%i==0:
        print("not a prime number")
        break
else:
    print("prime number")