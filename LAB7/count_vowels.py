# 4. Write a Python program to count and display the vowels of a given text 
# String=”Welcome to python Training”

string = "Welcome to python Training"
count = 0
for i in string:
    if i in "aeiouAEIOU":
        count += 1
print("Number of vowels: ", count)