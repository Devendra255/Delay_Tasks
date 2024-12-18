'''
*********
-*******
--*****
---***
----*
'''
'''
k = 0
for i in range(9, 0, -2):
    print(" "*(9-i-k),end="")
    for j in range(i):
        print("*",end="")
    print()
    k += 1
'''

# Exact Pattern
k = 0
for i in range(9, 0, -2):
    print("-"*(9-i-k),end="")
    for j in range(i):
        print("*",end="")
    print()
    k += 1