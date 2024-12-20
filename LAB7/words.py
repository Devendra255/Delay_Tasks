# 1. Write a Python program to count the occurrences of each word in a given sentence 
# string = “To change the overall look of your document. To change the look available in the gallery” 

string = input("Enter a sentence: ")
if string == '':
    string = "To change the overall look of your document. To change the look available in the gallery"
print('your sentence is:', string)
words = string.lower().split()
words_set = set(words)

for word in words_set:
    print(word, ":", words.count(word))