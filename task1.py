#star y pattern
# for i in range(5):
#     for j in range(5):
#         if (j==2 and i>1) or (i==j and j<2) or (i==0 and j==4) or (i==1 and j==3):
#             print("*",end="")
#         else:
#             print(" ",end='')
#     print()

#method 2
# rows=9
# for i in range(rows):
#     for j in range(rows):
#         if (i<=rows//2 and (j==i or j==rows-i-1)):
#             print("*",end="")
#         elif ((i>rows//2) and (j==rows//2)):
#             print("*",end="")
#         else:
#             print(" ",end='')
#     print()

#star m pattern
# for i in range(7):
#     for j in range(7):
#         if (j==0 or j==6)or (i==j and j<=3) or (i==1 and j==5) or (i==2 and j==4):
#             print("*",end="")
#         else:
#             print(" ",end='')
#     print()

rows = 7  # Choose how tall the 'M' should be

for i in range(rows):
    for j in range(rows):
        if j == 0 or j == rows - 1:  # Left and right vertical lines
            print("*", end="")
        elif i == j and i <= rows // 2:  # Left diagonal (top half)
            print("*", end="")
        elif i + j == rows - 1 and i <= rows // 2:  # Right diagonal (top half)
            print("*", end="")
        else:
            print(" ", end="")
    print()
