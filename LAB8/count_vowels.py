'''
4. Write a Python Count vowels in a string
input= “Welcome to Python Assigement”
output= Number of vowels: 9
'''

string = input("Enter a string: ")
if string == '':
    string = "Welcome to Python Assigement"
print('your string is:', string)

count = 0
for i in string:
    if i in "aeiouAEIOU":
        count += 1
print("Number of vowels: ", count)
