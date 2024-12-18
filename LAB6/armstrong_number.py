# 3. Python program to check if a given number is an Armstrong number

num = int(input("Enter the number: "))
temp = num
sum = 0
while temp > 0:
    rem = temp % 10
    sum = sum + rem ** 3 # this only works for 3 digit numbers
    temp = temp // 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")