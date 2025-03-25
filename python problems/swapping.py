#swapping method 1
a=10
b=20
print(a,b)
c=a
a=b
b=c
print(a,b)
#method 2
a,b=b,a
print(a,b)
#method 3
a=a+b
b=a-b
a=a-b
print(a,b)
#method 4
a=a*b
b=a/b
a=a/b
print(int(a),int(b))