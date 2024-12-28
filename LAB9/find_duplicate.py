# 3. Write a Python program to find duplicate values from a list and display those.

l = list()

while True:
    item = input("Enter a element (Enter to quit): ")
    if item == "":
        break
    l.append(item)

print("The list is: ", l)

d_found = []
for i in l:
    if i not in d_found:
        if l.count(i) > 1:
            print(f"{i} is a duplicate element appears {l.count(i)} times")
            d_found.append(i)