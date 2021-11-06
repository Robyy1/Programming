spam = ['hello', 'hi', 'howdy', 'heyas']

print(spam.index('hello'))
print(spam.index('heyas'))


spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
spam.index('Pooka')

# You need to specify with what list do you want to work with#


spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)


spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)


spam.append('moose')
spam.append('moose')
spam.append('moose')
spam.append('moose')
print(spam)




spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)


del spam[0]
print(spam)


spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
print(spam)




spam = [1, 5, 3.14, 1, -7]
spam.sort()
print(spam)


spam = ['ants', 'cats', 'dogs', 'badgers', 'elephant']
spam.sort()
print(spam)


spam = ['ants', 'cats', 'dogs', 'badgers', 'elephant']
spam.sort(reverse=True)
print(spam)

#Can't deal with numbers and words at the same time#



spam = ['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)


spam = ['a', 'z', 'A', 'Z']
spam.sort()
print(spam)

spam.sort(key=str.lower)
print(spam)



