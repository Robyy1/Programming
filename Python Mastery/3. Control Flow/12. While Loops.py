number = 100
while number > 0:
    print(number)
    number //= 2  # or number = number // 2


command = ""
# old way while command != "quit" and command != "QUIT":
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
