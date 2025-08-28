'''
PROBLEM STATEMENT:
Write a function that confirms whether two given passwords match

'''

new_password = input("Enter new password: ")
confirm_password = input("Confirm new password: ")

if new_password == confirm_password:
    print("Passwords match")
elif len(new_password) != len(confirm_password):
    print("Passwords do not match: Lengths differ")
elif new_password == "":
    print("Passwords cannot be empty")
elif new_password.isalnum() == False:
    print("Passwords must be alphanumeric")
elif new_password.islower():
    print("Passwords must contain at least one uppercase letter")
elif new_password.isupper():
    print("Passwords must contain at least one lowercase letter")
elif new_password.isdigit():
    print("Passwords must contain at least one letter")
elif len(new_password) < 8:
    print("Passwords must be at least 8 characters long")
elif new_password.casefold() == confirm_password.casefold():
    print("Passwords match (case insensitive)")
else:
    print("Passwords do not match") 