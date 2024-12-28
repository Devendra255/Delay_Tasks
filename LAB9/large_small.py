# 2. Write a Python program to get the largest and smallest number from a list without builtin functions.

l = list()

while True:
    num = input("Enter a number (Q to quit): ")
    if num.isalpha():
        break
    l.append(int(num))

print("The list is: ", l)

if l:
    small = l[0]
    large = l[0]

    for i in l:
        if i < small:
            small = i
        if i > large:
            large = i

    print("The smallest number is: ", small)
    print("The largest number is: ", large)
else:
    print("The list is empty")