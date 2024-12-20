# 4. Write a Python program to count and display the vowels of a given text 
# String=”Welcome to python Training”


string = input("Enter a sentence: ")
if string == '':
    string = 'Welcome to python Training'
print('your string is:', string)

only_vowels = ''
count = 0
for i in string:
    if i in "aeiouAEIOU":
        count += 1
        only_vowels += i
print("Number of vowels: ", count)
print("Vowels: ", only_vowels)
