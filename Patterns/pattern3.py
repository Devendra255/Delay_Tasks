'''
1
10
101
1010
10101
'''

for i in range(1,6):
    for j in range(i):
        if j%2==0:
            print(1,end="")
        else:
            print(0,end="")
    print()