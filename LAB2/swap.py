# Takes two Inputs
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

# Swapping operation
num1, num2 = num2, num1

'''
can also be swapped like this:
temp = num1
mum1 = num2
num2 = temp
'''

# Print the swapped numbers
print("Number 1 after swapping: ", num1)
print("Number 2 after swapping: ", num2)