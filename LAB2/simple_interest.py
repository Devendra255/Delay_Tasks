# Take inputs from the user
principal = int(input("Enter the principal amount: ")) # can enter 200 for Rs. 200
rate = float(input("Enter the rate of interest: ")) # can enter 5 for 5% per year
time = int(input("Enter the time in years: ")) # can enter 5 for 5 years

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Print the result
print("The simple interest is:", simple_interest)