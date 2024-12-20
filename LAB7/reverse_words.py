# 3. Write a Python program to reverse words in a string 
# String = “Deeptech Python Training” 

string = input("Enter a sentence: ")

if string == '':
    string = 'Deeptech Python Training'
print('your string is:', string)

# Entire string reversed
print(string[::-1])

# Only words reversed
words = string.split()
rev = ''
for i in words:
    rev += ''.join(reversed(i))
    rev += ' '
print(rev)
