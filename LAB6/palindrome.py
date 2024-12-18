# 2. Python program to check if the given string is a palindrome using loop

word = input("Enter the word: ")

for i in range(len(word)):
    if word[i] != word[len(word)-i-1]:
        print("The word is not a palindrome")
        break
else:
    print("The word is a palindrome")