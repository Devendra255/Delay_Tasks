# 1. Write a Python program to sum all the items in a list.

l = list()

while True:
    num = int(input("Enter a number (0 to quit): "))
    if num == 0:
        break
    l.append(num)

print("The list is: ", l)
print("The sum of the list is: ", sum(l))