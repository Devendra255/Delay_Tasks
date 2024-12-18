# 5. Python program to check the validity of password input by users

password = input("Enter the password: ")
con_pass = input("Enter the confirm password: ")

if password == con_pass:
    print("Password is valid")
else:
    print("Password is not valid")