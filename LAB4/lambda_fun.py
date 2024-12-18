# 5. Write a lambda function that takes one argument and returns 'Positive' if the number is greater than 0, 'Negative' if it's less than 0, and 'Zero' if it's 0. Test it with different numbers.
# using lambda function
f = lambda a: "Positive" if a>0 else "Negative" if a<0 else "Zero"
# Taking input and printing
a = int(input("Enter number: "))
print(f(a))