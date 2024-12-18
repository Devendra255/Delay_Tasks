'''
____1
___01
__101
_0101
10101
''' 

for i in range(5):
    print("_"*(4-i),end="")
    for j in range(i+1):
        if j%2==0:
            print(1,end="")
        else:
            print(0,end="")
    print()