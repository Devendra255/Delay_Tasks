'''
4. Write a Python program to split a given list into two parts where the length of the first part of the list is given.

Original list:
[1, 1, 2, 3, 4, 4, 5, 1]

Length of the first part of the list: 3
Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])
'''

l = list()

while True:
    item = input("Enter a number (Enter to use Default): ")
    if item == '':
        break
    l.append(int(item))
    
if not l:
    l = [1, 1, 2, 3, 4, 4, 5, 1]
    
print("Original list:", l)

n = int(input("Enter the length of the first part of the list: "))
print("Original list:", l)
print("Splitted the said list into two parts:", l[:n], l[n:])