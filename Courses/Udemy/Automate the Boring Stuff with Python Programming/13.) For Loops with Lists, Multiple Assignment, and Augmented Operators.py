for i in range (4):
    print(i)



print(range(4))
print([0, 1, 2, 3])

for i in [0, 1, 2, 3]:
    print(i)



print(range(4))
print(list (range(4)))

print(list(range(0, 100, 2)))
spam = (list(range(0, 100, 2)))
print(spam)



supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

supplies = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', ]
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])



cat = ['fat', 'orange', 'loud']
size = cat[0]
collor = cat[1]
dispozition = cat[2]

print(collor, size, dispozition)


size, collor, dispozition = cat
print(size ,collor ,dispozition)


size ,collor ,dispozition = 'skinny', 'black', 'quiet'
print(size, collor, dispozition)



a = 'AAA'
b = 'BBB'
a, b = b, a
print(a)
print(b)



spam = 42
spam = spam + 1
spam += 1
print(spam)



