"""This module provides a simple password checker."""

password = input("Enter your password: ")
result = {}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

if any(char.isdigit() for char in password):
    result["digits"] = True
else:
    result["digits"] = False


if any(char.isupper() for char in password):
    result["uppercase"] = True
else:
    result["uppercase"] = False

if all(result.values()):
    print("Strong password!")
else:
    print("Weak password!")
