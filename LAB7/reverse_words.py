# 3. Write a Python program to reverse words in a string 
# String = “Deeptech Python Training” 

string = "Deeptech Python Training"
# Entire string reversed
print(string[::-1])

# Only words reversed
words = string.split()
rev = ''
for i in words:
    rev += ''.join(reversed(i))
    rev += ' '
print(rev)
