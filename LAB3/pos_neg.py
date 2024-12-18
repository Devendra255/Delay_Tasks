# 3. Python Program to Check if a Number is Positive, Negative or 0

num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is a positive number")
elif num < 0:
    print(f"{num} is a negative number")
else:
    print(f"{num} is zero")