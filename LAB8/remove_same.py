'''
2. Write a Python program to remove duplicate words of a given string.
Input = “String and String Function”
Output: String and Function
'''

# this program removes duplicate 'words' from a string
string = input("Enter a string: ")
if string == '':
    string = "String and String Function"
print('your string is:', string)

words = string.lower().split()
words_set = set(words)
new_string = ''
for i in words:
    if i in words_set:
        words_set.remove(i)
        new_string += i
        new_string += ' '
print(new_string)
