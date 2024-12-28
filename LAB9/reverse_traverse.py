'''
5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.

Original list:
['red', 'green', 'white', 'black']

Traverse the said list in reverse order:
black
white
green
red
'''

l = list()

while True:
    item = input("Enter a number (Enter to use Default): ")
    if item == '':
        break
    l.append(int(item))
    
if not l:
    l = ['red', 'green', 'white', 'black']
    
print("Original list:", l)

print("Traverse the said list in reverse order:")
for i in l[::-1]:
    print(i)