'''
3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
Output:
UpperCase : 5
LowerCase : 18
NumberCase : 5
SpecialCase : 11
'''

string = input("Enter a string: ")
if string == '':
    string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
print('your string is:', string)
upper = 0
lower = 0
number = 0
special = 0
for i in string:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        number += 1
    elif not (i.isalpha() or i.isdigit()):
        special += 1
print("UpperCase:", upper)
print("LowerCase:", lower)
print("NumberCase:", number)
print("SpecialCase:", special)
