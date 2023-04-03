# Method 1:

age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# Method 2:

age = 22
if age >= 18:
    message = ("Eligible")
else:
    message = ("Not eligible")
print(message)

# Method 3:(Ternary Operator)

message = "ELigible" if age >= 18 else "Not eligible"
print(message)
