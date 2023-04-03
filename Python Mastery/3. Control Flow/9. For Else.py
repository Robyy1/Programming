successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break

successful = False
for number in range(1, 4):
    print("Attempt", number, number * ".")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed!")
