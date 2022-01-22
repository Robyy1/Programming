myCat = {'size': 'fat', 'color': 'gray', 'dispozition': 'loud'}
print (myCat['size'])  



print('My cat has ' + myCat['color'] + ' fur.')


spam = {12345: 'Luggage combination', 42: 'The Answer'}
print([1,2,3] == [3,2,1])


eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8 }
ham = {'species': 'cat', 'name': 'Zophie', 'age':8}
print(eggs == ham)

print('name' in eggs)
print(eggs)
print('name' not in eggs)


print((list(eggs.keys())))
print(list(eggs.values()))
print(list(eggs.items()))
print(eggs.keys())


for k in eggs.keys():
    print(k)


for v in eggs.values():
    print(k, v)


for i in eggs.items():
    print(i)


print(eggs)
print('cat' in eggs.values())

if 'color' in eggs:
    print(eggs['color'])

print(eggs)
print(eggs.get('age', 0))
print(eggs.get('color', ""))


picnicItems = {'apples': 5, 'cups': 2}
print("I am bringing " + str(picnicItems.get('napkins', 0)) + ' to the picnic.')



print(eggs)
if 'color' not in eggs:
    eggs['color'] = 'black'

print(eggs)
eggs.setdefault('color', 'orange')
print(eggs)


import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():   #or .upper
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)




































