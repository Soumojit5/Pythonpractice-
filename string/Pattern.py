"""
n = int(input("Enter the Number of stars"))
for i in range(0, int(input("Enter The no. of lines: "))):
    for j in range(n):
        print("*", end="")
    print("\n", end="")
"""
"""
row = int(input("Enter The No. of Rows: "))
col = int(input("Enter the no. of Coloumns: "))
for i in range(row):
    for j in range(col):
        if (i == 0) or (j == 0) or (i == (row-1)) or (j == (col-1)):
            print("*", end="")
        else:
            print(" ", end="")
    print("\n", end="")
"""
"""
r = int(input("Enter The range: "))
for i in range(1, r+1):
    for j in range(1, i+1):
        print("*", end="")
    print("\n", end="")
"""

# n = int(input("Enter The Range: "))
# for i in range(n)[::-1]:
#     for j in range(i+1):
#         print("*", end="")
#     print("\n", end="")

"""
n = int(input("Enter The Range: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print("\n", end="")
"""
"""
n = int(input("Enter The Range: "))
for i in range(1, n+1)[::-1]:
    for j in range(1, i+1):
        print(j, end="")
    print("\n", end="")
"""
"""
n = int(input("Enter The Range: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end="")
    print("\n", end="")
"""
