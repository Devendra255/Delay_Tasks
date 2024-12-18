'''
-----
----*
---**
--***
-****
*****
'''

# for i in range(6):
#     print(" "*(5-i),end="")
#     for j in range(i, 0, -1):
#         print("*",end="")
#     print()

# Exact Pattern
for i in range(6):
    print("-"*(5-i),end="")
    for j in range(i):
        print("*",end="")
    print()