'''
1. Write a Python program to Count all letters, digits, and special symbols from the given string
Input = “P@#yn26at^&i5ve”
Output: Chars = 8 Digits = 3 Symbol = 4
'''

string = input("Enter a string: ")
if string == '':
    string = "P@#yn26at^&i5ve"
print('your string is:', string)
chars = 0
digits = 0
symbols = 0
for i in string:
    if i.isalpha():
        chars += 1
    elif i.isdigit():
        digits += 1
    elif not (i.isalpha() or i.isdigit()):
        symbols += 1
print("Chars:", chars, end=" ")
print("Digits:", digits, end=" ")
print("Symbols:", symbols, end="")
