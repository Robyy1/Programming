spam = 43 #global variable

def eggs():
    spam = 43 #local variable

print("some code here.")
print('some more code.')





def spoon():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spoon()




def soup():
    oil = 'Hello'
    print(oil)

oil = 42
soup()
print(oil)





def stick():
    global oil
    oil = 'Hello'
    print(oil)

oil = 69
stick()
print(oil)




















