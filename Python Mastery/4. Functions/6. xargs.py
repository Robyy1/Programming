
# def multiply(x,y):
#     return x * y

# multiply(2,3,4,5)



def multiply(*numbers):
    print(numbers)


multiply(2,3,4,5)



def multiply(*numbers):
    for number in numbers:
        print(number)


multiply(2,3,4,5)


# Very important!


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2,3,4,5))
