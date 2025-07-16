# rows=5
# for i in range(rows,0,-1):
#     res=''
#     for space in range(rows-i):
#         res+=' '
#     for j in range(i):
#         res+="*"+' '
#     print(res)
# for i in range(2,rows+1):
#     res=""
#     for space in range(rows-i):
#         res+=" "
#     for j in range(i):
#         res+="*"+' '
#     print(res)

#2nd method
# rows=5
# for i in range(1,2*rows):
#     spaces=i-1 if i<=rows else 2*rows-i-1
#     cols=rows-spaces
#     print((" "*spaces)+("* "*cols))

#alphabet pattern
# rows=5
# code=97
# for i in range(1,2*rows):
#     res=""
#     spaces=rows-i if i<=rows else i-rows
#     res+=" "*spaces
#     cols=i if i<=rows else 2*rows-i
#     for j in range(cols):
#         res+=chr(code)+" "
#         code+=1
#     print(res)

#longest substring
# a=input("enter a string:-")
# l=''
# char=a[0]
# if a.count(char)==len(a):
#     l=char
# else:
#     for i in range(len(a)):
#         temp='' 
#         for j in range(i,len(a)):
#             if a[j] in temp:
#                 break
#             else:
#                 temp+=a[j]
#                 if len(temp)>len(l):
#                     l=temp
# print(l)

#word and its count
# word = 'aaaabbccdddaaa'
# i = 0

# while i < len(word):
#     count = 1
#     while i + 1 < len(word) and word[i] == word[i + 1]:
#         count += 1
#         i += 1
#     print(word[i], count)
#     i += 1

# rows=5
# for i in range(1,2*rows):
#     spaces=rows-i if i<=rows else i-rows
#     cols=i if i<=rows else (2*rows)-i
#     print((" "*spaces)+("* "*cols))

# rows=5
# for i in range((2*rows)-1):
#     spaces=i if i<rows else (2*rows-2)-i
#     cols=rows-spaces
#     print((" "*spaces)+("* "*cols))

#x pattern
# rows=5
# for i in range(rows):
#     for j in range(rows):
#         if (i==j) or (j==rows-i-1):
#             print("*",end='')
#         else:
#             print(' ',end='')
#     print()

#B pattern
for i in range(7):
    for j in range(7):
        if ((i==0 or i==3 or i==6) and j<3) or (j==0) or((i!=0 and i!=3 and i!=6)and j==5):
            print("* ",end='')
        else:
            print(" ",end="")
    print()