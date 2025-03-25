def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def pn_range(start,end):

    primes=[]
    for num in range(start,end+1):
        if is_prime(num):
            primes.append(num)
    return primes
start=int(input("enter start of range:"))
end=int(input("enter end of range:"))
print(f"prime numbers between {start} and {end}:{pn_range(start,end)} ")