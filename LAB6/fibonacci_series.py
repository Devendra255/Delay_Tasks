# 4. Python program to get the Fibonacci series between 0 to 50
'''
# this program gives the first 50 fibonacci numbers
n1 = 0
n2 = 1
n3 = 0
count = 0

print("Fibonacci Series: ")
while count < 50:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1
'''
# this program gives the fibonacci series between 0 to 50
n1 = 0
n2 = 1
n3 = 0
count = 0
print("Fibonacci Series: ")
while n1 <= 50:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
