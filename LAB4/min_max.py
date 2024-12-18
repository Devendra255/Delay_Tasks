# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers.
lst = []

# take 5 inputs from user
for i in range(5):
    lst.append(int(input("Enter number: ")))

print(max(lst))
print(min(lst))